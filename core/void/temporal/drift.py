import networkx as nx
from typing import List, Dict, Any, Tuple
import logging

class VoidTopology:
    """
    Layer 5: Graph-based Void Topology.
    Uses NetworkX to identify 'Critical Path Gaps' that block the transition to the goal state.
    """
    
    def __init__(self):
        self.graph = nx.DiGraph()
        logging.info("Void Topology Engine (NetworkX) initialized.")

    def build_void_graph(self, gaps: List[str], dependencies: Dict[str, List[str]]):
        """Build a directed graph of gaps and their prerequisites."""
        for gap in gaps:
            self.graph.add_node(gap)
            for dep in dependencies.get(gap, []):
                self.graph.add_edge(dep, gap)

    def find_bottleneck_gaps(self) -> List[str]:
        """Identify gaps with high PageRank or Centrality."""
        if not self.graph.nodes: return []
        
        # Gaps that many other gaps depend on are bottlenecks
        centrality = nx.in_degree_centrality(self.graph)
        sorted_gaps = sorted(centrality.items(), key=lambda x: x[1], reverse=True)
        
        bottlenecks = [g for g, c in sorted_gaps if c > 0]
        logging.info(f"Identified {len(bottlenecks)} bottleneck gaps in topology.")
        return bottlenecks

class TemporalVoidDrift:
    """
    Layer 6: Temporal Void Drift.
    Tracks how gaps evolve (open or close) over a time series.
    """
    
    def __init__(self):
        self.history = []
        logging.info("Temporal Void Drift tracker initialized.")

    def record_snapshot(self, void_density: float, timestamp: str):
        self.history.append({"density": void_density, "time": timestamp})
        
    def calculate_drift_rate(self) -> float:
        """Calculate the rate of void closure (positive) or expansion (negative)."""
        if len(self.history) < 2: return 0.0
        
        d1 = self.history[0]['density']
        d2 = self.history[-1]['density']
        return d1 - d2 # Positive means void is shrinking
