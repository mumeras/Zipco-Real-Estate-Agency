import logging
from datetime import datetime

def transform(data):
    cleaned_data = []
    for record in data:
        try:
            # Clean the data (e.g., handle missing values, format date, etc.)
            if not record.get('lastSaleDate'):
                record['lastSaleDate'] = None
            else:
                try:
                    # Convert string to date if it's not already in the correct format
                    record['lastSaleDate'] = datetime.strptime(record['lastSaleDate'], "%Y-%m-%dT%H:%M:%S.%fZ")
                except ValueError:
                    record['lastSaleDate'] = None

            # Check if critical fields are missing or invalid and clean them
            if not record.get('county') or not record.get('propertyType'):
                continue  # Skip this record if it's missing critical info

            cleaned_data.append(record)

        except Exception as e:
            logging.error(f"❌ Error transforming record: {e}")
    
    return cleaned_data
