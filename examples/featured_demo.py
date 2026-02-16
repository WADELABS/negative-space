"""
Featured Demo: Monolith to Microservices Migration

This demo showcases the Negative Space Framework's capability to analyze
a realistic software engineering scenario: migrating from a monolithic
application to a microservices architecture.

It demonstrates:
- Comprehensive void mapping
- Gap criticality analysis across 8 void types
- Strategic navigation planning
- JSON report generation
- Key metrics: void density, navigability, connectivity

Run with:
    python examples/featured_demo.py
    or
    python -m negative_space.demo
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
    print("📊 SUMMARY METRICS:")
    print(f"   Total gaps identified: {summary['total_gaps']}")
    print(f"   Void density: {summary['void_density']:.3f} (0=nothing missing, 1=almost everything missing)")
    print(f"   Navigability: {summary['navigability']:.3f} (0=many bottlenecks, 1=clear paths)")
    print(f"   Connectivity: {summary['connectivity']:.3f} (0=isolated gaps, 1=highly connected)")
    print()
    
    # Critical findings
    if report['critical_findings']:
        print("⚠️  CRITICAL FINDINGS:")
        print(f"   {len(report['critical_findings'])} critical gaps require immediate attention")
        print()
        for i, finding in enumerate(report['critical_findings'][:5], 1):
            print(f"   {i}. {finding['description']}")
            print(f"      Type: {finding.get('type', 'UNKNOWN')}")
            print(f"      Certainty: {finding.get('certainty', 'UNKNOWN')}")
            print()
    
    # Gap distribution by type
    patterns = report.get('patterns', {})
    gap_dist = patterns.get('gap_distribution', {})
    if gap_dist:
        print("📈 GAP DISTRIBUTION BY TYPE:")
        for gap_type, count in sorted(gap_dist.items(), key=lambda x: x[1], reverse=True):
            print(f"   {gap_type}: {count} gaps")
        print()
    
    # Criticality distribution
    crit_dist = patterns.get('criticality_distribution', {})
    if crit_dist:
        print("🚨 CRITICALITY DISTRIBUTION:")
        for level, count in sorted(crit_dist.items(), 
                                   key=lambda x: {'BLOCKING': 4, 'HIGH': 3, 'MEDIUM': 2, 'LOW': 1, 'UNKNOWN': 0}.get(x[0], 0),
                                   reverse=True):
            print(f"   {level}: {count} gaps")
        print()
    
    # Fillability analysis
    fillability_rate = patterns.get('fillability_rate', 0)
    print("🔧 FILLABILITY ANALYSIS:")
    print(f"   {fillability_rate*100:.1f}% of gaps appear fillable")
    if fillability_rate > 0.7:
        print("   ✓ Optimistic: Most gaps can be addressed")
    elif fillability_rate < 0.3:
        print("   ⚠ Pessimistic: Many gaps may be structural constraints")
    else:
        print("   ≈ Moderate: Balanced mix of fillable and structural gaps")
    print()
    
    # Gap clusters
    clusters = report.get('gap_clusters', [])
    if clusters:
        print("🔗 GAP CLUSTERING:")
        print(f"   {len(clusters)} clusters identified")
        for cluster in clusters[:3]:
            print(f"   - Cluster {cluster.get('id', 'unknown')}: {cluster.get('size', 0)} gaps ({cluster.get('type', 'unknown')})")
        print()
    
    # Navigation plan
    nav_plan = report.get('navigation_plan', {})
    if nav_plan:
        strategy = nav_plan.get('strategy', 'unknown')
        print("🧭 NAVIGATION STRATEGY:")
        print(f"   Recommended: {strategy}")
        
        path = nav_plan.get('path', [])
        if path:
            print(f"   Path has {len(path)} steps")
            if len(path) > 0:
                print(f"   First step: {path[0].get('description', 'unknown')}")
        
        total_cost = nav_plan.get('total_cost', 0)
        total_time = nav_plan.get('total_time', 0)
        if total_cost > 0:
            print(f"   Estimated cost: ${total_cost:,.0f}")
        if total_time > 0:
            print(f"   Estimated time: {total_time:.1f} months")
        print()
    
    # Recommendations
    recommendations = report.get('recommendations', [])
    if recommendations:
        print("💡 RECOMMENDATIONS:")
        for i, rec in enumerate(recommendations, 1):
            print(f"   {i}. {rec}")
        print()
    
    # Insights
    insights = patterns.get('insights', [])
    if insights:
        print("🔍 INSIGHTS:")
        for insight in insights:
            print(f"   • {insight}")
        print()
    
    # ========================================================================
    # SAVE JSON REPORT
    # ========================================================================
    print("="*80)
    print(" SAVING REPORTS")
    print("="*80)
    print()
    
    # Add metadata to report for JSON schema compliance
    report['schema_version'] = '1.0'
    report['timestamp'] = datetime.now().isoformat()
    report['void_map_id'] = summary.get('void_map_id', 'demo_migration')
    
    # Save detailed JSON report to current directory for easy access
    report_path = Path.cwd() / 'demo_output_report.json'
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2, default=str)
    
    print(f"✅ Detailed JSON report saved to: {report_path}")
    print(f"   File size: {report_path.stat().st_size} bytes")
    print()
    
    print("="*80)
    print(" DEMO COMPLETE")
    print("="*80)
    print()
    print("Next steps:")
    print("  1. Review the JSON report: demo_output_report.json")
    print("  2. Examine the void types and criticality levels")
    print("  3. Follow the navigation plan for migration")
    print("  4. Address blocking gaps first")
    print()
    print("Learn more:")
    print("  - Glossary: docs/GLOSSARY.md")
    print("  - JSON Schema: docs/VOID_REPORT_SCHEMA.md")
    print("  - Examples: examples/README.md")
    print()
    
    return report

def main():
    """Entry point for the featured demo."""
    asyncio.run(featured_demo())

if __name__ == "__main__":
    main()
