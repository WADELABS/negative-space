"""
Void Clustering: Grouping gaps to reveal patterns.
"""

from typing import List, Dict, Any
import logging
import hashlib
import numpy as np
import networkx as nx
from collections import defaultdict

from .core import VoidMap, Gap, GapCluster, VoidType, GapCriticality, GapCertainty

class VoidClusterer:
    """
    Clusters gaps to reveal patterns in what's missing.
    Groups related voids to show structural emptiness.
    """
    
    def __init__(self, n_clusters: int = 5):
        self.n_clusters = n_clusters
        self.clustering_methods = {
            "semantic": self._semantic_clustering,
            "structural": self._structural_clustering,
            "strategic": self._strategic_clustering
        }
    
    async def cluster_gaps(self, void_map: VoidMap,
                          method: str = "semantic") -> List[GapCluster]:
        """
        Cluster gaps to reveal void structure.
        """
        if not void_map.gaps:
            return []
        
        if method not in self.clustering_methods:
            logging.warning(f"Unknown clustering method {method}, using semantic")
            method = "semantic"
        
        clustering_func = self.clustering_methods[method]
        clusters = await clustering_func(void_map)
        
        # Post-process clusters
        for cluster in clusters:
            cluster.calculate_strategic_importance()
        
        logging.info(f"Clustered {len(void_map.gaps)} gaps into {len(clusters)} clusters")
        
        return clusters
    
    async def _semantic_clustering(self, void_map: VoidMap) -> List[GapCluster]:
        """Cluster gaps based on semantic similarity."""
        # Extract gap features
        gap_features = []
        gap_objects = []
        
        for gap in void_map.gaps:
            features = self._extract_semantic_features(gap)
            gap_features.append(features)
            gap_objects.append(gap)
        
        if not gap_features:
            return []
        
        # Simple clustering based on feature similarity
        clusters = []
        used_gaps = set()
        
        for i, gap1 in enumerate(gap_objects):
            if gap1.id in used_gaps:
                continue
            
            # Start new cluster
            cluster_gaps = [gap1]
            used_gaps.add(gap1.id)
            
            # Find similar gaps
            for j, gap2 in enumerate(gap_objects[i+1:], i+1):
                if gap2.id in used_gaps:
                    continue
                
                similarity = self._gap_similarity(gap1, gap2)
                if similarity > 0.6:  # Similarity threshold
                    cluster_gaps.append(gap2)
                    used_gaps.add(gap2.id)
            
            if cluster_gaps:
                cluster = self._create_cluster(cluster_gaps, "semantic")
                clusters.append(cluster)
        
        # Limit to n_clusters
        clusters.sort(key=lambda c: len(c.gaps), reverse=True)
        return clusters[:self.n_clusters]
    
    async def _structural_clustering(self, void_map: VoidMap) -> List[GapCluster]:
        """Cluster gaps based on structural position in gap network."""
        if not void_map.gap_network:
            return []
        
        # Use network community detection
        try:
            communities = list(nx.community.greedy_modularity_communities(void_map.gap_network))
            
            clusters = []
            for i, community in enumerate(communities[:self.n_clusters]):
                community_gaps = []
                for gap_id in community:
                    gap = next((g for g in void_map.gaps if g.id == gap_id), None)
                    if gap:
                        community_gaps.append(gap)
                
                if community_gaps:
                    cluster = self._create_cluster(community_gaps, "structural")
                    clusters.append(cluster)
            
            return clusters
            
        except Exception as e:
            logging.error(f"Structural clustering failed: {e}")
            return await self._semantic_clustering(void_map)
    
    async def _strategic_clustering(self, void_map: VoidMap) -> List[GapCluster]:
        """Cluster gaps based on strategic importance and fillability."""
        # Group by void type and criticality
        type_groups = defaultdict(list)
        
        for gap in void_map.gaps:
            key = f"{gap.void_type.name}_{gap.criticality.name}"
            type_groups[key].append(gap)
        
        clusters = []
        for key, gaps in type_groups.items():
            if gaps:
                cluster = self._create_cluster(gaps, "strategic")
                clusters.append(cluster)
        
        # Sort by strategic importance
        clusters.sort(key=lambda c: c.strategic_importance, reverse=True)
        return clusters[:self.n_clusters]
    
    def _extract_semantic_features(self, gap: Gap) -> Dict[str, float]:
        """Extract semantic features from a gap."""
        features = {
            "type": list(VoidType).index(gap.void_type) / len(VoidType),
            "criticality": self._criticality_to_float(gap.criticality),
            "certainty": self._certainty_to_float(gap.certainty),
            "size": gap.size,
            "clarity": gap.clarity,
            "fillable": 1.0 if gap.fillable else 0.0
        }
        
        # Add domain features
        for domain in ["financial", "temporal", "capability", "information"]:
            features[f"domain_{domain}"] = 1.0 if domain in gap.domains else 0.0
        
        return features
    
    def _criticality_to_float(self, criticality: GapCriticality) -> float:
        """Convert criticality to float."""
        mapping = {
            GapCriticality.BLOCKING: 1.0,
            GapCriticality.HIGH: 0.75,
            GapCriticality.MEDIUM: 0.5,
            GapCriticality.LOW: 0.25,
            GapCriticality.UNKNOWN: 0.5
        }
        return mapping.get(criticality, 0.5)
    
    def _certainty_to_float(self, certainty: GapCertainty) -> float:
        """Convert certainty to float."""
        mapping = {
            GapCertainty.DEFINITE: 1.0,
            GapCertainty.HYPOTHESIZED: 0.7,
            GapCertainty.SPECULATIVE: 0.3,
            GapCertainty.EMERGENT: 0.5
        }
        return mapping.get(certainty, 0.5)
    
    def _gap_similarity(self, gap1: Gap, gap2: Gap) -> float:
        """Calculate similarity between two gaps."""
        # Type similarity
        type_sim = 1.0 if gap1.void_type == gap2.void_type else 0.3
        
        # Domain overlap
        domains1 = set(gap1.domains)
        domains2 = set(gap2.domains)
        domain_sim = len(domains1 & domains2) / len(domains1 | domains2) if domains1 or domains2 else 0.0
        
        # Description similarity (simple word overlap)
        words1 = set(gap1.description.lower().split())
        words2 = set(gap2.description.lower().split())
        word_sim = len(words1 & words2) / len(words1 | words2) if words1 and words2 else 0.0
        
        return (type_sim * 0.4 + domain_sim * 0.3 + word_sim * 0.3)
    
    def _create_cluster(self, gaps: List[Gap], cluster_type: str) -> GapCluster:
        """Create a gap cluster from a list of gaps."""
        cluster_id = f"cluster_{cluster_type}_{hashlib.sha256(str([g.id for g in gaps]).encode()).hexdigest()[:8]}"
        
        # Calculate centroid (average features)
        if gaps:
            features_list = [self._extract_semantic_features(g) for g in gaps]
            centroid = {}
            for key in features_list[0].keys():
                values = [f[key] for f in features_list]
                centroid[key] = np.mean(values)
        else:
            centroid = {}
        
        # Determine dominant gap type
        type_counts = defaultdict(int)
        for gap in gaps:
            type_counts[gap.void_type] += 1
        
        dominant_type = max(type_counts.items(), key=lambda x: x[1])[0] if type_counts else VoidType.INFORMATION_GAP
        
        # Find boundary gaps (gaps with unique features)
        boundary_gaps = []
        if len(gaps) > 1:
            # Simple boundary detection: gaps most different from centroid
            gap_differences = []
            for gap in gaps:
                features = self._extract_semantic_features(gap)
                diff = sum(abs(features[k] - centroid[k]) for k in features.keys())
                gap_differences.append((gap, diff))
            
            gap_differences.sort(key=lambda x: x[1], reverse=True)
            boundary_gaps = [g.id for g, _ in gap_differences[:min(3, len(gaps))]]
        
        # Find core gaps (most representative)
        core_gaps = []
        if len(gaps) > 1:
            gap_differences.sort(key=lambda x: x[1])  # Sort by similarity to centroid
            core_gaps = [g for g, _ in gap_differences[:min(3, len(gaps))]]
        
        # Calculate density
        density = len(gaps) / 10  # Normalize
        
        return GapCluster(
            id=cluster_id,
            gaps=gaps,
            centroid=centroid,
            density=density,
            boundary=boundary_gaps,
            core_gaps=core_gaps,
            cluster_type=dominant_type
        )
