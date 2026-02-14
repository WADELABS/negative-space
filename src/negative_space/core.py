"""
Core data structures for the Negative Space Framework.
"""

from typing import Dict, List, Optional, Any, Tuple, Set, Union
from dataclasses import dataclass, field, asdict
from enum import Enum, auto
from datetime import datetime
import networkx as nx
import numpy as np
from dataclasses_json import dataclass_json

class VoidType(Enum):
    """Categories of void (what's missing)."""
    DEPENDENCY_GAP = auto()      # Missing parts/components
    INFORMATION_GAP = auto()      # Missing knowledge/data
    CONSTRAINT_GAP = auto()       # Missing permissions/abilities
    CAPABILITY_GAP = auto()       # Missing skills/tools
    CONCEPTUAL_GAP = auto()       # Missing understanding/frameworks
    CAUSAL_GAP = auto()           # Missing causal relationships
    TEMPORAL_GAP = auto()         # Missing temporal understanding
    ETHICAL_GAP = auto()          # Missing ethical considerations

class GapCertainty(Enum):
    """Certainty level about a gap's existence."""
    DEFINITE = auto()            # Gap definitely exists
    HYPOTHESIZED = auto()        # Gap likely exists
    SPECULATIVE = auto()         # Gap might exist
    EMERGENT = auto()            # Gap emerges from system dynamics

class GapCriticality(Enum):
    """How critical the gap is to reaching B."""
    BLOCKING = auto()           # Cannot reach B without filling
    HIGH = auto()               # Significantly impedes progress
    MEDIUM = auto()             # Slows progress
    LOW = auto()                # Minor impediment
    UNKNOWN = auto()            # Impact unclear

@dataclass_json
@dataclass
class Gap:
    """A specific void/gap between A and B."""
    id: str
    description: str
    void_type: VoidType
    
    # Characterization
    domains: List[str]                 # Which domains this gap affects
    evidence: List[Dict[str, Any]]     # Evidence for gap existence
    manifestations: List[str]          # How gap manifests
    
    # Properties
    criticality: GapCriticality
    certainty: GapCertainty
    size: float = 0.5                  # Estimated size of gap (0-1)
    clarity: float = 0.5               # How clearly defined the gap is
    
    # Relationships
    dependencies: List[str] = field(default_factory=list)      # Gaps this depends on
    blockers: List[str] = field(default_factory=list)          # What this gap blocks
    discovered_by: str = "unknown"     # Method of discovery
    discovery_time: datetime = field(default_factory=datetime.now)
    
    # Fillability assessment
    fillable: bool = True              # Can this gap be filled?
    fill_methods: List[str] = field(default_factory=list)      # Possible ways to fill
    fill_cost: float = 0.0             # Estimated cost to fill
    fill_time: float = 0.0             # Estimated time to fill
    
    # Negative space properties
    negative_shape: Dict[str, Any] = field(default_factory=dict)  # Shape of what's missing
    boundary_conditions: List[str] = field(default_factory=list)   # Where gap begins/ends
    
    def calculate_negative_shape(self):
        """Calculate the 'shape' of what's missing."""
        # This is metaphorical - defines properties of the void
        shape = {
            "dimensionality": self._estimate_dimensionality(),
            "connectivity": len(self.dependencies),
            "opacity": 1.0 - self.clarity,
            "edge_sharpness": self._calculate_edge_sharpness(),
            "void_depth": self.size * self.criticality.value if hasattr(self.criticality, 'value') else self.size
        }
        
        self.negative_shape = shape
    
    def _estimate_dimensionality(self) -> int:
        """Estimate how many dimensions the gap spans."""
        # Count distinct domains and manifestation types
        domain_count = len(set(self.domains))
        manifestation_count = len(set(self.manifestations))
        
        return min(5, domain_count + manifestation_count)
    
    def _calculate_edge_sharpness(self) -> float:
        """Calculate how sharply defined the gap boundaries are."""
        # Based on clarity and evidence
        evidence_strength = min(1.0, len(self.evidence) / 5)
        return (self.clarity + evidence_strength) / 2

@dataclass_json
@dataclass
class VoidMap:
    """Complete map of what's missing between A and B."""
    id: str
    point_a: Dict[str, Any]           # Current state
    point_b: Dict[str, Any]           # Goal state
    timestamp: datetime
    
    # The void itself
    gaps: List[Gap] = field(default_factory=list)
    gap_network: nx.Graph = field(default_factory=nx.Graph)
    
    # Negative space metrics
    void_density: float = 0.0          # How much is missing (0-1)
    connectivity: float = 0.0          # How gaps relate to each other
    navigability: float = 0.0          # How navigable the void is
    
    # Discovery process
    discovery_method: str = "unknown"
    exploration_depth: int = 0
    confidence: float = 0.0
    
    def calculate_void_density(self) -> float:
        """Calculate how much is missing vs present."""
        if not self.gaps:
            return 0.0
        
        # Weight gaps by criticality and certainty
        total_weight = 0.0
        for gap in self.gaps:
            weight = self._gap_weight(gap)
            total_weight += weight
        
        # Normalize by number of possible gaps (estimated)
        estimated_gaps = len(self._estimate_possible_gaps())
        if estimated_gaps > 0:
            return min(1.0, total_weight / estimated_gaps)
        return total_weight / 10  # Arbitrary scaling
    
    def _gap_weight(self, gap: Gap) -> float:
        """Calculate weight of a gap."""
        criticality_weights = {
            GapCriticality.BLOCKING: 1.0,
            GapCriticality.HIGH: 0.7,
            GapCriticality.MEDIUM: 0.4,
            GapCriticality.LOW: 0.2,
            GapCriticality.UNKNOWN: 0.5
        }
        
        certainty_weights = {
            GapCertainty.DEFINITE: 1.0,
            GapCertainty.HYPOTHESIZED: 0.7,
            GapCertainty.SPECULATIVE: 0.3,
            GapCertainty.EMERGENT: 0.5
        }
        
        return (criticality_weights.get(gap.criticality, 0.5) * 
                certainty_weights.get(gap.certainty, 0.5))
    
    def build_gap_network(self):
        """Build network showing relationships between gaps."""
        self.gap_network = nx.Graph()
        
        for gap in self.gaps:
            self.gap_network.add_node(
                gap.id,
                type=gap.void_type.name,
                criticality=gap.criticality.name,
                certainty=gap.certainty.name
            )
        
        # Add edges for related gaps
        for i, gap1 in enumerate(self.gaps):
            for gap2 in self.gaps[i+1:]:
                if self._are_gaps_related(gap1, gap2):
                    self.gap_network.add_edge(
                        gap1.id, gap2.id,
                        relationship=self._determine_relationship(gap1, gap2)
                    )
        
        # Calculate network metrics
        if len(self.gap_network.nodes) > 0:
            self.connectivity = nx.density(self.gap_network)
            
            # Calculate navigability (how easy to navigate the gap space)
            try:
                # Use betweenness centrality as proxy for navigability
                centralities = nx.betweenness_centrality(self.gap_network)
                self.navigability = 1.0 - (max(centralities.values()) if centralities else 0)
            except:
                self.navigability = 0.5
    
    def _estimate_possible_gaps(self) -> List[str]:
        """Estimate possible gaps based on A and B."""
        possible = []
        
        # Check for obvious mismatches
        a_keys = set(self.point_a.keys())
        b_keys = set(self.point_b.keys())
        
        # Missing in A that B requires
        for key in b_keys - a_keys:
            possible.append(f"missing_{key}_in_a")
        
        # Type mismatches
        for key in a_keys & b_keys:
            a_type = type(self.point_a[key]).__name__
            b_type = type(self.point_b[key]).__name__
            if a_type != b_type:
                possible.append(f"type_mismatch_{key}")
        
        # Value disparities
        for key in a_keys & b_keys:
            if isinstance(self.point_a[key], (int, float)) and isinstance(self.point_b[key], (int, float)):
                if abs(self.point_a[key] - self.point_b[key]) > 0:
                    possible.append(f"value_gap_{key}")
        
        return possible
    
    def _are_gaps_related(self, gap1: Gap, gap2: Gap) -> bool:
        """Determine if two gaps are related."""
        # Same type
        if gap1.void_type == gap2.void_type:
            return True
        
        # Dependency relationship
        if (gap1.void_type == VoidType.DEPENDENCY_GAP and 
            gap2.void_type in [VoidType.CAPABILITY_GAP, VoidType.INFORMATION_GAP]):
            return True
        
        # Causal relationship
        if (gap1.void_type == VoidType.CAUSAL_GAP and 
            gap2.void_type == VoidType.INFORMATION_GAP):
            return True
        
        # Check if domains overlap
        if set(gap1.domains) & set(gap2.domains):
            return True
        
        return False
    
    def _determine_relationship(self, gap1: Gap, gap2: Gap) -> str:
        """Determine relationship type between gaps."""
        if gap1.void_type == gap2.void_type:
            return "sibling"
        
        if gap1.void_type == VoidType.DEPENDENCY_GAP and gap2.void_type == VoidType.CAPABILITY_GAP:
            return "requires_capability"
        
        if gap1.void_type == VoidType.INFORMATION_GAP and gap2.void_type == VoidType.CAUSAL_GAP:
            return "informs_causality"
        
        return "related"

@dataclass_json
@dataclass
class GapCluster:
    """Cluster of related gaps."""
    id: str
    gaps: List[Gap]
    centroid: Dict[str, float]         # Center of cluster in gap space
    density: float                     # How dense the cluster is
    boundary: List[str]                # Boundary gaps
    core_gaps: List[Gap]               # Most central gaps
    
    # Cluster properties
    cluster_type: VoidType             # Dominant gap type
    strategic_importance: float = 0.0  # How important to address as cluster
    fill_sequence: List[str] = field(default_factory=list)  # Order to fill gaps
    
    def calculate_strategic_importance(self):
        """Calculate strategic importance of addressing this cluster."""
        # Based on gap criticalities and dependencies
        if not self.gaps:
            self.strategic_importance = 0.0
            return
        
        max_criticality = max(
            g.criticality.value if hasattr(g.criticality, 'value') else 0.5 
            for g in self.gaps
        )
        
        # Consider cluster density (dense clusters more important to address together)
        self.strategic_importance = max_criticality * self.density
