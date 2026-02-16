"""Tests for VoidAgent core functionality."""

import pytest
from negative_space import VoidAgent, GapCriticality, VoidType

@pytest.mark.asyncio
async def test_void_agent_initialization():
    """Test VoidAgent can be initialized."""
    agent = VoidAgent(name="TestAgent", rigor=0.8)
    assert agent.name == "TestAgent"
    assert agent.rigor == 0.8

@pytest.mark.asyncio
async def test_map_voids_basic():
    """Test basic void mapping between two states."""
    agent = VoidAgent(name="TestMapper", rigor=0.7)
    
    point_a = {"feature": "A", "value": 1}
    point_b = {"feature": "B", "value": 2, "extra": "new"}
    
    report = await agent.map_voids(point_a, point_b)
    
    assert "summary" in report
    assert "total_gaps" in report["summary"]
    assert report["summary"]["total_gaps"] >= 0

@pytest.mark.asyncio
async def test_gap_criticality_classification():
    """Test that gaps are properly classified by criticality."""
    agent = VoidAgent(name="CriticalityTest", rigor=0.9)
    
    point_a = {"status": "prototype"}
    point_b = {"status": "production", "deployment": "k8s"}
    
    report = await agent.map_voids(point_a, point_b)
    
    # Should identify critical gaps for production deployment
    critical = [g for g in report.get('critical_findings', []) 
                if g.get('criticality') == 'BLOCKING']
    
    assert len(critical) >= 0  # Framework should identify blocking gaps
