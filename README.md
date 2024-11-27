# Web Address Scraper
A Python-based web scraper designed to extract addresses from websites. This project uses `requests` and `BeautifulSoup` for HTML fetching and parsing, 
along with a SQLite database for storing the extracted data.
---

## Features

- **HTML Fetching**: Retrieves web page content using `requests` with user-agent rotation.
- **Address Parsing**: Extracts and standardizes address information using `BeautifulSoup` and regular expressions.
- **Data Storage**: Saves scraped addresses to a SQLite database for structured storage and easy querying.
- **Automation**: Supports task scheduling for periodic scraping.
- **Logging**: Tracks progress and errors in log files.
- **Unit Testing**: Includes comprehensive unit tests for all components.

---
## Requirements

Ensure you have Python 3.8 or later installed. Install the necessary dependencies using `requirements.txt`:

```bash
pip install -r requirements.txt
