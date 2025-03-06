import psycopg2
import logging
import json

def load(transformed_data):
    try:
        conn = psycopg2.connect(
            dbname="real_estate",  # Replace with your database name
            user="etl_user",  # Replace with your username
            password="Password@1",  # Replace with your password
            host="localhost",  # Assuming local PostgreSQL server
            port=5432  # Default PostgreSQL port
        )
        cursor = conn.cursor()

        fact_properties_count = 0
        dim_property_sales_count = 0
        dim_owners_count = 0
        dim_addresses_count = 0
        dim_features_count = 0  # New count for dim_features

        # Insert into fact_properties table
        for record in transformed_data:
            cursor.execute("""
                INSERT INTO fact_properties (county, propertyType, bedrooms, bathrooms, squareFootage, lotSize, yearBuilt, formattedAddress, lastSaleDate)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (
                record.get('county', ''),
                record.get('propertyType', ''),
                record.get('bedrooms', 0),
                record.get('bathrooms', 0),
                record.get('squareFootage', 0),
                record.get('lotSize', 0),
                record.get('yearBuilt', 0),
                record.get('formattedAddress', ''),
                record.get('lastSaleDate')
            ))
            fact_properties_count += 1

            # Insert into dim_property_sales table
            cursor.execute("""
                INSERT INTO dim_property_sales (salePrice, saleDate)
                VALUES (%s, %s)
            """, (
                record.get('lastSalePrice', 0),
                record.get('lastSaleDate')
            ))
            dim_property_sales_count += 1

            # Insert into dim_owners table
            cursor.execute("""
                INSERT INTO dim_owners (ownerName, ownerAddress)
                VALUES (%s, %s)
            """, (
                record.get('ownerName', ''),
                record.get('ownerAddress', '')
            ))
            dim_owners_count += 1

            # Insert into dim_addresses table
            cursor.execute("""
                INSERT INTO dim_addresses (addressLine1, city, state, zipCode)
                VALUES (%s, %s, %s, %s)
            """, (
                record.get('addressLine1', ''),
                record.get('city', ''),
                record.get('state', ''),
                record.get('zipCode', '')
            ))
            dim_addresses_count += 1

            # Insert into dim_features table (with features serialized as JSON)
            features = record.get('features', {})
            features_json = json.dumps(features) if isinstance(features, dict) else str(features)  # Serialize dictionary to JSON string

            cursor.execute("""
                INSERT INTO dim_features (features, propertyType, zoning)
                VALUES (%s, %s, %s)
            """, (
                features_json,  # Insert the JSON string of features
                record.get('propertyType', ''),
                record.get('zoning', '')
            ))
            dim_features_count += 1

        # Commit the transaction
        conn.commit()

        # Log the results
        logging.info(f"✅ {fact_properties_count} rows inserted into fact_properties table.")
        logging.info(f"✅ {dim_property_sales_count} rows inserted into dim_property_sales table.")
        logging.info(f"✅ {dim_owners_count} rows inserted into dim_owners table.")
        logging.info(f"✅ {dim_addresses_count} rows inserted into dim_addresses table.")
        logging.info(f"✅ {dim_features_count} rows inserted into dim_features table.")  # Log for dim_features

    except Exception as e:
        logging.error(f"❌ Error during load: {e}")
    finally:
        cursor.close()
        conn.close()
