from src.pdf_processor import process_pdfs
from src.db_manager import connect_db, get_all_documents  # Include get_all_documents for JSON export
from src.logger import setup_logger  # Make sure this import is included
import json

def save_to_json(db, output_file):
    # Get all documents (summaries and keywords) from MongoDB
    documents = get_all_documents(db)
    
    # Save the documents to a JSON file
    with open(output_file, 'w') as json_file:
        json.dump(documents, json_file, indent=4)

def main():
    logger = setup_logger()
    try:
        # Load configuration
        with open('config/config.json') as config_file:
            config = json.load(config_file)

        # Connect to MongoDB
        db = connect_db(config['mongodb_uri'], config['db_name'], config['collection_name'])

        # Print confirmation of database connection
        print("Successfully connected to MongoDB!")

        # Process PDFs and store results
        print("Processing PDFs...")
        process_pdfs('data/sample_pdfs', db)

        # Save the MongoDB records to a JSON file
        output_file = 'output/summaries.json'
        print(f"Saving summaries and keywords to {output_file}...")
        save_to_json(db, output_file)
        print(f"Data saved to {output_file} successfully!")

    except Exception as e:
        logger.error(f"Error in pipeline: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    main()


