"""Pytest configuration and fixtures."""

import pytest
from negative_space import VoidAgent

@pytest.fixture
def simple_agent():
    """Fixture providing a basic VoidAgent."""
    return VoidAgent(name="TestAgent", rigor=0.7)

@pytest.fixture
def sample_states():
    """Fixture providing sample point A and point B."""
    point_a = {
        "environment": "development",
        "features": ["basic"],
        "users": 10
    }
    
    point_b = {
        "environment": "production",
        "features": ["basic", "advanced", "enterprise"],
        "users": 10000,
        "scaling": "auto",
        "monitoring": "full"
    }
    
    return point_a, point_b
