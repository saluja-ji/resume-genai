import PyPDF2
import docx2txt
import google.generativeai as genai
import nltk
from nltk.tokenize import word_tokenize
import os

# Download necessary NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

# Configure Gemini API
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEYS")
if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)
else:
    print("Warning: GOOGLE_API_KEY not found in environment variables.")
    genai = None  # Disable Gemini if API key is missing

def extract_text_from_document(file):
    """Extracts text from PDF or DOCX files."""
    try:
        if file.name.endswith(".pdf"):
            text = ""
            with open(file, "rb") as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    text += page.extract_text()
            return text
        elif file.name.endswith(".docx"):
            text = docx2txt.process(file)
            return text
        else:
            return "Unsupported file format."
    except Exception as e:
        return f"Error extracting text: {e}"

def generate_gemini_response(prompt):
    """Generates a response from the Gemini API."""
    if genai is None:
        return "Gemini API not configured.  Please set the GOOGLE_API_KEY environment variable."

    model = genai.GenerativeModel('gemini-pro')  # Or 'gemini-1.5-pro' if you have access
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating response from Gemini: {e}"

def extract_skills(resume_text):
    """Extracts skills from the resume text using Gemini."""
    prompt = prompts.SKILL_EXTRACTION_PROMPT.format(resume_text=resume_text)
    return generate_gemini_response(prompt)

def get_formatting_feedback(resume_text):
    """Gets formatting feedback from Gemini."""
    prompt = prompts.FORMATTING_FEEDBACK_PROMPT.format(resume_text=resume_text)
    return generate_gemini_response(prompt)

def get_content_suggestions(resume_text):
    """Gets content suggestions from Gemini."""
    prompt = prompts.CONTENT_SUGGESTION_PROMPT.format(resume_text=resume_text)
    return generate_gemini_response(prompt)

def analyze_keywords(resume_text, job_description):
    """Analyzes keywords in the resume and job description."""
    prompt = prompts.KEYWORD_ANALYSIS_PROMPT.format(resume_text=resume_text, job_description=job_description)
    return generate_gemini_response(prompt)
