import psycopg2
import logging

def load(transformed_data):
    conn = None
    cursor = None
    
    try:
        # Establish PostgreSQL connection
        conn = psycopg2.connect(
            dbname="real_estate",  # Replace with your database name
            user="etl_user",  # Replace with your username
            password="Password@1",  # Replace with your password
            host="localhost",  # Assuming local PostgreSQL server
            port=5432  # Default PostgreSQL port
        )
        cursor = conn.cursor()

        # Log the structure of the transformed_data to confirm the data structure
        logging.info(f"Transformed Data Structure: {transformed_data}")

        # Ensure transformed_data is a list (list of records)
        if isinstance(transformed_data, list):
            for record in transformed_data:
                logging.info(f"Processing record: {record}")  # Log each record being processed
                
                # Insert into the addresses table
                cursor.execute("""
                    INSERT INTO addresses (addressLine1, city, state, zipCode)
                    VALUES (%s, %s, %s, %s)
                """, (record.get('addressLine1', ''), record.get('city', ''), 
                      record.get('state', ''), record.get('zipCode', '')))

                # Insert into the property_sales table
                cursor.execute("""
                    INSERT INTO property_sales (salePrice, saleDate)
                    VALUES (%s, %s)
                """, (record.get('lastSalePrice', 0), record.get('lastSaleDate', '')))

                # Insert into the owners table
                cursor.execute("""
                    INSERT INTO owners (ownerName, ownerAddress)
                    VALUES (%s, %s)
                """, (record.get('ownerName', ''), record.get('ownerAddress', '')))

                # Insert into the properties table
                cursor.execute("""
                    INSERT INTO dim_properties (county, propertyType, bedrooms, bathrooms, squareFootage, lotSize, yearBuilt, formattedAddress)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, (record.get('county', ''), record.get('propertyType', ''), 
                      record.get('bedrooms', 0), record.get('bathrooms', 0), 
                      record.get('squareFootage', 0), record.get('lotSize', 0), 
                      record.get('yearBuilt', 0), record.get('formattedAddress', '')))

            # Commit the transaction
            conn.commit()
            logging.info("Data successfully loaded into the database.")

        else:
            logging.error("Error: Transformed data is not a list as expected")

    except Exception as e:
        logging.error(f"Error during load: {e}")
        if conn:
            conn.rollback()

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()
