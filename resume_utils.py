import fitz  # PyMuPDF
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    return " ".join([page.get_text() for page in doc])

def analyze_resume(resume_file, job_desc):
    resume_text = extract_text_from_pdf(resume_file)

    prompt = f"""
    Analyze the resume below against the job description.
    Provide:
    1. Match percentage
    2. Strengths
    3. Weaknesses
    4. Matched & missing keywords
    5. Short resume summary

    Resume:
    {resume_text}

    Job Description:
    {job_desc}
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )

    return {
        "feedback": response['choices'][0]['message']['content']
    }
