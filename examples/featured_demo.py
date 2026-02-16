"""
Featured Demo: Monolith to Microservices Migration
====================================================

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
from datetime import datetime
from pathlib import Path

from negative_space import VoidAgent, GapCriticality, VoidType

async def featured_demo():
    """
    Comprehensive demonstration of negative space reasoning
    for a monolith-to-microservices migration.
    """
    
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(message)s'
    )
    
    print("="*80)
    print(" NEGATIVE SPACE FRAMEWORK - FEATURED DEMO")
    print(" Scenario: Monolith to Microservices Migration")
    print("="*80)
    print()
    
    # ========================================================================
    # POINT A: Current State (Monolithic Application)
    # ========================================================================
    point_a = {
        "architecture": "monolith",
        "deployment": "single_vm",
        "database": "single_postgres",
        "auth": "session_based",
        "scaling": "vertical_only",
        "monitoring": "basic_logs",
        "team_structure": "single_team",
        "cicd": "manual_deployment",
        "api_gateway": False,
        "service_mesh": False,
        "containers": False,
        "orchestration": None,
        "observability": "minimal",
        "fault_tolerance": "none",
        "data_consistency": "acid",
        "security": "perimeter_defense",
        "documentation": "outdated",
        "team_skills": ["python", "sql"],
        "budget": 50000,
        "timeline_months": 0
    }
    
    # ========================================================================
    # POINT B: Target State (Microservices Architecture)
    # ========================================================================
    point_b = {
        "architecture": "microservices",
        "deployment": "kubernetes_cluster",
        "database": "polyglot_persistence",
        "auth": "oauth2_jwt",
        "scaling": "horizontal_autoscaling",
        "monitoring": "distributed_tracing",
        "team_structure": "autonomous_teams",
        "cicd": "gitops_automated",
        "api_gateway": True,
        "service_mesh": True,
        "containers": True,
        "orchestration": "kubernetes",
        "observability": "prometheus_grafana_jaeger",
        "fault_tolerance": "circuit_breakers_retries",
        "data_consistency": "eventual_consistency",
        "security": "zero_trust",
        "documentation": "api_specs_runbooks",
        "team_skills": ["python", "sql", "kubernetes", "docker", "go", "terraform"],
        "budget": 500000,
        "timeline_months": 12,
        "service_count": 15,
        "deployment_frequency": "multiple_per_day"
    }
    
    # ========================================================================
    # CONTEXT: Constraints, Dependencies, and Ethical Concerns
    # ========================================================================
    context = {
        "dependencies": {
            "kubernetes_deployment": ["containers", "orchestration", "cicd"],
            "service_mesh": ["kubernetes_deployment", "observability"],
            "horizontal_scaling": ["containers", "orchestration"],
            "distributed_tracing": ["service_mesh", "observability"],
            "autonomous_teams": ["team_skills", "documentation"],
            "zero_trust": ["auth", "api_gateway", "service_mesh"]
        },
        "constraints": {
            "max_budget": 600000,
            "max_timeline_months": 18,
            "cannot_stop_production": True,
            "team_size": 8,
            "regulatory_compliance": ["GDPR", "SOC2"]
        },
        "ethical_concerns": [
            "data_migration_risk",
            "service_availability_during_transition",
            "team_training_burnout",
            "technical_debt_vs_new_features"
        ],
        "business_goals": {
            "improve_scalability": "high_priority",
            "reduce_deployment_time": "high_priority",
            "improve_fault_tolerance": "medium_priority",
            "enable_team_autonomy": "medium_priority"
        }
    }
    
    print("📍 POINT A (Current State):")
    print(f"   Architecture: {point_a['architecture']}")
    print(f"   Deployment: {point_a['deployment']}")
    print(f"   Team: {len(point_a['team_skills'])} core skills")
    print()
    
    print("🎯 POINT B (Target State):")
    print(f"   Architecture: {point_b['architecture']}")
    print(f"   Deployment: {point_b['deployment']}")
    print(f"   Team: {len(point_b['team_skills'])} required skills")
    print(f"   Timeline: {point_b['timeline_months']} months")
    print(f"   Budget: ${point_b['budget']:,}")
    print()
    
    print("🔍 Initializing Void Agent...")
    agent = VoidAgent(name="ArchitectureMigrationAnalyzer", rigor=0.85)
    print(f"   Agent: {agent.name}")
    print(f"   Rigor: {agent.rigor}")
    print()
    
    # ========================================================================
    # VOID MAPPING: Identify all gaps between A and B
    # ========================================================================
    print("🗺️  Mapping voids between current state and target state...")
    print("   This may take a moment as we analyze the gap space...")
    print()
    
    report = await agent.map_voids(point_a, point_b, context)
    
    # ========================================================================
    # DISPLAY RESULTS
    # ========================================================================
    print("="*80)
    print(" VOID ANALYSIS RESULTS")
    print("="*80)
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
    
    # Save detailed JSON report
    report_path = Path(__file__).parent.parent / 'demo_output_report.json'
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2, default=str)
    
    print(f"✅ Detailed JSON report saved to: {report_path}")
    print(f"   File size: {report_path.stat().st_size} bytes")
    print()
    
    # Save console output
    console_output_path = Path(__file__).parent.parent / 'demo_output.txt'
    print(f"💾 Console output available at: {console_output_path}")
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
