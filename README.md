## Web Address Scraper

A Python-based web scraper designed to extract addresses from websites. This project uses `requests` and `BeautifulSoup` for HTML fetching and parsing, 
along with a SQLite database for storing the extracted data.
---

## Features

- **HTML Fetching**: Retrieves web page content using `requests` with user-agent rotation.
- **Address Parsing**: Extracts and standardizes address information using `BeautifulSoup` and regular expressions.
- **Data Storage**: Saves scraped addresses to a SQLite database for structured storage and easy querying.
- **Automation**: Supports task scheduling for periodic scraping.
- **Logging**: Tracks progress and errors in log files.
  

---
## Requirements

Ensure you have Python 3.8 or later installed. Install the necessary dependencies using `requirements.txt`:

```bash
pip install -r requirements.txt
```
## Dependencies
```bash
beautifulsoup4==4.12.2
requests==2.31.0
lxml==4.9.3
```
## Project Structure
```bash
SCRAPER/
├── scrape.py          # Main script to run the scraping process
├── requirements.txt     # Project dependencies
├── logs/                # Directory for log files
├── data/                # Directory for data storage
└── .gitignore           
```
## Setup
- Create a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
- Install dependencies:
```bash
pip install -r requirements.txt
``` 
- Initialize the project:
 ```bash
python scrape.py
``` 
## Usage
- Simply execute the scraper.py script to fetch, parse, and store addresses:
```bash
python scrape.py
``` 
