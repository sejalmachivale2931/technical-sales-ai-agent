import pandas as pd


keywords_df = pd.read_csv("keywords.csv")


def read_meeting(file_name):

    with open(file_name, "r", encoding="utf-8") as f:
        return f.read().lower()


def analyze_text(text):

    matched_rows = keywords_df[
        keywords_df["keyword"].apply(lambda k: k.lower() in text)
    ]

    return {
        "pain_points": matched_rows["pain_points"].dropna().unique(),
        "tech_stack": matched_rows["tech_stack"].dropna().unique(),
        "outcome": matched_rows["outcome"].dropna().unique(),
        "solution": matched_rows["solution"].dropna().unique(),
        "implementation_steps": matched_rows["implementation_step"].dropna().unique()
    }


meeting_text = read_meeting("meeting1.txt")

result = analyze_text(meeting_text)


def format_list(title, items):

    if len(items) == 0:
        return f"{title}:\n - Not identified\n"

    formatted = "\n".join([f" - {item}" for item in items])

    return f"{title}:\n{formatted}\n"



output_text = f"""
================ AI SOLUTION DESIGN ================

CLIENT REQUIREMENT:
{meeting_text}

{format_list("PAIN POINTS", result["pain_points"])}

{format_list("CURRENT TECH STACK", result["tech_stack"])}

{format_list("DESIRED OUTCOME", result["outcome"])}

{format_list("SUGGESTED SOLUTION", result["solution"])}

{format_list("IMPLEMENTATION STEPS", result["implementation_steps"])}

====================================================
"""



with open("solution_design.txt", "w", encoding="utf-8") as f:
    f.write(output_text)


print(output_text)

print("\nresult saved to solution_design.txt")
