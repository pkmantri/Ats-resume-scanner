# utils/visualizer.py

import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
from fpdf import FPDF
import datetime
import unicodedata

def safe_text(text):
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")

def plot_skill_match(skills_dict):
    """
    Creates a radar chart for skill match coverage.
    Shows 0 if a category is empty.
    """
    categories = list(skills_dict.keys())
    values = [len(skills_dict.get(cat, [])) for cat in categories]

    # Radar chart needs circular plot
    values += values[:1]
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.plot(angles, values, color='green', linewidth=2)
    ax.fill(angles, values, color='skyblue', alpha=0.25)

    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=12)

    st.pyplot(fig)


def generate_pdf_report(name, evaluation, skills_dict, match_score_text, cover_letter=None):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, safe_text("ATS Resume Scanner Report"), ln=True, align="C")
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, safe_text(f"Candidate: {name}"), ln=True)
    pdf.cell(200, 10, f"Date: {datetime.date.today()}", ln=True)
    pdf.ln(10)

    # Evaluation
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, safe_text("1. Resume Evaluation"), ln=True)
    pdf.set_font("Arial", size=11)
    for line in evaluation.split('\n'):
        pdf.multi_cell(0, 10, safe_text(line))
    pdf.ln(5)

    # Skills
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, safe_text("2. Extracted Skills"), ln=True)
    pdf.set_font("Arial", size=11)
    for category, items in skills_dict.items():
        pdf.set_font("Arial", "B", 12)
        pdf.cell(200, 10, safe_text(f"{category}:"), ln=True)
        pdf.set_font("Arial", size=11)
        pdf.multi_cell(0, 10, safe_text(', '.join(items)) if items else "None")
    pdf.ln(5)

    # Match Score
    pdf.set_font("Arial", "B", 14)
    pdf.cell(200, 10, safe_text("3. Match Score"), ln=True)
    pdf.set_font("Arial", size=11)
    for line in match_score_text.split('\n'):
        pdf.multi_cell(0, 10, safe_text(line))
    pdf.ln(5)

    # Cover Letter (optional)
    if cover_letter:
        pdf.set_font("Arial", "B", 14)
        pdf.cell(200, 10, safe_text("4. AI-Generated Cover Letter"), ln=True)
        pdf.set_font("Arial", size=11)
        for line in cover_letter.split('\n'):
            pdf.multi_cell(0, 10, safe_text(line))

    # Output PDF bytes with safe encoding
    return pdf.output(dest='S').encode('latin1', 'ignore')
