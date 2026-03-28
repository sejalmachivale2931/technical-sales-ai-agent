# AI Technical Sales Engineer Agent

## Project Overview

This project is a rule-based AI agent that analyzes client meeting transcripts and automatically generates a structured Solution Design Document.

The agent identifies:

* Client pain points
* Existing technology stack
* Desired outcomes
* Suggested solution architecture

The system uses a dataset-driven approach where keywords and solution mappings are stored in a CSV file. This makes the agent dynamic and easily configurable without modifying the main code.

---

## How It Works

1. The agent reads client requirements from meeting.txt
2. It compares the text with keywords stored in keywords_large.csv
3. Matching keywords are used to identify:

   * Pain Points
   * Current Tech Stack
   * Desired Outcome
   * Suggested Solution
4. The result is automatically saved in solution_design.txt

---

## Project Structure

sales_agent_project

│
├── meeting.txt
├── keywords_large.csv
├── agent.py
├── solution_design.txt
└── README.md

---

## Example Input (meeting.txt)

Client is using excel sheets for reporting.
The process is manual and very slow.
We want automation and dashboard.
System should scale in future.
We are open to cloud deployment.
Currently some scripts are written in python.

---

## Example Output

AI SOLUTION DESIGN

PAIN POINTS

* Manual reporting using Excel
* Manual process causing delay
* Slow system performance

CURRENT TECH STACK

* Excel
* Python

DESIRED OUTCOME

* Interactive dashboard
* Process automation
* Cloud scalability

SUGGESTED SOLUTION

* Python automation
* Power BI dashboard
* AWS / Azure cloud

---

## Installation

Install required library:

pip install pandas

---

## How to Run

Step 1: Update meeting1.txt with client requirements

Step 2: Run the script:

python agent.py

Step 3: Output will be saved automatically:

solution_design.txt

---

## Key Features

Dynamic behaviour – changing input automatically changes output

Dataset-driven logic – keywords and mappings stored in CSV file

No paid API required

Easy to modify and extend

End-to-end working AI agent

Simple and explainable logic

---

## Technology Used

Python

Pandas

CSV dataset

Rule-based AI logic

---

## Future Improvements

Add NLP-based keyword matching

Add confidence score for solution relevance

Add Streamlit UI for interactive interface

Integrate with CRM system

Use LLM API for advanced reasoning

---

## Author

Sejal Machivale
