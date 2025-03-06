# etl_logging.py - Logging Setup
import logging
from config import LOG_FILE

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_message(message, level="info"):
    """Log messages to the file"""
    if level == "info":
        logging.info(message)
    elif level == "error":
        logging.error(message)
    elif level == "warning":
        logging.warning(message)

log_message("🔄 ETL Process Started", "info")
