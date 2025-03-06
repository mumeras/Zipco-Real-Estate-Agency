import logging
from datetime import datetime

def transform(data):
    cleaned_data = []

    for record in data:
        try:
            # 1. Handle missing values for simple fields
            if not record.get("county"):
                record["county"] = "Unknown"
            
            if not record.get("propertyType"):
                record["propertyType"] = "Unknown"

            # 2. Validate and clean date format
            if record.get("lastSaleDate"):
                try:
                    # Ensure the date is in the correct format
                    record["lastSaleDate"] = datetime.strptime(record["lastSaleDate"], "%Y-%m-%dT%H:%M:%S.%fZ").date()
                except ValueError:
                    record["lastSaleDate"] = None  # Set to None if invalid date
            else:
                record["lastSaleDate"] = None

            # 3. Clean numerical data
            if not isinstance(record.get("bedrooms", 0), int) or record["bedrooms"] < 0:
                record["bedrooms"] = None  # Invalid value for bedrooms
            if not isinstance(record.get("bathrooms", 0), int) or record["bathrooms"] < 0:
                record["bathrooms"] = None  # Invalid value for bathrooms
            if not isinstance(record.get("squareFootage", 0), (int, float)) or record["squareFootage"] < 0:
                record["squareFootage"] = None  # Invalid value for square footage
            if not isinstance(record.get("lotSize", 0), (int, float)) or record["lotSize"] < 0:
                record["lotSize"] = None  # Invalid value for lot size
            if not isinstance(record.get("yearBuilt", 0), int) or record["yearBuilt"] < 0:
                record["yearBuilt"] = None  # Invalid value for year built
            if not isinstance(record.get("lastSalePrice", 0), (int, float)) or record["lastSalePrice"] < 0:
                record["lastSalePrice"] = None  # Invalid value for sale price

            # 4. Clean address data
            record["addressLine1"] = record.get("addressLine1", "").strip()
            record["city"] = record.get("city", "").strip()
            record["state"] = record.get("state", "").strip()
            record["zipCode"] = str(record.get("zipCode", "")).strip()

            # 5. Clean owner data and address
            record["ownerAddress"] = ""
            if record.get("owner"):
                record["ownerAddress"] = record["owner"].get("mailingAddress", {}).get("addressLine1", "")

            # 6. Remove duplicates or records with critical missing data (e.g., address)
            if not record.get("addressLine1") or not record.get("city") or not record.get("state") or not record.get("zipCode"):
                continue  # Skip this record if crucial address info is missing

            # 7. Format the address to make it more readable (you can customize this)
            record["formattedAddress"] = f"{record['addressLine1']}, {record['city']}, {record['state']} {record['zipCode']}"

            # Add cleaned record to the list
            cleaned_data.append(record)

        except Exception as e:
            logging.error(f"Error during transformation: {e}")

    return cleaned_data
