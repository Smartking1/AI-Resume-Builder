# resume_builder.py

from groq_client import GroqClient
from config import RESUME_PROMPT_TEMPLATE, RESUME_MODIFICATION_PROMPT_TEMPLATE, TEMPLATES_DIR, OUTPUT_RESUME_PATH
from utils import load_template

class ResumeBuilder:
    def __init__(self):
        self.groq_client = GroqClient()

    def generate_resume(self, job_description, template_name=None, original_resume=None):
        # Default to "template1" if no template is provided
        if not template_name:
            template_name = "template1"

        if original_resume:
            # Modify the existing resume
            prompt = RESUME_MODIFICATION_PROMPT_TEMPLATE.format(
                job_description=job_description,
                original_resume=original_resume
            )
        else:
            # Generate a new resume using the selected template
            template_path = f"{TEMPLATES_DIR}/{template_name}.md"
            try:
                resume_template = load_template(template_path)
            except FileNotFoundError:
                return f"Error: Template file '{template_name}.md' not found."

            prompt = RESUME_PROMPT_TEMPLATE.format(
                job_description=job_description,
                resume_template=resume_template
            )

        # Generate the resume using the Groq client
        generated_resume = self.groq_client.generate_text(prompt)
        return generated_resume

    def save_resume(self, resume_text, output_path=OUTPUT_RESUME_PATH):
        with open(output_path, "w") as file:
            file.write(resume_text)
        print(f"Resume saved to {output_path}")