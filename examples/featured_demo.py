"""
Featured Demo: Comprehensive Negative Space Framework Showcase
Demonstrates migration from monolith to microservices architecture.
"""

import asyncio
import json
import logging
from pathlib import Path

from negative_space import VoidAgent, VoidCollective, GapCriticality, VoidType


async def monolith_to_microservices_demo():
    """
    Comprehensive demo: Mapping the void between monolith and microservices.
    This represents a realistic software architecture transformation scenario.
    """
    logging.basicConfig(
        level=logging.WARNING,  # Reduce noise for demo
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    print("="*70)
    print("NEGATIVE SPACE FRAMEWORK - FEATURED DEMO")
    print("Scenario: Monolith to Microservices Migration")
    print("="*70)
    print()
    
    # Define Point A: Current Monolith State
    point_a = {
        "architecture": "monolithic",
        "deployment": "single_server",
        "database": "shared_mysql",
        "auth": "session_based",
        "services": ["user_management", "order_processing", "inventory"],
        "containerization": False,
        "orchestration": None,
        "monitoring": "basic_logs",
        "scaling": "vertical",
        "latency_p99": 2000,  # ms
        "deployment_time": 120,  # minutes
        "team_size": 8,
        "budget": 50000,
    }
    
    # Define Point B: Target Microservices State
    point_b = {
        "architecture": "microservices",
        "deployment": "kubernetes_cluster",
        "database": "polyglot_persistence",
        "auth": "jwt_oauth2",
        "services": [
            "user_service",
            "order_service", 
            "inventory_service",
            "notification_service",
            "analytics_service"
        ],
        "containerization": True,
        "orchestration": "k8s",
        "monitoring": "observability_stack",  # Prometheus, Grafana, Jaeger
        "scaling": "horizontal_auto",
        "latency_p99": 200,  # ms
        "deployment_time": 5,  # minutes (CI/CD)
        "api_gateway": "kong",
        "service_mesh": "istio",
        "event_bus": "kafka",
        "team_size": 15,
        "budget": 200000,
    }
    
    # Context: Constraints, dependencies, and considerations
    context = {
        "dependencies": {
            "k8s_deployment": ["containerization", "orchestration_knowledge"],
            "service_mesh": ["k8s_deployment", "network_policies"],
            "observability": ["distributed_tracing", "metrics_collection"],
            "api_gateway": ["service_discovery", "routing_rules"],
        },
        "constraints": {
            "max_budget": 250000,
            "timeline_months": 12,
            "zero_downtime_required": True,
            "data_migration_complexity": "high",
        },
        "ethical_concerns": [
            "data_privacy_during_migration",
            "service_reliability_guarantees",
            "technical_debt_communication",
        ],
        "risks": [
            "distributed_system_complexity",
            "network_latency_issues",
            "eventual_consistency_challenges",
        ]
    }
    
    # Create void agent with high rigor for production readiness assessment
    print("🔍 Initializing Void Agent (rigor=0.85)...")
    void_agent = VoidAgent(name="ArchitectureMapper", rigor=0.85)
    
    # Map the void
    print("📊 Mapping void between monolith and microservices...")
    print()
    report = await void_agent.map_voids(point_a, point_b, context)
    
    # ============== DISPLAY RESULTS ==============
    
    print("="*70)
    print("VOID ANALYSIS RESULTS")
    print("="*70)
    print()
    
    # Summary metrics
    summary = report['summary']
    print("📈 KEY METRICS")
    print("-" * 70)
    print(f"  Total Gaps Identified:    {summary['total_gaps']}")
    print(f"  Void Density:            {summary['void_density']:.3f} (0=nothing missing, 1=everything missing)")
    print(f"  Navigability:            {summary.get('navigability', 0.0):.3f} (0=impassable, 1=clear path)")
    print(f"  Connectivity:            {summary.get('connectivity', 0.0):.3f} (gap interdependence)")
    print(f"  Blocking Gaps:           {summary.get('blocking_gaps', 0)}")
    print(f"  Fillable Gaps:           {summary.get('fillable_gaps', 0)}")
    print()
    
    # Gap criticality distribution
    if 'patterns' in report and 'criticality_distribution' in report['patterns']:
        print("🎯 GAP CRITICALITY DISTRIBUTION")
        print("-" * 70)
        for criticality, count in report['patterns']['criticality_distribution'].items():
            print(f"  {criticality:15s}: {count:3d} gaps")
        print()
    
    # Critical findings
    if report['critical_findings']:
        print("⚠️  CRITICAL FINDINGS (Top 5)")
        print("-" * 70)
        for i, finding in enumerate(report['critical_findings'][:5], 1):
            print(f"{i}. [{finding['void_type']}] {finding['description']}")
            print(f"   Criticality: {finding['criticality']} | Certainty: {finding['certainty']}")
        print()
    
    # Gap clusters
    if report.get('clusters'):
        print("🔗 GAP CLUSTERS")
        print("-" * 70)
        for i, cluster in enumerate(report['clusters'][:3], 1):
            print(f"Cluster {i}: {len(cluster.get('gaps', []))} related gaps")
            print(f"  Density: {cluster.get('density', 0):.3f} | Strategic importance: {cluster.get('strategic_importance', 0):.3f}")
        print()
    
    # Navigation plan
    if report.get('navigation_plan'):
        nav_plan = report['navigation_plan']
        print("🗺️  RECOMMENDED NAVIGATION PLAN")
        print("-" * 70)
        print(f"Strategy: {nav_plan.get('strategy', 'Unknown')}")
        if 'path' in nav_plan and nav_plan['path']:
            print("\nSuggested Path (first 5 steps):")
            for i, step in enumerate(nav_plan['path'][:5], 1):
                print(f"{i}. {step.get('description', 'N/A')}")
                print(f"   Action: {step.get('action', 'N/A')}")
                if 'estimated_cost' in step:
                    print(f"   Est. Cost: ${step['estimated_cost']:,.0f} | Time: {step.get('estimated_time', 0):.1f} days")
        if 'total_cost' in nav_plan:
            print(f"\nTotal Estimated Cost: ${nav_plan['total_cost']:,.0f}")
            print(f"Total Estimated Time: {nav_plan.get('total_time', 0):.1f} days")
        print()
    
    # Recommendations
    if report['recommendations']:
        print("💡 RECOMMENDATIONS")
        print("-" * 70)
        for i, rec in enumerate(report['recommendations'], 1):
            print(f"{i}. {rec}")
        print()
    
    # ============== EXPORT JSON REPORT ==============
    
    print("="*70)
    print("EXPORTING REPORTS")
    print("="*70)
    print()
    
    # Save full JSON report
    output_file = Path(__file__).parent.parent / "demo_output_report.json"
    with open(output_file, 'w') as f:
        json.dump(report, f, indent=2, default=str)
    print(f"✅ Full JSON report saved to: {output_file}")
    
    # Also save a simplified console-friendly version
    console_report = {
        "scenario": "Monolith to Microservices Migration",
        "summary": summary,
        "critical_findings_count": len(report['critical_findings']),
        "top_blocking_gaps": [
            f for f in report['critical_findings'] 
            if f['criticality'] == 'BLOCKING'
        ][:3],
        "recommendations": report['recommendations'][:5],
    }
    
    console_file = Path(__file__).parent.parent / "demo_console_report.json"
    with open(console_file, 'w') as f:
        json.dump(console_report, f, indent=2, default=str)
    print(f"✅ Console report saved to: {console_file}")
    print()
    
    # ============== COLLECTIVE MAPPING (OPTIONAL) ==============
    
    print("="*70)
    print("COLLECTIVE VOID MAPPING (Multi-Agent Consensus)")
    print("="*70)
    print()
    print("Running collective mapping with specialized agents...")
    
    collective = VoidCollective()
    collective_report = await collective.collective_void_mapping(point_a, point_b, context)
    
    print(f"✅ Collective analysis complete")
    print(f"   Consensus result: {collective_report.get('consensus', 'N/A')}")
    print(f"   Agreement score: {collective_report.get('agreement_score', 0):.3f}")
    print()
    
    # ============== FINAL SUMMARY ==============
    
    print("="*70)
    print("DEMO COMPLETE")
    print("="*70)
    print()
    print("This demo showcased:")
    print("  ✓ Comprehensive void mapping between two states")
    print("  ✓ Multi-dimensional gap characterization")
    print("  ✓ Criticality and navigability analysis")
    print("  ✓ Strategic navigation planning")
    print("  ✓ JSON report generation for tool integration")
    print("  ✓ Multi-agent collective consensus")
    print()
    print("Next steps:")
    print("  → Review demo_output_report.json for full analysis")
    print("  → Integrate void reports into your CI/CD pipeline")
    print("  → Explore docs/GLOSSARY.md for terminology")
    print("  → Check docs/VOID_REPORT_SCHEMA.md for JSON schema")
    print()


if __name__ == "__main__":
    asyncio.run(monolith_to_microservices_demo())
