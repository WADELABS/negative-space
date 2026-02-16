"""
CLI entry point for Negative Space Framework.
Allows running: python -m negative_space
"""

import asyncio
import argparse
import json
from pathlib import Path
from negative_space import VoidAgent

async def main():
    parser = argparse.ArgumentParser(
        description="Negative Space Framework - Map voids between states"
    )
    parser.add_argument(
        "--current",
        type=str,
        required=True,
        help="Path to JSON file describing current state (Point A)"
    )
    parser.add_argument(
        "--goal",
        type=str,
        required=True,
        help="Path to JSON file describing goal state (Point B)"
    )
    parser.add_argument(
        "--rigor",
        type=float,
        default=0.8,
        help="Mapping rigor (0.0-1.0, default: 0.8)"
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Path to save void report JSON"
    )
    
    args = parser.parse_args()
    
    # Load states
    point_a = json.loads(Path(args.current).read_text())
    point_b = json.loads(Path(args.goal).read_text())
    
    # Map voids
    agent = VoidAgent(name="CLI-Agent", rigor=args.rigor)
    print(f"🔍 Mapping voids (rigor={args.rigor})...")
    
    report = await agent.map_voids(point_a, point_b)
    
    # Display results
    print(f"\n✅ Void Mapping Complete")
    print(f"   Total gaps: {report['summary']['total_gaps']}")
    print(f"   Void density: {report['summary']['void_density']:.3f}")
    
    if report['critical_findings']:
        print(f"\n⚠️  Critical Findings:")
        for finding in report['critical_findings'][:5]:
            print(f"   - {finding['description']}")
    
    # Save if requested
    if args.output:
        Path(args.output).write_text(json.dumps(report, indent=2, default=str))
        print(f"\n💾 Report saved to: {args.output}")

if __name__ == "__main__":
    asyncio.run(main())
