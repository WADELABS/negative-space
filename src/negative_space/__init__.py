"""
Negative Space: A framework for reasoning about unknowns and gaps.

This package provides tools for mapping the "void" between current and desired states,
enabling agentic systems to navigate complexity through exclusion and targeted inquiry.
"""

__version__ = "0.1.0"

# Core exports
from .agent import VoidAgent, VoidCollective
from .visualization import VoidVisualizer
from .core import GapCriticality, VoidType, Gap, VoidMap

__all__ = [
    "VoidAgent",
    "VoidCollective", 
    "VoidVisualizer",
    "GapCriticality",
    "VoidType",
    "Gap",
    "VoidMap",
]
