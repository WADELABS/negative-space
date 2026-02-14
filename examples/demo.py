"""
DEMO: Negative Space Framework in Action.
"""

import asyncio
import logging
from src.negative_space.agent import VoidAgent, VoidCollective
from src.negative_space.visualization import VoidVisualizer

async def main_example():
    """Main example demonstrating the Void Mapper framework."""
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    print("="*60)
    print("VOID MAPPER: NEGATIVE SPACE REASONING FRAMEWORK")
    print("="*60)
    
    # Define Point A (current state)
    point_a = {
        "dataset": "raw_customer_data.csv",
        "model_type": "undefined",
        "accuracy": 0.0,
        "features_extracted": False,
        "validation_set": None,
        "budget": 1000
    }
    
    # Define Point B (goal state)
    point_b = {
        "dataset": "processed_training_data.parquet",
        "model_type": "gradient_boosting",
        "accuracy": 0.85,
        "features_extracted": True,
        "validation_set": "validation_split_0.2",
        "budget": 5000,
        "deployment_ready": True
    }
    
    # Context
    context = {
        "dependencies": {
            "model_training": ["feature_extraction", "validation_set"],
            "deployment_ready": ["model_training", "testing"]
        },
        "constraints": {
            "max_cost": 10000,
            "time_limit": 30  # days
        },
        "ethical_concerns": ["data_privacy", "bias_detection"]
    }
    
    # Create void agent
    void_agent = VoidAgent(name="GapFinder", rigor=0.8)
    
    # Map the void
    print("\nMapping void between current state and goal...")
    report = await void_agent.map_voids(point_a, point_b, context)
    
    print(f"\nVoid Analysis Complete:")
    print(f"  Total gaps identified: {report['summary']['total_gaps']}")
    print(f"  Void density: {report['summary']['void_density']:.3f}")
    
    # Show critical findings
    if report['critical_findings']:
        print(f"\nCritical Findings ({len(report['critical_findings'])}):")
        for finding in report['critical_findings'][:3]:  # Show top 3
            print(f"  - {finding['description']}")
    
    # Show recommendations
    if report['recommendations']:
        print(f"\nRecommendations:")
        for rec in report['recommendations']:
            print(f"  - {rec}")
    
    # Collective Example
    print("\n\nCOLLECTIVE VOID MAPPING EXAMPLE")
    print("-"*40)
    collective = VoidCollective()
    collective_report = await collective.collective_void_mapping(point_a, point_b, context)
    print("Collective mapping complete.")
    
    print("\n" + "="*60)
    print("VOID MAPPING COMPLETE")
    print("="*60)

if __name__ == "__main__":
    asyncio.run(main_example())
