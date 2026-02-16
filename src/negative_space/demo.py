"""
Demo module for Negative Space Framework.
Can be run with: python -m negative_space.demo

This is a wrapper that provides access to the featured demo.
When running from an installed package, it will print instructions instead.
"""

import sys
import os
from pathlib import Path

def main():
    """Run the featured demo or provide instructions."""
    
    # Try to find the examples directory
    # Check if we're in development mode
    package_dir = Path(__file__).parent
    repo_root = package_dir.parent.parent
    examples_dir = repo_root / "examples"
    
    if examples_dir.exists() and (examples_dir / "featured_demo.py").exists():
        # We're in development mode, run the demo
        sys.path.insert(0, str(examples_dir))
        try:
            from featured_demo import main as demo_main
            demo_main()
        except ImportError as e:
            print(f"Error: Could not import featured demo: {e}")
            sys.exit(1)
    else:
        # Package is installed, provide instructions
        print("="*80)
        print(" NEGATIVE SPACE FRAMEWORK - DEMO")
        print("="*80)
        print()
        print("To run the featured demo, please download the examples from:")
        print("https://github.com/WADELABS/negative-space/tree/main/examples")
        print()
        print("Then run:")
        print("  python featured_demo.py")
        print()
        print("Alternatively, you can use the CLI to analyze your own states:")
        print("  python -m negative_space --current state_a.json --goal state_b.json")
        print()
        print("For more information, see:")
        print("  - Documentation: https://github.com/WADELABS/negative-space")
        print("  - Glossary: docs/GLOSSARY.md")
        print("  - Schema: docs/VOID_REPORT_SCHEMA.md")
        print()

if __name__ == "__main__":
    main()
