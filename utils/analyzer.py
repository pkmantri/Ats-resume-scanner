# utils/analyzer.py

import google.generativeai as genai
import json
import os
from dotenv import load_dotenv

# Configure Gemini API
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")  # Use "gemini-1.5-pro" if needed

def review_resume(resume_text, job_description):
    prompt = f"""
You are an experienced HR professional. Analyze the resume below against the job description.

Resume:
\"\"\"{resume_text}\"\"\"

Job Description:
\"\"\"{job_description}\"\"\"

Please provide a detailed evaluation with:
- Strengths
- Weaknesses
- Fit for the role
"""
    response = model.generate_content(prompt)
    return response.text.strip()

def extract_skills(resume_text, job_description):
    prompt = f"""
You are an ATS system. Compare the resume and job description.

Resume:
\"\"\"{resume_text}\"\"\"

Job Description:
\"\"\"{job_description}\"\"\"

Extract matching and missing skills. Return in this JSON format:
{{
  "Technical Skills": [],
  "Analytical Skills": [],
  "Soft Skills": []
}}

Only use skills found in the job description. If a category has no matching skills, return an empty list for that category.
"""
    try:
        response = model.generate_content(prompt)
        text = response.text.strip()
        json_start = text.find("{")
        json_data = json.loads(text[json_start:])
        return json_data
    except Exception as e:
        return {"error": str(e), "raw_response": response.text if 'response' in locals() else "No response"}

def match_percentage(resume_text, job_description):
    prompt = f"""
Act as an ATS evaluator. Given the resume and job description, provide:

1. Match Percentage (out of 100%)
2. Missing Keywords
3. Final Thoughts

Format your response clearly and professionally.

Resume:
\"\"\"{resume_text}\"\"\"

Job Description:
\"\"\"{job_description}\"\"\"
"""
    response = model.generate_content(prompt)
    return response.text.strip()

def generate_cover_letter(resume_text, job_description, your_name="John Doe"):
    prompt = f"""
You are a professional career assistant.

Given the resume and job description below, generate a personalized, ATS-friendly cover letter for the role. Keep it concise and impactful.

Resume:
\"\"\"{resume_text}\"\"\"

Job Description:
\"\"\"{job_description}\"\"\"

Start with "Dear Hiring Manager" and end with a professional closing. Mention the candidate name as {your_name}.
"""
    response = model.generate_content(prompt)
    return response.text.strip()
