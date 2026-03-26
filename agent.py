# Technical Sales Engineer AI Agent

# read transcript file
def read_transcript(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read().lower()


def analyze_transcript(text):

    pain_points = []
    tech_stack = []
    outcome = []
    solution = []

    # logic rules

    if "excel" in text:
        tech_stack.append("Excel")
        pain_points.append("Manual reporting using Excel")
        solution.append("Python automation + Power BI dashboard")

    if "manual" in text:
        pain_points.append("Manual process causing delay")

    if "slow" in text:
        pain_points.append("Slow system performance")

    if "dashboard" in text:
        outcome.append("Interactive dashboard")

    if "cloud" in text:
        outcome.append("Cloud scalability")
        solution.append("AWS / Azure cloud")

    if "python" in text:
        tech_stack.append("Python")

    if "testing" in text:
        pain_points.append("Manual testing effort")
        solution.append("Automated testing tools")

    if "automation" in text:
        outcome.append("Process automation")

    if "legacy" in text:
        pain_points.append("Legacy system limitations")
        solution.append("Modern low-code platform")

    if not solution:
        solution.append("Custom AI-based solution")

    result = f"""
AI Solution Design Document

Pain Points:
- {chr(10).join(set(pain_points))}

Current Tech Stack:
- {chr(10).join(set(tech_stack))}

Desired Outcome:
- {chr(10).join(set(outcome))}

Suggested Solution Architecture:
- {chr(10).join(set(solution))}

Implementation Steps:
1. Requirement Analysis
2. Architecture Design
3. Development
4. Testing
5. Deployment
"""

    return result


transcript = read_transcript("meeting1.txt")

response = analyze_transcript(transcript)

print(response)


with open("solution_design.txt", "w", encoding="utf-8") as f:
    f.write(response)

print("\nFile saved: solution_design.txt")