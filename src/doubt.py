"""
src/doubt.py
Doubt Heuristics: Quantifying the Abyss.
"""

import math
from typing import Dict, List

class DoubtCalculator:
    """Calculates Epistemological Uncertainty (EU) scores."""
    
    def calculate_eu(self, data_points: List[str], contradictions: int) -> float:
        """
        EU = log(Contradictions + 1) / sqrt(DataPoints + 1)
        High EU suggests high probability of hallucination or inference error.
        """
        if not data_points:
            return 1.0 # Absolute Uncertainty
            
        n = len(data_points)
        c = contradictions
        
        eu = math.log(c + 1) / math.sqrt(n + 1)
        return min(round(eu, 4), 1.0)

    def evaluate_response_integrity(self, response: str, source_count: int) -> Dict:
        """
        Heuristic for real-time inference monitoring.
        """
        # Phase 1: Mock contradiction detection
        assumed_contradictions = 1 if len(response) > 50 and source_count < 2 else 0
        
        eu_score = self.calculate_eu([response], assumed_contradictions)
        
        return {
            "eu_score": eu_score,
            "integrity_level": "STABLE" if eu_score < 0.3 else "UNSTABLE",
            "action": "PROCEED" if eu_score < 0.5 else "TRIGGER_SCIENTIFIC_METHOD"
        }
