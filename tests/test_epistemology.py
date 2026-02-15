"""
tests/test_epistemology.py
Verification of Epistemological Uncertainty (EU) and Ontological Mapping.
"""

import unittest
from src.ontology import SemanticMapper
from src.doubt import DoubtCalculator

class TestEpistemology(unittest.TestCase):
    def setUp(self):
        self.mapper = SemanticMapper()
        self.doubt = DoubtCalculator()

    def test_semantic_density(self):
        """Test that semantic density is calculated correctly."""
        claim = "The cat sat on the mat."
        result = self.mapper.analyze_claim(claim)
        self.assertGreater(result["semantic_density"], 0.5)

    def test_epistemological_uncertainty_limit(self):
        """Test EU score for absolute uncertainty."""
        eu = self.doubt.calculate_eu([], 1)
        self.assertEqual(eu, 1.0)

    def test_integrity_trigger(self):
        """Test that unstable responses trigger the Scientific Method."""
        response = "This is a very long response that has no citations and likely contains some hallucinations."
        result = self.doubt.evaluate_response_integrity(response, 0)
        self.assertEqual(result["action"], "TRIGGER_SCIENTIFIC_METHOD")

if __name__ == "__main__":
    unittest.main()
