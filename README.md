📚 AWS NoSQL Books Data Pipeline

(Web Scraping → Amazon DocumentDB → Transformation → Amazon DynamoDB)

📌 Project Overview

This project implements an end-to-end AWS NoSQL data pipeline using Python.
Book data is scraped from a public website, stored as raw documents in Amazon DocumentDB, transformed and cleaned, and then loaded into Amazon DynamoDB for scalable NoSQL storage and querying.

The pipeline reflects a real-world data engineering workflow executed via terminal (PuTTY/SSH) in an AWS environment.

🎯 Key Features

Web scraping of book metadata using Python

Raw data storage in Amazon DocumentDB (MongoDB-compatible)

Data cleaning and transformation

Structured data ingestion into Amazon DynamoDB

Terminal-based validation and querying

Secure TLS-based database connections

🛠 Tech Stack

Programming Language: Python

Web Scraping: Requests, BeautifulSoup

AWS Services:

Amazon DocumentDB

Amazon DynamoDB

AWS SDK: AWS SDK for Python (boto3)

Database Client: pymongo

Infrastructure Access: PuTTY / SSH

Data Format: JSON

🔄 Data Pipeline Workflow

Scrape book data from a public website

Store raw scraped data in Amazon DocumentDB

Read data from DocumentDB

Transform and clean data:

Remove currency symbols from prices

Convert ratings from text to numeric values

Add ingestion timestamps

Load transformed records into Amazon DynamoDB

Validate data by querying DocumentDB via terminal

📂 Project Structure
aws-nosql-books-pipeline/
│
├── src/
│   ├── scrape_to_docdb.py
│   ├── transform_and_loadto_dynamodb.py
│   └── viewdata_in_docdb.py
│
├── docs/
│   ├── putty_commands.md
│   └── documentdb_commands.md
│
├── outputs/
│   └── screenshots/
│
├── README.md
├── requirements.txt
└── .gitignore

📜 Script Description
1️⃣ scrape_to_docdb.py

Scrapes book title, price, stock status, rating, and image URL

Connects securely to Amazon DocumentDB using TLS

Inserts raw book documents into DocumentDB

2️⃣ transform_and_loadto_dynamodb.py

Reads raw data from DocumentDB

Cleans and transforms data:

Price → numeric (Decimal)

Rating → integer (1–5)

Adds ingestion timestamp

Loads transformed records into Amazon DynamoDB using boto3

3️⃣ viewdata_in_docdb.py

Connects to Amazon DocumentDB

Retrieves and displays sample records

Used for data validation and verification

⚙️ How to Run the Project
Prerequisites

Python 3.x

AWS Account

Amazon DocumentDB cluster

Amazon DynamoDB table

AWS credentials configured

TLS certificate (global-bundle.pem)

Install Dependencies
pip install -r requirements.txt

Run the Pipeline
# Step 1: Scrape and store data in DocumentDB
python scrape_to_docdb.py

# Step 2: Transform and load data into DynamoDB
python transform_and_loadto_dynamodb.py

# Step 3: View stored data from DocumentDB
python viewdata_in_docdb.py

🔐 Security Note

⚠️ Sensitive credentials are not included in this repository.
All secrets such as:

AWS credentials

Database usernames/passwords

TLS certificates

should be stored securely using environment variables or configuration files and excluded via .gitignore.

📸 Results

Successfully scraped book data from the web

Raw data stored in Amazon DocumentDB

Cleaned and transformed data loaded into Amazon DynamoDB

Data verified through terminal-based queries

(Screenshots available in the outputs/screenshots/ directory)

🚀 Future Enhancements

Automate pipeline using AWS Lambda

Add pagination for scraping multiple pages

Implement error logging and retry mechanisms

Add data analytics using Athena or QuickSight

Schedule pipeline with Amazon EventBridge

👩‍💻 Author

Nikitha (Nikki)
Aspiring Data Engineer | AWS | Python | NoSQL | Data Pipelines
