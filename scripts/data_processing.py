# scripts/data_processing.py
import sys
from src.logger import logger  # Assuming you have a logger configured in your src

def process_data(file_path):
    logger.info(f"Processing data from {file_path}")
    # Your data processing logic here

if __name__ == "__main__":
    if len(sys.argv) < 2:
        logger.error("Please provide a file path.")
    else:
        process_data(sys.argv[1])
