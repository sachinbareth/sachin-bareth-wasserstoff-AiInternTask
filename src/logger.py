import logging
import os

def setup_logger():
    # Set the log file path
    log_dir = 'logs'
    log_path = os.path.join(log_dir, 'pdf_pipeline.log')

    # Ensure the logs directory exists
    if not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)

    # Set up logging to the file
    logging.basicConfig(filename=log_path, level=logging.ERROR)
    return logging.getLogger()
