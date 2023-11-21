from database_utils import DatabaseConnector
from data_cleaning import DataCleaning
from data_extraction import DataExtractor


if __name__ == '__main__':
    # Step 1: Extract Data
    extractor = DataExtractor()
    df_extracted = extractor.extract_from_s3()

    # # Step 2: Clean Data
    cleaner = DataCleaning()
    df_converted = cleaner.convert_product_weights(df_extracted)
    df_cleaned = cleaner.clean_products_data(df_converted)

    # Step 3: Upload Cleaned Data
    # Assuming DatabaseConnector can connect to 'sales_data' database
    db_connector_product_data = DatabaseConnector('../config/pgadmin_creds.yaml')
    db_connector_product_data.upload_to_db(df_cleaned, 'dim_products')

    print("Data extraction, cleaning, and uploading process completed.")
