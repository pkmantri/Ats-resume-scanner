# 🧠 ATS Resume Scanner Pro

An AI-powered Applicant Tracking System (ATS) Resume Scanner built with **Streamlit**, **Python**, and **Google Gemini API**. Upload your resume and a job description to receive:
- An AI evaluation
- Extracted skills
- Match percentage
- A personalized cover letter
- A downloadable PDF report

---

## 🔍 Features

✅ Upload resume (PDF)  
✅ Paste job description  
✅ Get AI-powered resume evaluation  
✅ Extract technical, analytical, and soft skills  
✅ View skill coverage on a radar chart  
✅ See match score and missing keywords  
✅ Generate a cover letter using AI  
✅ Download a PDF report of everything

---

## 📷 Screenshots

> Coming soon...

---

## 🚀 Demo

Want to try it live? Deploy to Streamlit Cloud or Render — setup guide below.

---

## 🛠 Tech Stack

| Tool | Use |
|------|-----|
| **Python** | Core backend logic |
| **Streamlit** | Frontend + web app |
| **Google Gemini API** | AI content generation |
| **PyPDF2** | Resume PDF parsing |
| **Matplotlib** | Skill radar charts |
| **FPDF** | PDF report generation |

---

## 🧩 Installation

1. **Clone the repository**

```bash
git clone https://github.com/pkmantri/ats-resume-scanner.git
cd ats-resume-scanner

---

2. **Create and Activate a Virtual Environment**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

---

3. **Install Requirements**

```bash
pip install -r requirements.txt

---

4. **Add Google Gemini API Key**
Create a .env file in the root folder and add:

```ini
GOOGLE_API_KEY=your_gemini_api_key_here
🔑 Get your API key from Google AI Studio

---

▶️ Run the App
```bash
streamlit run app.py
