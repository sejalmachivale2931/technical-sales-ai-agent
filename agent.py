# Technical Sales Engineer AI Agent

# Step 1: read transcript
def read_transcript(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read().lower()


# Step 2: AI analysis logic
def analyze_transcript(text):

    pain_points = set()
    tech_stack = set()
    outcome = set()
    solution = set()

    # rule based mapping (AI logic)
    rules = {

        "excel": {
            "tech_stack": ["Excel"],
            "pain_points": ["Manual reporting using Excel"],
            "solution": ["Python automation + Power BI dashboard"]
        },

        "manual": {
            "pain_points": ["Manual process causing delay"]
        },

        "slow": {
            "pain_points": ["Slow system performance"]
        },

        "dashboard": {
            "outcome": ["Interactive dashboard"]
        },

        "cloud": {
            "outcome": ["Cloud scalability"],
            "solution": ["AWS / Azure cloud"]
        },

        "python": {
            "tech_stack": ["Python"]
        },

        "testing": {
            "pain_points": ["Manual testing effort"],
            "solution": ["Automated testing tools"]
        },

        "automation": {
            "outcome": ["Process automation"]
        },

        "legacy": {
            "pain_points": ["Legacy system limitations"],
            "solution": ["Modern low-code platform"]
        }
    }

    # apply AI rules
    for keyword, value in rules.items():

        if keyword in text:

            pain_points.update(value.get("pain_points", []))
            tech_stack.update(value.get("tech_stack", []))
            outcome.update(value.get("outcome", []))
            solution.update(value.get("solution", []))

    # default solution
    if not solution:
        solution.add("Custom AI-based solution")

    return format_output(pain_points, tech_stack, outcome, solution)


# Step 3: format output document
def format_output(pain_points, tech_stack, outcome, solution):

    result = f"""
AI Solution Design Document

Pain Points:
- {chr(10).join(pain_points)}

Current Tech Stack:
- {chr(10).join(tech_stack)}

Desired Outcome:
- {chr(10).join(outcome)}

Suggested Solution Architecture:
- {chr(10).join(solution)}

Implementation Steps:
1. Requirement Analysis
2. Architecture Design
3. Development
4. Testing
5. Deployment
"""

    return result


# Step 4: run complete AI agent
transcript = read_transcript("meeting2.txt")

response = analyze_transcript(transcript)

print(response)


# Step 5: save output file
with open("solution_design.txt", "w", encoding="utf-8") as f:
    f.write(response)

print("\nFile saved: solution_design.txt")
