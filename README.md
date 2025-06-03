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
git clone https://github.com/your-username/ats-resume-scanner.git
cd ats-resume-scanner

Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set up environment variables

Create a .env file in the root folder:

ini
Copy
Edit
GOOGLE_API_KEY=your_google_gemini_api_key
Run the app

bash
Copy
Edit
streamlit run app.py
📦 Folder Structure
bash
Copy
Edit
ats-resume-scanner/
├── app.py
├── requirements.txt
├── .env
├── .streamlit/secrets.toml
├── utils/
│   ├── analyzer.py
│   ├── parser.py
│   └── visualizer.py
└── README.md
☁️ Deployment (Optional)
✅ Streamlit Cloud
Push your code to a GitHub repository

Go to streamlit.io/cloud

Connect your GitHub → Select this repo

Add your GOOGLE_API_KEY in .streamlit/secrets.toml:

toml
Copy
Edit
GOOGLE_API_KEY = "your-key-here"
🧠 AI Prompts in Use
Resume analysis

Skill extraction

Match percentage

Cover letter writing

🤝 Contributing
Pull requests are welcome! If you'd like to collaborate or add features like LinkedIn scraping, feedback scoring, or resume editing — feel free to fork and submit a PR.



