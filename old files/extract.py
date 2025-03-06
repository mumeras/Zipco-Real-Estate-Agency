import logging
import json

def extract(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            logging.info(f"✅ Extraction Successful - {len(data)} rows extracted.")
            return data
    except Exception as e:
        logging.error(f"Error during extraction: {e}")
        return None
