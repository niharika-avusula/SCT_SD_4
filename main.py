# Task 4 - Web Scraper for Product Information
# Extracts Product Name, Price, and Rating from Books to Scrape
# Saves the extracted data into a CSV file

import requests
from bs4 import BeautifulSoup
import csv
import os

# List to store all product data
products = []

# Scrape first 5 pages (100 books)
for page in range(1, 6):

    # Generate page URL
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    # Send request to website
    response = requests.get(url)

    # Parse HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all book containers
    books = soup.find_all("article", class_="product_pod")

    # Extract information from each book
    for book in books:

        # Get book name
        name = book.h3.a["title"]

        # Get price
        price = book.find("p", class_="price_color").text

        # Get rating (One, Two, Three, Four, Five)
        rating = book.find("p")["class"][1]

        # Store data in list
        products.append([name, price, rating])
print("Products collected:", len(products))        

# Create CSV file
with open("products.csv", "w", newline="", encoding="utf-8") as file:

    writer = csv.writer(file)

    # Write column headers
    writer.writerow(["Product Name", "Price", "Rating"])

    # Write product data
    writer.writerows(products)
    print("Products collected:", len(products))

# Success message
print("Data extracted successfully!")
print(f"Total Products Scraped: {len(products)}")
print("CSV File Created: products.csv")

# Display file location
print("\nFile saved at:")
print(os.path.abspath("products.csv"))