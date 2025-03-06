import json
import logging
from extract import extract
from transform import transform
from load import load
from etl_logging import setup_logging

# Setup logging
setup_logging()

def run_etl():
    try:
        logging.info("🔄 Starting ETL Process")

        # Step 1: Extract data
        file_path = "C:\\Users\\mumer\\Documents\\MyProject\\data\\PropertyRecords.json"  # Adjust path if needed
        data = extract(file_path)
        logging.info(f"✅ Extraction Successful - {len(data)} records extracted.")

        # Step 2: Transform data
        transformed_data = transform(data)
        logging.info(f"✅ Transformation Complete - {len(transformed_data)} records transformed.")

        # Step 3: Load data
        load(transformed_data)
        logging.info("✅ Loading Complete - Data loaded into the database.")

        logging.info("🔚 ETL Pipeline Completed!")

    except Exception as e:
        logging.error(f"❌ ETL process failed: {e}")

# Run the ETL process
if __name__ == "__main__":
    run_etl()
