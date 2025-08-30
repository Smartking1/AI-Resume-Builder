# AI Resume Builder

AI Resume Builder is a web application that generates tailored, ATS-friendly resumes using AI. Users can input a job description, select a resume template, and optionally upload their existing resume for optimization. The app leverages Groq's LLM API to generate professional resumes and provides options to view, copy, edit, and download resumes as PDF.

**Live Demo:** [https://ai-resume-builder-ugjj.onrender.com/](https://ai-resume-builder-ugjj.onrender.com/)

## Features

- **AI-Powered Resume Generation:** Uses Groq's LLM to create resumes optimized for job descriptions.
- **Template Selection:** Choose from multiple professional resume templates.
- **Resume Upload:** Upload your existing resume in `.pdf`, `.docx`, `.txt`, or `.md` formats for AI-powered enhancement.
- **PDF Download:** Download your generated resume as a PDF.
- **Copy & Edit:** Easily copy resume text or prepare for future editing features.

## Getting Started

### Prerequisites

- Python 3.12+
- Groq API key set as environment variable (`GROQ_API_KEY`)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/AI-Resume-Builder.git
    cd AI-Resume-Builder
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv resume
    .\resume\Scripts\activate
    ```

3. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set your Groq API key:
    ```sh
    set GROQ_API_KEY=your_api_key
    ```

### Running the App

```sh
python app.py
```

Visit [http://localhost:5000](http://localhost:5000) in your browser.

## Project Structure

- `app.py` - Main Flask application.
- `resume_builder.py` - Resume generation logic.
- `groq_client.py` - Groq API integration.
- `config.py` - Configuration and prompt templates.
- `utils.py` - Utility functions for file/template loading.
- `templates/` - HTML and Markdown resume templates.
- `static/` - Static files (CSS, images, generated resumes).
- `uploads/` - Uploaded resumes.

## Customization

- Add new resume templates in `templates/` as Markdown files.
- Update styles in `static/styles.css`.

## License

MIT License

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Groq](https://groq.com/)
- [ReportLab](https://www.reportlab.com/)

