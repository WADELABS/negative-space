"""
Void Navigation Engine: Strategies for traversing the void.
"""

from typing import Dict, List, Any
import logging
from datetime import datetime
import networkx as nx
import numpy as np

from .core import VoidMap, Gap, VoidType

class VoidNavigationEngine:
    """
    Engine for navigating through the void (what's missing).
    Finds paths through gap space rather than solution space.
    """
    
    def __init__(self):
        self.navigation_strategies = {
            "gap_hopping": self._gap_hopping,
            "boundary_skirting": self._boundary_skirting,
            "void_bridging": self._void_bridging,
            "constraint_circumvention": self._constraint_circumvention
        }
        
        self.navigation_history: List[Dict[str, Any]] = []
        
    async def navigate_void(self, void_map: VoidMap,
                          strategy: str = "gap_hopping") -> Dict[str, Any]:
        """
        Navigate through the void to find path from A to B.
        """
        logging.info(f"Navigating void using strategy: {strategy}")
        
        if strategy not in self.navigation_strategies:
            logging.warning(f"Unknown strategy {strategy}, using gap_hopping")
            strategy = "gap_hopping"
        
        # Apply navigation strategy
        navigation_func = self.navigation_strategies[strategy]
        navigation_plan = await navigation_func(void_map)
        
        # Record navigation
        self.navigation_history.append({
            "void_map_id": void_map.id,
            "strategy": strategy,
            "timestamp": datetime.now(),
            "plan": navigation_plan.get("summary", "No summary")
        })
        
        return navigation_plan
    
    async def _gap_hopping(self, void_map: VoidMap) -> Dict[str, Any]:
        """
        Navigation by hopping across gaps.
        Identifies sequence of gaps to fill.
        """
        if not void_map.gaps:
            return {"strategy": "gap_hopping", "path": [], "summary": "No gaps to navigate"}
        
        # Build gap dependency graph
        dep_graph = nx.DiGraph()
        
        for gap in void_map.gaps:
            dep_graph.add_node(gap.id, gap=gap)
            for dep in gap.dependencies:
                if dep in [g.id for g in void_map.gaps]:
                    dep_graph.add_edge(dep, gap.id)
        
        # Find fillable gaps with no dependencies
        start_gaps = []
        for gap in void_map.gaps:
            if gap.fillable and dep_graph.in_degree(gap.id) == 0:
                start_gaps.append(gap)
        
        # Sort by priority
        start_gaps.sort(key=lambda g: void_map._gap_weight(g), reverse=True)
        
        # Create navigation path
        path = []
        filled_gaps = set()
        
        while start_gaps:
            current_gap = start_gaps.pop(0)
            
            if current_gap.id in filled_gaps:
                continue
            
            path.append({
                "gap_id": current_gap.id,
                "description": current_gap.description,
                "action": f"Fill {current_gap.void_type.name} gap",
                "estimated_cost": current_gap.fill_cost,
                "estimated_time": current_gap.fill_time
            })
            
            filled_gaps.add(current_gap.id)
            
            # Update dependent gaps
            for successor in dep_graph.successors(current_gap.id):
                # Check if all dependencies are filled
                predecessors = list(dep_graph.predecessors(successor))
                if all(pred in filled_gaps for pred in predecessors):
                    gap_obj = dep_graph.nodes[successor]["gap"]
                    start_gaps.append(gap_obj)
            
            # Re-sort
            start_gaps.sort(key=lambda g: void_map._gap_weight(g), reverse=True)
        
        return {
            "strategy": "gap_hopping",
            "path": path,
            "summary": f"Navigate by filling {len(path)} gaps in sequence",
            "total_estimated_cost": sum(p["estimated_cost"] for p in path),
            "total_estimated_time": sum(p["estimated_time"] for p in path)
        }
    
    async def _boundary_skirting(self, void_map: VoidMap) -> Dict[str, Any]:
        """
        Navigation by skirting around void boundaries.
        Finds paths that avoid the largest voids.
        """
        if not void_map.gap_network:
            return {"strategy": "boundary_skirting", "path": [], "summary": "No gap network"}
        
        # Identify core voids (highly connected gaps)
        centrality = nx.betweenness_centrality(void_map.gap_network)
        core_gaps = [node for node, cent in centrality.items() 
                    if cent > np.median(list(centrality.values()))]
        
        # Find peripheral gaps (low centrality)
        peripheral_gaps = [node for node in void_map.gap_network.nodes 
                          if node not in core_gaps]
        
        # Create path through peripheral gaps
        path = []
        for gap_id in peripheral_gaps[:5]:  # Limit to 5 peripheral gaps
            gap = next((g for g in void_map.gaps if g.id == gap_id), None)
            if gap and gap.fillable:
                path.append({
                    "gap_id": gap_id,
                    "description": gap.description,
                    "action": f"Address peripheral {gap.void_type.name} gap",
                    "rationale": "Lower centrality makes this easier to address"
                })
        
        return {
            "strategy": "boundary_skirting",
            "path": path,
            "summary": f"Navigate by addressing {len(path)} peripheral gaps first",
            "core_gaps_avoided": len(core_gaps)
        }
    
    async def _void_bridging(self, void_map: VoidMap) -> Dict[str, Any]:
        """
        Navigation by bridging across voids.
        Creates bridges between what exists and what's missing.
        """
        # Find bridgeable gaps (gaps with clear boundaries)
        bridgeable_gaps = []
        for gap in void_map.gaps:
            if gap.boundary_conditions and gap.fillable:
                bridgeable_gaps.append(gap)
        
        # Sort by clarity (clearer boundaries are easier to bridge)
        bridgeable_gaps.sort(key=lambda g: g.clarity, reverse=True)
        
        # Create bridging path
        path = []
        for gap in bridgeable_gaps[:3]:  # Bridge 3 clearest gaps
            path.append({
                "gap_id": gap.id,
                "description": gap.description,
                "action": f"Bridge {gap.void_type.name} gap",
                "bridge_type": self._suggest_bridge_type(gap),
                "boundary_conditions": gap.boundary_conditions
            })
        
        return {
            "strategy": "void_bridging",
            "path": path,
            "summary": f"Navigate by bridging {len(path)} clear-boundary gaps",
            "bridging_technique": "Identify and connect boundary conditions"
        }
    
    def _suggest_bridge_type(self, gap: Gap) -> str:
        """Suggest type of bridge for a gap."""
        if gap.void_type == VoidType.INFORMATION_GAP:
            return "information_pipeline"
        elif gap.void_type == VoidType.DEPENDENCY_GAP:
            return "dependency_interface"
        elif gap.void_type == VoidType.CAPABILITY_GAP:
            return "capability_proxy"
        elif gap.void_type == VoidType.CONCEPTUAL_GAP:
            return "conceptual_metaphor"
        else:
            return "general_bridge"
    
    async def _constraint_circumvention(self, void_map: VoidMap) -> Dict[str, Any]:
        """
        Navigation by circumventing constraints.
        Finds alternative paths that avoid blocked areas.
        """
        # Identify constraint gaps
        constraint_gaps = [g for g in void_map.gaps 
                          if g.void_type == VoidType.CONSTRAINT_GAP]
        
        if not constraint_gaps:
            return {"strategy": "constraint_circumvention", "path": [], 
                   "summary": "No constraint gaps to circumvent"}
        
        # Find circumvention strategies
        path = []
        for gap in constraint_gaps:
            circumventions = self._suggest_circumventions(gap)
            
            for circ in circumventions[:2]:  # Top 2 circumventions per gap
                path.append({
                    "gap_id": gap.id,
                    "description": gap.description,
                    "action": f"Circumvent {gap.void_type.name} constraint",
                    "circumvention": circ,
                    "risk": "moderate"  # Circumvention always has risk
                })
        
        return {
            "strategy": "constraint_circumvention",
            "path": path,
            "summary": f"Navigate by circumventing {len(constraint_gaps)} constraints",
            "warning": "Circumvention may introduce new risks"
        }
    
    def _suggest_circumventions(self, gap: Gap) -> List[str]:
        """Suggest ways to circumvent a constraint gap."""
        circumventions = []
        
        if "resource" in gap.description.lower():
            circumventions.extend(["resource_sharing", "efficiency_improvement", 
                                 "alternative_resource", "phased_approach"])
        
        elif "time" in gap.description.lower():
            circumventions.extend(["parallel_processing", "critical_path_optimization",
                                 "milestone_revision", "time_extension_request"])
        
        elif "legal" in gap.description.lower() or "ethical" in gap.description.lower():
            circumventions.extend(["alternative_approach", "stakeholder_negotiation",
                                 "regulatory_consultation", "compliance_demonstration"])
        
        else:
            circumventions.extend(["workaround_development", "requirement_relaxation",
                                 "alternative_solution", "problem_redefinition"])
        
        return circumventions
