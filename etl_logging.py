import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler("etl_process.log", encoding='utf-8'), logging.StreamHandler()]
    )

def log_error(e):
    logging.error(f"❌ Error during load: {e}")
