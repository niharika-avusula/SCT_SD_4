# SCT_SD_4 - E-Commerce Product Data Scraper

## Description

This project is a Python-based web scraping application that extracts product information from an online e-commerce website and stores the data in a structured CSV file.

The program collects:

- Product Name
- Product Price
- Product Rating

and saves the extracted data into `products.csv` for further analysis.

## Website Used

Books to Scrape: https://books.toscrape.com/

This website is designed for practicing web scraping techniques.

## Features

- Extracts product names
- Extracts product prices
- Extracts product ratings
- Scrapes multiple pages automatically
- Stores data in CSV format
- Displays total products scraped
- Shows the location of the generated CSV file

## Technologies Used

- Python
- Requests
- BeautifulSoup
- CSV Module

## How It Works

1. Connects to the website.
2. Downloads the HTML content.
3. Parses the webpage using BeautifulSoup.
4. Extracts product information:
   - Name
   - Price
   - Rating
5. Stores the extracted data in a list.
6. Writes the data to a CSV file.
7. Displays a success message.

## Project Structure

```text
SCT_SD_4/
│
├── main.py
├── products.csv
└── README.md
```

## Sample Output

| Product Name         |  Price | Rating|
|----------------------|----------------|
| A Light in the Attic | £51.77 | Three |
| Tipping the Velvet   | £53.74 | One   |
| Soumission           | £50.10 | One   |

## Concepts Used

- Web Scraping
- HTTP Requests
- HTML Parsing
- BeautifulSoup
- Loops
- Lists
- CSV File Handling
- Data Extraction

## Applications

- Price Comparison
- Market Research
- Competitor Analysis
- Product Data Collection
- Business Reporting

## Learning Outcomes

Through this project, I learned:

- How web scraping works
- How to extract data from websites
- HTML parsing using BeautifulSoup
- CSV file creation and management
- Data collection automation
- Python libraries for web scraping

## Author

**Niharika Avusula**

GitHub: `niharika-avusula`