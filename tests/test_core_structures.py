"""Tests for core data structures."""

import pytest
from negative_space import Gap, VoidType, GapCriticality, GapCertainty

def test_gap_creation():
    """Test Gap dataclass creation."""
    gap = Gap(
        id="test-gap-1",
        description="Missing authentication layer",
        void_type=VoidType.DEPENDENCY_GAP,
        domains=["security"],
        evidence=[{"type": "analysis", "finding": "no auth found"}],
        manifestations=["unauthorized access possible"],
        criticality=GapCriticality.BLOCKING,
        certainty=GapCertainty.DEFINITE
    )
    
    assert gap.id == "test-gap-1"
    assert gap.void_type == VoidType.DEPENDENCY_GAP
    assert gap.criticality == GapCriticality.BLOCKING

def test_gap_negative_shape():
    """Test negative shape calculation."""
    gap = Gap(
        id="shape-test",
        description="Test gap",
        void_type=VoidType.INFORMATION_GAP,
        domains=["data"],
        evidence=[],
        manifestations=[],
        criticality=GapCriticality.MEDIUM,
        certainty=GapCertainty.HYPOTHESIZED,
        dependencies=["gap-1", "gap-2"]
    )
    
    gap.calculate_negative_shape()
    
    assert "connectivity" in gap.negative_shape
    assert gap.negative_shape["connectivity"] == 2
