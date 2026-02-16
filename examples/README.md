# Examples Directory

This directory contains examples demonstrating various features of the Negative Space Framework.

## Available Examples

### 1. Featured Demo (featured_demo.py)
**Comprehensive demonstration of the framework's capabilities**

**Scenario:** Monolith to Microservices Migration

This example showcases:
- Complete void mapping workflow
- All 8 gap types (DEPENDENCY, INFORMATION, CONSTRAINT, CAPABILITY, CONCEPTUAL, CAUSAL, TEMPORAL, ETHICAL)
- Gap criticality analysis (BLOCKING, HIGH, MEDIUM, LOW)
- Strategic navigation planning
- JSON report generation
- Key metrics: void density, navigability, connectivity

**Run:**
```bash
python examples/featured_demo.py
# or
python -m negative_space.demo
```

**Expected Output:**
- Console: Comprehensive void analysis with metrics, critical findings, and recommendations
- File: `demo_output_report.json` (structured JSON report)

**Sample Metrics:**
- Total gaps: 3-30 (depends on scenario complexity)
- Void density: 0.0-1.0 (how much is missing)
- Navigability: 0.0-1.0 (ease of traversing gaps)
- Connectivity: 0.0-1.0 (inter-gap network density)

---

### 2. Basic Demo (demo.py)
**Introductory example with ML model development scenario**

**Scenario:** Building an ML model from raw data to production

This example demonstrates:
- Basic void mapping between Point A and Point B
- Context-aware gap discovery (dependencies, constraints, ethical concerns)
- VoidCollective for multi-agent consensus

**Run:**
```bash
python examples/demo.py
```

**Expected Output:**
- Total gaps identified
- Void density metric
- Top critical findings
- Strategic recommendations
- Collective mapping results

---

### 3. Quickstart (quickstart.py)
**Minimal working example for getting started quickly**

**Purpose:** Quick introduction to core concepts

**Run:**
```bash
python examples/quickstart.py
```

---

### 4. Portfolio Demo (portfolio_demo.py)
**Real-world application to project portfolio management**

**Scenario:** Portfolio resource allocation and risk assessment

**Run:**
```bash
python examples/portfolio_demo.py
```

---

## Installation

Before running examples, install the package:

```bash
# From repository root
pip install -e .

# Or with development dependencies
pip install -e ".[dev]"
```

## Understanding the Output

### Void Density
- **0.0**: Nothing missing (rare - usually means trivial transformation)
- **0.0-0.3**: Small void (manageable gaps)
- **0.3-0.6**: Moderate void (significant work required)
- **0.6-0.9**: Large void (major transformation)
- **0.9-1.0**: Massive void (reconsider goal feasibility)

### Gap Criticality Levels
- **BLOCKING**: Cannot proceed without filling this gap
- **HIGH**: Significantly impedes progress
- **MEDIUM**: Slows progress but has workarounds
- **LOW**: Minor impediment
- **UNKNOWN**: Impact unclear (needs investigation)

### Navigability
- **High (0.7-1.0)**: Clear paths exist, few bottlenecks
- **Medium (0.4-0.7)**: Some bottlenecks, multiple path options
- **Low (0.0-0.4)**: Many bottlenecks, limited path options

### Navigation Strategies
- **Gap Hopping**: Fill gaps sequentially by dependency order
- **Boundary Skirting**: Navigate around blocking gaps
- **Void Bridging**: Find shortest path through gap space
- **Constraint Circumvention**: Work around fundamental constraints

## Programmatic Usage

All examples follow this pattern:

```python
import asyncio
from negative_space import VoidAgent

async def main():
    # Define states
    point_a = {"current": "state"}
    point_b = {"desired": "state"}
    context = {"dependencies": {}, "constraints": {}}
    
    # Create agent
    agent = VoidAgent(name="MyAgent", rigor=0.8)
    
    # Map voids
    report = await agent.map_voids(point_a, point_b, context)
    
    # Analyze results
    print(f"Void density: {report['summary']['void_density']}")
    print(f"Total gaps: {report['summary']['total_gaps']}")
    
    # Access critical findings
    for finding in report['critical_findings']:
        print(f"- {finding['description']}")

asyncio.run(main())
```

## JSON Report Structure

Each void mapping generates a structured JSON report. See `demo_output_report.json` for a complete example.

Key sections:
- `summary`: High-level metrics
- `critical_findings`: Blocking and high-priority gaps
- `navigation_plan`: Recommended strategy and path
- `patterns`: Gap distribution and insights
- `recommendations`: Strategic advice

For complete schema documentation, see: [docs/VOID_REPORT_SCHEMA.md](../docs/VOID_REPORT_SCHEMA.md)

## Further Reading

- **Concepts & Terminology:** [docs/GLOSSARY.md](../docs/GLOSSARY.md)
- **JSON Schema:** [docs/VOID_REPORT_SCHEMA.md](../docs/VOID_REPORT_SCHEMA.md)
- **Main README:** [README.md](../README.md)
- **Framework Manifesto:** [manifesto/MANIFESTO.md](../manifesto/MANIFESTO.md)

## Contributing Examples

To add a new example:

1. Create a new `.py` file in this directory
2. Follow the pattern used in `featured_demo.py`
3. Include clear docstrings and comments
4. Add a section to this README
5. Test that it runs successfully

Example template:

```python
"""
Example Name: Brief Description

This example demonstrates:
- Feature 1
- Feature 2

Run with: python examples/your_example.py
"""

import asyncio
from negative_space import VoidAgent

async def main():
    # Your example code here
    pass

if __name__ == "__main__":
    asyncio.run(main())
```
