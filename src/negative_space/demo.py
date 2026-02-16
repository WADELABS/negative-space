"""
Demo module for Negative Space Framework.
Can be run with: python -m negative_space.demo
"""

import sys
from pathlib import Path

# Import and run the featured demo
sys.path.insert(0, str(Path(__file__).parent.parent.parent / 'examples'))

try:
    from featured_demo import main
    main()
except ImportError:
    print("Error: Could not import featured demo.")
    print("Please ensure you are running from the package root directory.")
    sys.exit(1)
