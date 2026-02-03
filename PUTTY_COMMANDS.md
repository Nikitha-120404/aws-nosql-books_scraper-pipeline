# PuTTY Commands – AWS NoSQL Books Pipeline

This file documents the PuTTY (SSH) commands used to execute and validate
the AWS NoSQL Books Data Pipeline on an EC2 instance.

---

## 🔹 Connect to EC2

```text
ubuntu@<EC2_PUBLIC_IP>
Port: 22
Auth: .ppk key file

🔹 Navigate to Project
cd aws-nosql-books-scraper-pipeline/src
🔹 Activate Virtual Environment
source myenv/bin/activate
🔹 Install Dependencies
pip install -r requirements.txt
🔹 Run Pipeline Scripts
Scrape data into DocumentDB
python3 scrape_to_docdb.py
Transform & load into DynamoDB
python3 transform_and_loadto_dynamodb.py
🔹 Validate DocumentDB (Optional)
db.books.find().limit(5)
🔹 Exit Environment
deactivate
