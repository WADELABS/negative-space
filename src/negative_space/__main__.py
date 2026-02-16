"""
CLI entry point for Negative Space Framework.
Allows running: python -m negative_space
"""

import asyncio
import argparse
import json
from pathlib import Path
from negative_space import VoidAgent

async def async_main():
    """Async main function for void mapping."""
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
    try:
        point_a = json.loads(Path(args.current).read_text())
    except FileNotFoundError:
        print(f"❌ Error: Could not find current state file: {args.current}")
        return
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON in current state file: {args.current}")
        print(f"   {e}")
        return
    except Exception as e:
        print(f"❌ Error reading current state file: {e}")
        return
    
    try:
        point_b = json.loads(Path(args.goal).read_text())
    except FileNotFoundError:
        print(f"❌ Error: Could not find goal state file: {args.goal}")
        return
    except json.JSONDecodeError as e:
        print(f"❌ Error: Invalid JSON in goal state file: {args.goal}")
        print(f"   {e}")
        return
    except Exception as e:
        print(f"❌ Error reading goal state file: {e}")
        return
    
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
        try:
            Path(args.output).write_text(json.dumps(report, indent=2, default=str))
            print(f"\n💾 Report saved to: {args.output}")
        except PermissionError:
            print(f"\n❌ Error: Permission denied writing to: {args.output}")
        except Exception as e:
            print(f"\n❌ Error writing report: {e}")

def main():
    """Synchronous entry point for CLI."""
    asyncio.run(async_main())

if __name__ == "__main__":
    main()
