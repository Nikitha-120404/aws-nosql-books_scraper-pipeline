📚 AWS NoSQL Books Data Pipeline (Web Scraping + DocumentDB + DynamoDB)

📌 Project Overview

This project demonstrates a complete end-to-end NoSQL data pipeline on AWS using web-scraped book data.

The pipeline extracts book information from a public website, stores raw unstructured data in Amazon DocumentDB, transforms and cleans the data using Python, and loads the processed records into Amazon DynamoDB for scalable NoSQL storage.

This project reflects real-world data engineering practices, including web scraping, NoSQL data modeling, data transformation, and cloud-based database integration using AWS services.

🎯 Project Objective

To build a cloud-based NoSQL data pipeline that:

Scrapes book data from the web using Python

Stores raw data in Amazon DocumentDB

Cleans and transforms unstructured data

Loads structured data into Amazon DynamoDB

Validates stored data using terminal-based queries

🛠️ Technologies Used

Programming Language: Python

Web Scraping: Requests, BeautifulSoup

AWS Services:

Amazon DocumentDB

Amazon DynamoDB

AWS SDK: AWS SDK for Python (boto3)

Database Client: pymongo

Infrastructure Access: PuTTY / SSH

Data Format: JSON

🔄 Data Pipeline Architecture

Extract book data from a public website using web scraping

Store raw scraped data as JSON documents in Amazon DocumentDB

Read raw data from DocumentDB

Transform data:

Clean price values

Convert ratings from text to numeric

Add ingestion timestamps

Load transformed records into Amazon DynamoDB

Validate data using DocumentDB queries via terminal

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

⚙️ Implementation Details
🔹 Web Scraping & Raw Data Storage

Scrapes book title, price, stock availability, rating, and image URL

Stores raw data in Amazon DocumentDB using secure TLS connections

🔹 Data Transformation

Cleans currency symbols from prices

Converts rating values from text to numeric form

Adds ingestion timestamps for tracking

🔹 NoSQL Data Loading

Inserts transformed data into Amazon DynamoDB using boto3

Ensures scalable and efficient NoSQL storage

▶️ How to Run the Project
Prerequisites

Python 3.x

AWS account

Amazon DocumentDB cluster

Amazon DynamoDB table

AWS credentials configured

TLS certificate for DocumentDB

Install Dependencies
pip install -r requirements.txt

Execute Pipeline
# Scrape and store data in DocumentDB
python scrape_to_docdb.py

# Transform data and load into DynamoDB
python transform_and_loadto_dynamodb.py

# View sample data from DocumentDB
python viewdata_in_docdb.py

🔐 Security Considerations

Sensitive information such as:

AWS credentials

Database usernames and passwords

TLS certificates

are not included in this repository and should be managed securely using environment variables or configuration files excluded via .gitignore.

📊 Project Outcomes

Successfully scraped and stored book data in Amazon DocumentDB

Transformed unstructured data into structured format

Loaded cleaned data into Amazon DynamoDB

Verified data using terminal-based queries

🚀 Future Enhancements

Add pagination to scrape multiple pages

Automate pipeline using AWS Lambda

Add logging and error handling

Integrate analytics using AWS Athena or QuickSight

Schedule pipeline execution with Amazon EventBridge

👩‍💻 Author

Siva Nikitha 
Aspiring Data Engineer | AWS | Python | NoSQL | Data Pipelines
