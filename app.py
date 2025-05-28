from flask import Flask, request, jsonify
from flask_cors import CORS
from resume_utils import analyze_resume
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/api/analyze', methods=['POST'])
def analyze():
    resume_file = request.files.get("resume")
    job_desc = request.form.get("job_description")

    if not resume_file or not job_desc:
        return jsonify({"error": "Missing resume or job description"}), 400

    try:
        result = analyze_resume(resume_file, job_desc)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
