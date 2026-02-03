"""
File Name: viewdata_in_docdb.py

Description:
This script connects securely to Amazon DocumentDB and retrieves
sample book records for validation and inspection.

Key Operations:
- Establishes a TLS-secured connection to Amazon DocumentDB
- Fetches documents from the books collection
- Displays a limited number of records in the terminal

This script is used for data verification in the AWS NoSQL Books Data Pipeline.
"""

import os
from pymongo import MongoClient  # MongoDB / DocumentDB client
from dotenv import load_dotenv  # Load environment variables

# ---------------- CONFIG SECTION --------------------
# Load environment variables from .env file
load_dotenv()

DOCUMENTDB_USERNAME = os.getenv("DOCUMENTDB_USERNAME")  # DocumentDB username
DOCUMENTDB_PASSWORD = os.getenv("DOCUMENTDB_PASSWORD")  # DocumentDB password
DOCUMENTDB_CLUSTER_ENDPOINT = os.getenv("DOCUMENTDB_CLUSTER_ENDPOINT")  # DocumentDB endpoint
DOCUMENTDB_PORT = 27017  # Standard MongoDB/DocumentDB port
CA_CERTIFICATE_PATH = "./global-bundle.pem"  # TLS certificate path
DATABASE_NAME = "booksdb"  # Database name
COLLECTION_NAME = "books"  # Collection name
# ----------------------------------------------------

# 1. Connect to DocumentDB
client = MongoClient(
    f"mongodb://{DOCUMENTDB_USERNAME}:{DOCUMENTDB_PASSWORD}@{DOCUMENTDB_CLUSTER_ENDPOINT}:{DOCUMENTDB_PORT}/"
    f"?tls=true&tlsCAFile={CA_CERTIFICATE_PATH}"
)

db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

print("Connected to DocumentDB!")

# 2. Fetch and display documents
print("\nBooks data from DocumentDB (sample records):\n")

# Retrieve and print first 10 documents
for book in collection.find().limit(10):
    print(book)

print("\nData extracted successfully!")
