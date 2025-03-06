import logging
from extract import extract  # Assuming extract.py is in the same directory
from transform import transform  # Assuming transform.py is in the same directory
from load import load  # Assuming load.py is in the same directory

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def run_etl():
    logging.info("🔄 ETL Process Started")
    logging.info("🚀 Starting ETL Pipeline")

    file_path = "C:/Users/mumer/Documents/MyProject/data/PropertyRecords.json"  # Replace with actual file path

    # Extract
    logging.info("✅ Starting Extraction")
    data = extract(file_path)
    
    if data:
        # Transform
        logging.info("🔄 Starting Transformation")
        transformed_data = transform(data)
        
        if transformed_data:
            # Load
            logging.info("⚡ Starting Load")
            load(transformed_data)
        else:
            logging.error("❌ Transformation Failed")
    else:
        logging.error("❌ Extraction Failed")

    logging.info("🔚 ETL Pipeline Completed!")

if __name__ == "__main__":
    run_etl()
