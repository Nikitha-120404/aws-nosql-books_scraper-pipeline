"""
File Name: transform_and_loadto_dynamodb.py

Description:
This script reads raw book data stored in Amazon DocumentDB, performs data
cleaning and transformation, and loads the processed records into Amazon
DynamoDB.

Key Operations:
- Connects securely to Amazon DocumentDB using TLS
- Reads raw book documents
- Cleans price values and converts ratings to numeric format
- Adds ingestion timestamps
- Inserts transformed records into Amazon DynamoDB using AWS SDK (boto3)

This script is part of an end-to-end AWS NoSQL data pipeline.
"""
import os
import boto3  # AWS SDK for Python (to interact with AWS services like DynamoDB)
from pymongo import MongoClient  # Import MongoClient to connect and interact with DocumentDB (MongoDB-compatible)
import uuid  # For generating unique IDs
import re  # For text cleaning (e.g., removing symbols like £)
from datetime import datetime  # For adding timestamps
from decimal import Decimal  # For storing currency properly in DynamoDB
from dotenv import load_dotenv  # Load environment variables

# ---------------- CONFIG SECTION --------------------
# Load environment variables from .env file
load_dotenv()

DOCUMENTDB_USERNAME = os.getenv("DOCUMENTDB_USERNAME")  # Username to connect to DocumentDB
DOCUMENTDB_PASSWORD = os.getenv("DOCUMENTDB_PASSWORD")  # Password to connect to DocumentDB
DOCUMENTDB_CLUSTER_ENDPOINT = os.getenv("DOCUMENTDB_CLUSTER_ENDPOINT")  # DocumentDB cluster endpoint
DOCUMENTDB_PORT = 27017  # Default MongoDB port
CA_CERTIFICATE_PATH = "./global-bundle.pem"  # Certificate path for secure connection
DATABASE_NAME = "booksdb"  # Database name in DocumentDB
COLLECTION_NAME = "books"  # Collection name in DocumentDB

DYNAMODB_TABLE_NAME = os.getenv("DYNAMODB_TABLE_NAME", "dynamo2025")  # DynamoDB table name
AWS_REGION = os.getenv("AWS_REGION", "us-east-2")  # AWS Region where DynamoDB table is located
# ----------------------------------------------------

# Connect to DocumentDB
docdb_client = MongoClient(
    f"mongodb://{DOCUMENTDB_USERNAME}:{DOCUMENTDB_PASSWORD}@{DOCUMENTDB_CLUSTER_ENDPOINT}:{DOCUMENTDB_PORT}/?tls=true&tlsCAFile={CA_CERTIFICATE_PATH}"
)  # Establish secure connection to DocumentDB

docdb_db = docdb_client[DATABASE_NAME]  # Access the specific database
docdb_collection = docdb_db[COLLECTION_NAME]  # Access the specific collection
print("Connected to DocumentDB!")  # Confirmation message

# Connect to DynamoDB
dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION)  # Connect to DynamoDB service
dynamo_table = dynamodb.Table(DYNAMODB_TABLE_NAME)  # Specify the DynamoDB table to use
print("Connected to DynamoDB!")  # Confirmation message

# Helper function to clean price field
def clean_price(price_str):
    price_num = re.sub(r'[^0-9\.]', '', price_str)  # Remove £ symbol
    return Decimal(price_num)  # Convert price string to Decimal type (DynamoDB expects Decimal, not float)

# Helper function to convert rating from text (like "Three") to numeric (like 3)
def rating_to_number(rating_str):
    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    return rating_map.get(rating_str, 0)  # Return 0 if rating text not found

# Initialize counter to track successful migrations
books_migrated = 0

# Loop over each book document in DocumentDB
for full_doc in docdb_collection.find():
    try:
        # Prepare the transformed document for DynamoDB
        transformed_doc = {
            "books_id": str(uuid.uuid4()),  # Generate a unique ID for DynamoDB item
            "title": full_doc.get("title", "Unknown Title"),  # Get book title
            "price": clean_price(full_doc.get("price", "£0.00")),  # Clean and convert price
            "stock": full_doc.get("stock", "Unknown"),  # Stock status
            "rating": rating_to_number(full_doc.get("rating", "Zero")),  # Convert rating to number
            "ingestion_time": datetime.utcnow().isoformat()  # Add ingestion timestamp
        }

        # Insert the transformed document into DynamoDB
        dynamo_table.put_item(Item=transformed_doc)
        books_migrated += 1  # Increment counter if insertion successful

    except Exception as e:
        print(f"Error processing document: {e}")  # Print error if any during transformation or insertion

# Final message
print(f"\nSuccessfully migrated {books_migrated} books into DynamoDB after transformation!")
