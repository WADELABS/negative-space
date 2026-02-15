"""
src/ontology.py
Ontolegical Mapping: Defining the boundaries of the known.
"""

from typing import Dict, List, Set

class KnowledgeGraph:
    """Represents a sparse semantic map of a domain."""
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_fact(self, source: str, target: str, relationship: str):
        self.nodes.add(source)
        self.nodes.add(target)
        if source not in self.edges:
            self.edges[source] = []
        self.edges[source].append({"target": target, "rel": relationship})

    def get_inference_gaps(self, target_node: str) -> List[str]:
        """Identifies nodes that are poorly connected/defined."""
        if target_node not in self.nodes:
            return ["Node not found in current ontology."]
        
        connections = self.edges.get(target_node, [])
        if len(connections) < 2:
            return [f"High Inference Gap: '{target_node}' is semantically isolated."]
        return []

class SemanticMapper:
    """Orchestrates the mapping of negative space."""
    def __init__(self):
        self.graph = KnowledgeGraph()

    def analyze_claim(self, claim: str) -> Dict:
        """Heuristic for identifying the 'Dark Matter' in a claim."""
        # Phase 1: Simple keyword density/isolation check
        words = claim.split()
        isolated_terms = [w for w in words if len(w) > 3] # Mock isolated term detection
        
        return {
            "claim": claim,
            "semantic_density": round(len(set(words)) / len(words), 4) if words else 0,
            "potential_gaps": isolated_terms,
            "epistemological_status": "EXPLORATIVE"
        }
