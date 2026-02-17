#!/usr/bin/env python3
"""
Simple script to generate personalized Ironman 70.3 training dashboards.
Run this to create custom dashboards from the template.
"""

import sys
from datetime import datetime, timedelta

def generate_dashboard(name, weight, race_date, goal="6:00"):
    """Generate a personalized dashboard HTML file"""

    # Read the template
    with open('training-dashboard.html', 'r') as f:
        template = f.read()

    # Calculate start date (22 weeks before race)
    race_dt = datetime.strptime(race_date, '%Y-%m-%d')
    start_dt = race_dt - timedelta(weeks=22)

    # Do replacements
    customized = template
    customized = customized.replace(
        "const RACE_DATE = new Date('2026-07-25');",
        f"const RACE_DATE = new Date('{race_date}');"
    )
    customized = customized.replace(
        "const START_DATE = new Date('2026-02-17');",
        f"const START_DATE = new Date('{start_dt.strftime('%Y-%m-%d')}');"
    )
    customized = customized.replace(
        "Athlete: Ian | 170 lbs | Goal: Sub-6 Hours",
        f"Athlete: {name} | {weight} lbs | Goal: Sub-{goal}"
    )
    customized = customized.replace(
        "<title>IM 70.3 Training Dashboard</title>",
        f"<title>{name}'s IM 70.3 Training Dashboard</title>"
    )

    # Save the customized version
    output_filename = f"{name.replace(' ', '-')}-ironman-dashboard.html"
    with open(output_filename, 'w') as f:
        f.write(customized)

    print(f"✅ Dashboard created: {output_filename}")
    print(f"📅 Race Date: {race_date}")
    print(f"🏃 Athlete: {name}")
    print(f"⚖️  Weight: {weight} lbs")
    print(f"🎯 Goal: Sub-{goal}")
    print(f"\n💡 Next: Open {output_filename} in your web browser!")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python generate-dashboard.py NAME WEIGHT RACE_DATE [GOAL]")
        print("Example: python generate-dashboard.py 'John Smith' 170 2026-07-25 6:00")
        sys.exit(1)

    name = sys.argv[1]
    weight = sys.argv[2]
    race_date = sys.argv[3]
    goal = sys.argv[4] if len(sys.argv) > 4 else "6:00"

    generate_dashboard(name, weight, race_date, goal)
