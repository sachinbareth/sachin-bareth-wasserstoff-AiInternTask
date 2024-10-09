# PDF Summarization and Keyword Extraction Pipeline


PDF Summarization and Keyword Extraction Pipeline that processes PDFs, generates summaries, extracts keywords, and stores the data in MongoDB.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Project Structure](#project-structure)
5. [Configuration](#configuration)
6. [How it Works](#how-it-works)


## Features

- Ingest PDFs from a folder.
- Extract text from PDFs.
- Generate summaries.
- Extract domain-specific keywords.
- Store results in MongoDB.
- Concurrency support for faster processing.
- Export results as `summaries.json`.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pdf_pipeline.git

### **Usage**
Explain how to run the project:
```markdown
## Usage

1. Add your PDFs to the `data/sample_pdfs` folder.
2. Configure your MongoDB settings in the `config/config.json` file.
3. Run the project:
   ```bash
   python main.py
   ```


## Project Structure
```plaintext
PDF_PIPELINE/
├── config/                 # Configuration files (like MongoDB settings)
├── data/                   # Folder where PDFs are stored
├── logs/                   # Log files to track pipeline activity
├── output/                 # Summaries and keyword extraction output
├── src/                    # Source code files
├── Dockerfile              # Docker configuration for containerization
└── main.py                 # Main script to run the pipeline
```


## Configuration

The `config/config.json` file contains MongoDB settings. Make sure your MongoDB URI, database name, and collection name are correctly configured:
```json
{
    "mongodb_uri": "mongodb://localhost:27017/",
    "db_name": "pdf_summary_db",
    "collection_name": "pdfs"
}
```
## Docker Setup

To run this project in a Docker container, follow these steps:

1. Build the Docker image:
   ```bash
   docker build -t pdf_pipeline_project .
   ```

2. Run the Docker container:
   ```bash
   docker run pdf_pipeline_project
   ```

This will create a containerized version of the pipeline.


### **How It Works**
Explain the core functionality briefly:
```markdown
## How It Works

1. The pipeline scans the `data/sample_pdfs` folder for PDF files.
2. It extracts text from each PDF and processes it to generate summaries and keywords.
3. The results are stored in MongoDB and saved as `summaries.json`.
4. Concurrent processing is used to handle multiple PDFs at once for better performance.
