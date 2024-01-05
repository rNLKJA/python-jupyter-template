# logger.py
import logging
import os

# Create logs directory if it doesn't exist
log_dir = 'logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Configure logging
log_format = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(
    level=logging.DEBUG,  # Capture all levels of log messages
    format=log_format,
    handlers=[
        logging.FileHandler(f"{log_dir}/app.log"),  # Log to a file
        logging.StreamHandler()  # Log to standard output
    ]
)

logger = logging.getLogger(__name__)

# Usage Example:
# logger.debug("This is a debug message")
# logger.info("This is an info message")
# logger.warning("This is a warning message")
# logger.error("This is an error message")
# logger.critical("This is a critical message")
