"""
Quickstart: Minimal Void Mapping Demo
Run this after installing: pip install -e .
"""

import asyncio
from negative_space import VoidAgent, GapCriticality

async def quickstart():
    # Define current state and goal
    current = {"infrastructure": "local", "security": "basic"}
    goal = {"infrastructure": "kubernetes", "security": "zero_trust"}
    
    # Map the voids
    agent = VoidAgent(name="QuickMapper", rigor=0.8)
    report = await agent.map_voids(current, goal)
    
    print(f"Found {report['summary']['total_gaps']} gaps")
    print(f"Void density: {report['summary']['void_density']:.2f}")
    
    for gap in report['critical_findings'][:3]:
        print(f"  ⚠️  {gap['description']}")

if __name__ == "__main__":
    asyncio.run(quickstart())
