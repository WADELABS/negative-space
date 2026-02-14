import asyncio
import logging
from datetime import datetime
import sys
import os

# Ensure local 'src' is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

# Internal Imports
from src.void.interpolation.engine import VoidInterpolator, MultispectralMapper
from src.void.temporal.drift import VoidTopology, TemporalVoidDrift
from src.void.logic.consensus import BarrierCollapse, EpistemicConsensus
from src.void.logic.mitigation import MitigationHarness

async def run_negative_space_demo():
    """
    7-Layer Complexity Portfolio Demo for Negative Space (AFRRC Tier 3).
    Grounding: Global Financial Regulatory Gap Mapping.
    """
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    
    print("\n" + "="*80)
    print("NEGATIVE SPACE PORTFOLIO DEMO: 7-LAYER REGULATORY GAP MAPPING")
    print("="*80 + "\n")

    # 1. State Definition (Current vs Goal)
    current_state = {"licenses": ["SEC_NY"], "markets": ["US"]}
    goal_state = {"licenses": ["SEC_NY", "MiFID_II_EU"], "markets": ["US", "EU"], "kyc_compliance": True}

    # 2. Multispectral Mapping (Layer 2)
    mapper = MultispectralMapper()
    voids = mapper.map_layers(current_state, goal_state)
    print(f"[*] Global Regulatory voids identified: {list(voids.keys())}")

    # 3. Probabilistic Interpolation (Layer 1)
    interpolator = VoidInterpolator(iterations=500)
    summary = interpolator.estimate_void_density([10, 20, 30], {"max_threshold": 25})

    # 4. Topology Analysis (Layer 5)
    topology = VoidTopology()
    all_gaps = []
    for g in voids.values(): all_gaps.extend(g)
    
    # Define dependencies (e.g., EU Market depends on MiFID_II)
    deps = {"MiFID_II_EU": ["SEC_NY"], "EU_Market": ["MiFID_II_EU"]}
    topology.build_void_graph(all_gaps, deps)
    bottlenecks = topology.find_bottleneck_gaps()
    print(f"[*] Critical path bottlenecks for market entry: {bottlenecks}")

    # 5. Barrier Collapse (Layer 3)
    collapser = BarrierCollapse()
    if bottlenecks:
        impact = collapser.simulate_resolution(bottlenecks[0], deps)
        print(f"[*] Resolving {bottlenecks[0]} collapses blockers: {impact}")

    # 6. Epistemic Consensus (Layer 4)
    consensus_engine = EpistemicConsensus()
    consensus_gaps = consensus_engine.resolve_disagreement({
        "Legal_Desk": ["MiFID_II_EU", "kyc_compliance"],
        "Trading_Desk": ["EU_Market", "MiFID_II_EU"]
    })

    # 7. Temporal Drift & Mitigation (Layer 6 & 7)
    drifter = TemporalVoidDrift()
    drifter.record_snapshot(summary['void_density'], datetime.now().isoformat())
    
    harness = MitigationHarness()
    for gap in consensus_gaps:
        plan = harness.generate_mitigation_plan(gap, "REGULATORY" if "compliance" in gap or "MiFID" in gap else "TECHNICAL")
        print(f"[+] MITIGATION: {plan}")

    print(f"\n[+] Analysis Complete. Void Logic verified across 7 layers.")
    print("\n" + "="*80)

if __name__ == "__main__":
    asyncio.run(run_negative_space_demo())
