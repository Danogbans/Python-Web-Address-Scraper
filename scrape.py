import os
import sqlite3
import requests
from bs4 import BeautifulSoup
import re
import random
import logging #The logging module is used to set up a system for tracking events that occur while a program runs.
from datetime import datetime
import time



# Configuration
websites = [
    {
        "url": "", 
        "address_selector":  ""
    }
]


# #This function sets up the environment by creating necessary directories and configuring logging.
def setup_environment():
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(filename="logs/scraper.log", level=logging.INFO)
    

#This function sets up an SQLite database to store the address data scraped from websites.
def setup_database():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect("data/addresses.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS addresses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            street_type TEXT,
            street_name TEXT,
            building_number TEXT,
            postal_code TEXT,
            city TEXT,
            province TEXT,
            country TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print("Database and table setup complete.")



# This function is designed to retrieve the HTML content of a given URL using HTTP requests. 
# It includes logic for selecting a random user agent, handling potential request errors, 
# and logging any issues encountered during the request.
def fetch_html(url):
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) Gecko/20100101 Firefox/45.0"
    ] # user_agents strings mimic real browsers (Chrome, Safari, and Firefox) on different operating systems.

    headers = {"User-Agent": random.choice(user_agents)}
    for _ in range(3):
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            logging.error(f"Error fetching {url}: {e}")
            time.sleep(5)
    return None


# Parsing HTML and Extracting Addresses
def parse_addresses(html, selector):
    soup = BeautifulSoup(html, 'html.parser')
    address_elements = soup.select(selector)
    addresses = []
    for element in address_elements:
        raw_address = element.get_text().strip()
        cleaned_address = clean_address(raw_address)
        print(f"Raw Address: {raw_address}") 
        if cleaned_address:
            addresses.append(cleaned_address)
        if not addresses:
            logging.info(f"No addresses found on {site['url']}")
    return addresses


# Utility Function: Cleaning and Standardizing Addresses
def clean_address(raw_address):
    pattern = r'(Calle|Avenida|Paseo|Plaza|Camino|Carrera|Ronda) (\w+( \w+)*?) (\d+), (\d{5}) (\w+( \w+)*)(, (\w+( \w+)*))?'
    match = re.search(pattern, raw_address)
    if match:
        return {
            "street_type": match.group(1),
            "street_name": match.group(2),
            "building_number": match.group(4),
            "postal_code": match.group(5),
            "city": match.group(6),
            "province": match.group(9)
        }
    return None


# Database Operations
def save_address_to_db(address):
    try:
        conn = sqlite3.connect("data/addresses.db")
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO addresses (street_type, street_name, building_number, postal_code, city, province, country)
            VALUES (?, ?, ?, ?, ?,?,?)
        ''', (address["street_type"], address["street_name"], address["building_number"], address["postal_code"], address["city"], address["province"], "Spain"))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()


# Automation: Schedule Tasks
def schedule_task(task_func, interval=86400):
    while True:
        logging.info(f"Running task at {datetime.now()}")
        task_func()
        logging.info(f"Task completed at {datetime.now()}")
        time.sleep(interval)


# Main Script to Run Scraping Process.
def main():
    setup_environment()
    setup_database()
    schedule_task(main, interval=86400)
    for site in websites:
        html = fetch_html(site['url']) 
        print(html)
        if html:
            addresses = parse_addresses(html, site['address_selector']) 
            for address in addresses:
                print(address)
                print(f"Inserting into database: {address}")
                save_address_to_db(address)




if __name__ == "__main__":
    main()
