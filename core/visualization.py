"""
Void Visualization: Seeing what's missing.
"""

from typing import Dict, Any, List
import matplotlib.pyplot as plt
import networkx as nx
from collections import defaultdict
from .core import VoidMap, GapCriticality, VoidType

class VoidVisualizer:
    """Visualizes voids and gaps."""
    
    @staticmethod
    def visualize_void_map(void_map: VoidMap):
        """Visualize a void map."""
        if not void_map.gaps:
            print("No gaps to visualize")
            return
        
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))
        
        # 1. Gap type distribution
        ax1 = axes[0, 0]
        type_counts = defaultdict(int)
        for gap in void_map.gaps:
            type_counts[gap.void_type.name] += 1
        
        if type_counts:
            ax1.bar(type_counts.keys(), type_counts.values())
            ax1.set_title("Gap Type Distribution")
            ax1.set_ylabel("Count")
            ax1.tick_params(axis='x', rotation=45)
        
        # 2. Criticality distribution
        ax2 = axes[0, 1]
        crit_counts = defaultdict(int)
        for gap in void_map.gaps:
            crit_counts[gap.criticality.name] += 1
        
        if crit_counts:
            # Simple pie chart
            ax2.pie(crit_counts.values(), labels=crit_counts.keys(), autopct='%1.1f%%')
            ax2.set_title("Gap Criticality")
        
        # 3. Void network
        ax3 = axes[0, 2]
        if void_map.gap_network and len(void_map.gap_network.nodes) > 0:
            try:
                pos = nx.spring_layout(void_map.gap_network)
                nx.draw(void_map.gap_network, pos, ax=ax3, node_size=100, width=1, alpha=0.7)
                ax3.set_title("Gap Network")
            except Exception as e:
                ax3.text(0.5, 0.5, f"Network viz failed: {e}", ha='center', va='center')

        # 4. Fillability vs Criticality (Placeholder)
        ax4 = axes[1, 0]
        ax4.text(0.5, 0.5, "Fillability vs Criticality", ha='center', va='center')
        ax4.set_title("Fillability Analysis")

        # 5. Gap Size Distribution (Placeholder)
        ax5 = axes[1, 1]
        sizes = [g.size for g in void_map.gaps]
        if sizes:
            ax5.hist(sizes)
        ax5.set_title("Gap Sizes")

        # 6. Summary Text
        ax6 = axes[1, 2]
        ax6.axis('off')
        summary = f"Total Gaps: {len(void_map.gaps)}\nDensity: {void_map.void_density:.2f}"
        ax6.text(0.1, 0.5, summary, fontsize=12)

        plt.suptitle(f"Void Map: {void_map.id}")
        plt.tight_layout()
        plt.show()

    @staticmethod
    def visualize_void_navigation(navigation_plan: Dict[str, Any]):
        """Visualize void navigation plan."""
        if "path" not in navigation_plan or not navigation_plan["path"]:
            print("No navigation path to visualize")
            return
            
        print(f"Visualizing navigation plan: {navigation_plan.get('strategy', 'Unknown')}")
        # Simplification for non-interactive environments: just print summary
        for step in navigation_plan["path"]:
            print(f"- {step.get('action')}: {step.get('description')}")
