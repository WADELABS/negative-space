# Negative Space Terminology Guide

## Core Concepts

### Negative Space Reasoning
An epistemology focusing on what is **absent** rather than what is present. Instead of interpolating between known states, we map the voids, gaps, and missing elements between current reality (Point A) and desired objectives (Point B).

### Void Mapping
The process of systematically identifying, classifying, and analyzing gaps between two states. Unlike traditional gap analysis, void mapping treats absence as a first-class citizen with measurable properties.

### Point A & Point B
- **Point A**: Current state/reality (what exists now)
- **Point B**: Target state/objective (what we want to exist)
- **The Void**: Everything missing between A and B

## Gap Types (VoidType)

### DEPENDENCY_GAP
**Missing components or dependencies required for functionality.**
- Example: Library not installed, service not deployed
- Manifestation: Import errors, connection failures

### INFORMATION_GAP
**Missing knowledge, data, or documentation.**
- Example: Unknown API requirements, undocumented assumptions
- Manifestation: Cannot proceed without research

### CONSTRAINT_GAP
**Missing permissions, access, or abilities.**
- Example: No database credentials, insufficient IAM roles
- Manifestation: Access denied errors

### CAPABILITY_GAP
**Missing skills, tools, or technical capacity.**
- Example: Team lacks Kubernetes expertise, no CI/CD pipeline
- Manifestation: Cannot execute required tasks

### CONCEPTUAL_GAP
**Missing mental models or frameworks.**
- Example: Unclear system architecture, undefined success criteria
- Manifestation: Confusion about approach

### CAUSAL_GAP
**Missing understanding of cause-effect relationships.**
- Example: Unknown why system fails under load
- Manifestation: Cannot debug or prevent issues

### TEMPORAL_GAP
**Missing time-based understanding.**
- Example: Unknown deployment sequencing, unclear timeline
- Manifestation: Race conditions, ordering issues

### ETHICAL_GAP
**Missing ethical considerations or safeguards.**
- Example: No privacy review, unaddressed bias concerns
- Manifestation: Compliance violations, harm

## Metrics

### Void Density (0-1)
**How much is missing** relative to what's needed. Weighted by gap criticality and certainty.
- 0.0 = Nothing missing (rare)
- 0.5 = Moderate void
- 1.0 = Almost everything missing

### Gap Criticality
**Impact of a gap** on reaching Point B.
- **BLOCKING**: Cannot proceed without filling
- **HIGH**: Significantly impedes progress
- **MEDIUM**: Slows progress
- **LOW**: Minor impediment
- **UNKNOWN**: Impact unclear

### Navigability (0-1)
**How easily you can traverse the gap space.** High navigability means clear paths exist; low navigability means many bottlenecks.

### Fillability
**Whether a gap can be closed** and at what cost/time. Some voids are:
- **Fillable**: Can be addressed directly
- **Unfillable**: Constraint is fundamental
- **Emergent**: Gap arises from system dynamics

## Comparison to Traditional Approaches

| Traditional Gap Analysis | Negative Space Reasoning |
| :--- | :--- |
| Focus on known gaps | **Discover unknown gaps** |
| Linear path planning | **Map void topology** |
| Single-dimension | **Multi-dimensional void characterization** |
| "What do we need?" | **"What's missing and why?"** |
| Solution-oriented | **Void-oriented (solutions later)** |

## Navigation Strategies

### Gap Hopping
Fill gaps sequentially based on dependency order.

### Boundary Skirting
Navigate around blocking gaps when direct paths are infeasible.

### Void Bridging
Find shortest path through gap space, minimizing total void traversal.

### Constraint Circumvention
Work around fundamental constraints by redefining Point B or finding alternative paths.

## For Practitioners

If you're building software and want to apply negative space reasoning:

1. **Define Point A** (current system state)
2. **Define Point B** (target architecture/outcome)
3. **Map the void** using `VoidAgent.map_voids(a, b)`
4. **Inspect gaps** by type and criticality
5. **Navigate** using recommended strategies
6. **Fill gaps** in dependency order

## For Researchers

This framework operationalizes absence-based epistemology for AI systems. Key research questions:
- Can we formalize the "shape" of a void?
- How do emergent voids arise from system interactions?
- What is the optimal navigation strategy for different void topologies?
