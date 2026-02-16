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
NEGATIVE SPACE FRAMEWORK - FEATURED DEMO
Scenario: Monolith to Microservices Migration

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

**What it demonstrates:**
- Basic void mapping workflow
- Simple state definitions
- Critical findings identification
- Recommendations generation
- Collective mapping example

**Expected Output:**
```
