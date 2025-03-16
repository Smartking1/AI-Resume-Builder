from flask import Flask, render_template, request, redirect, url_for, send_file
from resume_builder import ResumeBuilder
from config import OUTPUT_RESUME_PATH, UPLOADS_DIR
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
import io
import PyPDF2  # For multi-page PDF text extraction
import docx  # For reading Word documents

app = Flask(__name__)
app.config["UPLOADS_DIR"] = UPLOADS_DIR

def extract_text_from_pdf(file_path):
    """Extract text from a multi-page PDF file using PyPDF2."""
    try:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
            return text
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return None

def extract_text_from_docx(file_path):
    """Extract text from a Word document using python-docx."""
    try:
        doc = docx.Document(file_path)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text
    except Exception as e:
        print(f"Error extracting text from Word document: {e}")
        return None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    job_description = request.form["job_description"]
    template_name = request.form.get("template", "template1")  # Default to "template1"
    uploaded_file = request.files.get("resume_file")

    # Save the uploaded file (if any)
    original_resume = None
    if uploaded_file and uploaded_file.filename:
        # Ensure the uploads directory exists
        os.makedirs(app.config["UPLOADS_DIR"], exist_ok=True)

        # Save the uploaded file
        file_path = os.path.join(app.config["UPLOADS_DIR"], uploaded_file.filename)
        uploaded_file.save(file_path)

        # Extract text based on file type
        if uploaded_file.filename.lower().endswith(".pdf"):
            original_resume = extract_text_from_pdf(file_path)
        elif uploaded_file.filename.lower().endswith(".docx"):
            original_resume = extract_text_from_docx(file_path)
        else:
            # Handle other file types (e.g., .txt, .md)
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    original_resume = file.read()
            except UnicodeDecodeError:
                # Fallback to 'latin-1' if UTF-8 fails
                with open(file_path, "r", encoding="latin-1") as file:
                    original_resume = file.read()

        # Print the extracted text for debugging
        if original_resume:
            print("Extracted Text from Uploaded File:")
            print("=" * 50)
            print(original_resume)
            print("=" * 50)
        else:
            print("Failed to extract text from the uploaded file.")

    # Generate the resume
    builder = ResumeBuilder()
    resume = builder.generate_resume(job_description, template_name, original_resume)

    if resume:
        # Save the resume to a file
        builder.save_resume(resume)
        return redirect(url_for("view_resume"))
    else:
        return "Failed to generate resume. Please try again."
    
@app.route("/view_resume")
def view_resume():
    try:
        with open(OUTPUT_RESUME_PATH, "r", encoding="utf-8") as file:
            resume_content = file.read()
        return render_template("view_resume.html", resume_content=resume_content)
    except FileNotFoundError:
        return "Resume not found. Please generate a resume first."

@app.route("/download-pdf")
def download_pdf():
    try:
        # Read the generated resume content
        with open(OUTPUT_RESUME_PATH, "r", encoding="utf-8") as file:
            resume_content = file.read()

        # Create a PDF in memory
        buffer = io.BytesIO()
        pdf = SimpleDocTemplate(buffer, pagesize=letter)
        styles = getSampleStyleSheet()
        story = []

        # Add the resume content to the PDF
        for line in resume_content.split("\n"):
            if line.strip():  # Skip empty lines
                story.append(Paragraph(line, styles["BodyText"]))
                story.append(Spacer(1, 12))  # Add spacing between lines

        # Build the PDF
        pdf.build(story)

        # Move the buffer's cursor to the beginning
        buffer.seek(0)

        # Return the PDF as a downloadable file
        return send_file(
            buffer,
            as_attachment=True,
            download_name="generated_resume.pdf",
            mimetype="application/pdf"
        )
    except FileNotFoundError:
        return "Resume not found. Please generate a resume first."
    except Exception as e:
        print(f"Error generating PDF: {e}")
        return "Failed to generate PDF. Please try again."

if __name__ == "__main__":
    os.makedirs(app.config["UPLOADS_DIR"], exist_ok=True)
    app.run(debug=True)