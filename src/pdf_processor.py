import os
from PyPDF2 import PdfReader
from concurrent.futures import ThreadPoolExecutor
from src.text_processor import summarize_text, extract_keywords
from src.db_manager import store_summary_and_keywords

# Function to extract text from a single PDF file
def extract_text_from_pdf(pdf_path):
    try:
        # Open the PDF file in binary mode
        with open(pdf_path, 'rb') as file:
            reader = PdfReader(file)  # Initialize the PDF reader
            text = ""  # Variable to store extracted text
            
            # Loop through each page in the PDF and extract text
            for page in reader.pages:
                text += page.extract_text()
                
        # Return the extracted text
        return text
    except Exception as e:
        # If any error occurs (like file corruption), return None
        return None

# Function to process all PDFs in a given folder, extract summaries and keywords, and store results in MongoDB
def process_pdfs(folder_path, db):
    # Get a list of all PDF files in the folder
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]
    
    # Create full paths for each PDF file
    pdf_paths = [os.path.join(folder_path, pdf) for pdf in pdf_files]

    # Use ThreadPoolExecutor to process multiple PDFs concurrently
    with ThreadPoolExecutor() as executor:
        for pdf_path in pdf_paths:
            # Extract text from each PDF
            text = extract_text_from_pdf(pdf_path)
            
            # If text was successfully extracted, proceed to summarization and keyword extraction
            if text:
                summary = summarize_text(text)  # Generate a summary of the extracted text
                keywords = extract_keywords(text)  # Extract relevant keywords from the text
                
                # Store the summary and keywords in the MongoDB database
                store_summary_and_keywords(db, pdf_path, summary, keywords)
