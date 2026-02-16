# Negative Space Framework - Examples

This directory contains demonstration scripts showcasing the Negative Space Framework's capabilities.

## 📋 Available Examples

### 1. Featured Demo (Recommended Starting Point)
**File:** `featured_demo.py`

A comprehensive demonstration showing how to map the void between a monolithic application and a microservices architecture. This is the best example to understand the framework's full capabilities.

**Run:**
```bash
python examples/featured_demo.py
# or
python -m negative_space.demo  # if the module entry point is configured
```

**What it demonstrates:**
- ✅ Complete void mapping between two complex states
- ✅ Gap characterization (8 void types)
- ✅ Criticality analysis (BLOCKING/HIGH/MEDIUM/LOW)
- ✅ Navigability and connectivity metrics
- ✅ Strategic navigation planning
- ✅ Gap clustering
- ✅ JSON report generation
- ✅ Multi-agent collective consensus

**Expected Output:**
```
======================================================================
NEGATIVE SPACE FRAMEWORK - FEATURED DEMO
Scenario: Monolith to Microservices Migration
======================================================================

📈 KEY METRICS
----------------------------------------------------------------------
  Total Gaps Identified:    4
  Void Density:            0.211 (0=nothing missing, 1=everything missing)
  Navigability:            1.000 (0=impassable, 1=clear path)
  Connectivity:            1.000 (gap interdependence)
  Blocking Gaps:           0
  Fillable Gaps:           0
...
```

**Generated Files:**
- `demo_output_report.json` - Full void analysis report
- `demo_console_report.json` - Simplified console-friendly version

---

### 2. Basic Demo
**File:** `demo.py`

A simpler example showing fundamental void mapping between a machine learning project's current and desired states.

**Run:**
```bash
python examples/demo.py
```

**What it demonstrates:**
- Basic void mapping workflow
- Simple state definitions
- Critical findings identification
- Recommendations generation
- Collective mapping example

**Expected Output:**
```
============================================================
VOID MAPPER: NEGATIVE SPACE REASONING FRAMEWORK
============================================================

Void Analysis Complete:
  Total gaps identified: 2
  Void density: 0.180

Recommendations:
  - Proceed cautiously - while void is small, remaining gaps may be critical
```

---

### 3. Portfolio Analysis Demo
**File:** `portfolio_demo.py`

Demonstrates void mapping for an investment portfolio analysis scenario.

**Run:**
```bash
python examples/portfolio_demo.py
```

---

### 4. Quick Start
**File:** `quickstart.py`

Minimal example for getting started quickly with the framework.

**Run:**
```bash
python examples/quickstart.py
```

---

## 🚀 Installation

Before running examples, ensure the package is installed:

```bash
# Install from source (development mode)
pip install -e .

# Install with dev dependencies
pip install -e ".[dev]"
```

## 📊 Understanding Output

### Void Density (0-1)
- **0.0**: Nothing is missing (rare - means states are identical)
- **0.1-0.3**: Small void (incremental changes needed)
- **0.3-0.6**: Moderate void (significant effort required)
- **0.6-1.0**: Large void (major transformation needed)

### Gap Criticality
- **BLOCKING**: Cannot proceed without addressing
- **HIGH**: Significantly impedes progress
- **MEDIUM**: Slows progress moderately
- **LOW**: Minor impediment
- **UNKNOWN**: Impact unclear

### Navigability (0-1)
- **High (0.7-1.0)**: Clear paths exist through the gap space
- **Medium (0.4-0.7)**: Some bottlenecks present
- **Low (0-0.4)**: Many blocking constraints

## 🧪 Customizing Examples

You can modify any example to explore different scenarios:

```python
from negative_space import VoidAgent

# Define your current state
point_a = {
    "your_current_attribute": "value",
    "another_attribute": 123
}

# Define your desired state
point_b = {
    "your_desired_attribute": "new_value",
    "another_attribute": 456,
    "new_feature": True
}

# Map the void
agent = VoidAgent(name="CustomMapper", rigor=0.8)
report = await agent.map_voids(point_a, point_b)

# Access results
print(f"Total gaps: {report['summary']['total_gaps']}")
print(f"Void density: {report['summary']['void_density']:.3f}")
```

## 📚 Further Reading

- **Main README**: `../README.md` - Overview and installation
- **Glossary**: `../docs/GLOSSARY.md` - Terminology and concepts
- **JSON Schema**: `../docs/VOID_REPORT_SCHEMA.md` - Report structure for tool integration
- **Manifesto**: `../manifesto/MANIFESTO.md` - Philosophical foundation

## 🐛 Troubleshooting

### Import Errors
If you get `ModuleNotFoundError: No module named 'negative_space'`:
```bash
pip install -e .
```

### Async Runtime Errors
The examples use `asyncio.run()`. If you're running in a Jupyter notebook:
```python
# Instead of asyncio.run(main_example())
await main_example()
```

## 💡 Next Steps

1. Run `featured_demo.py` to see full capabilities
2. Review the generated `demo_output_report.json`
3. Read `docs/GLOSSARY.md` to understand terminology
4. Explore `docs/VOID_REPORT_SCHEMA.md` for JSON integration
5. Build your own void mapping scenario!
