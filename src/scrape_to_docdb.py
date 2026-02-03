# ---------------- CONFIG SECTION --------------------
import os
import requests  # Library to send HTTP requests (to fetch webpage content)
from bs4 import BeautifulSoup  # Library to parse and extract data from HTML (web scraping)
from pymongo import MongoClient  # Library to connect to MongoDB or AWS DocumentDB
from dotenv import load_dotenv  # Load environment variables

# Load environment variables from .env file
load_dotenv()

# --- Database Connection Details ---
DOCUMENTDB_USERNAME = os.getenv("DOCUMENTDB_USERNAME")  # DocumentDB username
DOCUMENTDB_PASSWORD = os.getenv("DOCUMENTDB_PASSWORD")  # DocumentDB password
DOCUMENTDB_CLUSTER_ENDPOINT = os.getenv("DOCUMENTDB_CLUSTER_ENDPOINT")  # DocumentDB endpoint
DOCUMENTDB_PORT = 27017  # Default MongoDB/DocumentDB port
DATABASE_NAME = "booksdb"  # Database name
COLLECTION_NAME = "books"  # Collection name
CA_CERTIFICATE_PATH = "./global-bundle.pem"  # TLS certificate path

# --- Target Website for Scraping ---
BASE_URL = "http://books.toscrape.com/"
PAGE_URL = BASE_URL + "catalogue/page-1.html"

# ----------------------------------------------------

# 1. Connect to DocumentDB
client = MongoClient(
    f"mongodb://{DOCUMENTDB_USERNAME}:{DOCUMENTDB_PASSWORD}@{DOCUMENTDB_CLUSTER_ENDPOINT}:{DOCUMENTDB_PORT}/"
    f"?tls=true&tlsCAFile={CA_CERTIFICATE_PATH}"
)

db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

print("Connected to DocumentDB!")

# 2. Scrape data
response = requests.get(PAGE_URL)
soup = BeautifulSoup(response.content, "html.parser")
books_scraped = 0

# Loop through all book listings
for article in soup.find_all('article', class_='product_pod'):
    title = article.h3.a['title']
    price = article.find('p', class_='price_color').text
    stock = article.find('p', class_='instock availability').text.strip()
    rating = article.p['class'][1]
    image_rel_url = article.find('img')['src']
    image_url = BASE_URL + image_rel_url.replace('../', '')

    # Build document
    book_doc = {
        "title": title,
        "price": price,
        "stock": stock,
        "rating": rating,
        "image_url": image_url
    }

    # 3. Insert into DocumentDB
    collection.insert_one(book_doc)
    books_scraped += 1
  
print(f"Successfully scraped and saved {books_scraped} books into DocumentDB!")
