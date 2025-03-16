# config.py
import os
# Groq API configuration
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
MODEL_NAME = "llama3-70b-8192"  # Example model name

# File paths
TEMPLATES_DIR = "./templates"
UPLOADS_DIR = "./uploads"
OUTPUT_RESUME_PATH = "static/generated_resume.md"

# Prompt templates
RESUME_PROMPT_TEMPLATE = """
You are a professional resume builder. Generate a tailored, ATS-friendly resume based on the following job description:

Job Description:
{job_description}

Use the following template as a guide:
{resume_template}

Ensure the resume:
1. Highlights relevant skills, experiences, and achievements that match the job description.
2. Uses keywords from the job description to improve ATS compatibility.
3. Is well-structured, concise, and professional.
4. Avoids unnecessary personal information (e.g., age, gender, photo).
5. Includes a professional summary, skills section, work experience, education, and certifications (if applicable).

Return only the resume content in Markdown format.
"""

RESUME_MODIFICATION_PROMPT_TEMPLATE = """
You are a professional resume builder. Modify the following resume to better match the job description:

Job Description:
{job_description}

Original Resume:
{original_resume}

Ensure the modified resume:
1. Highlights relevant skills, experiences, and achievements that match the job description.
2. Uses keywords from the job description to improve ATS compatibility.
3. Is well-structured, concise, and professional.
4. Avoids unnecessary personal information (e.g., age, gender, photo).
5. Includes a professional summary, skills section, work experience, education, and certifications (if applicable).

Return only the modified resume content in Markdown format.
"""