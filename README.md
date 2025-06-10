# Daily Income Calculator (CLI + Web Scraper)

This is a command-line tool designed to help you calculate daily income using custom currency inputs. It includes:

- Live currency symbol scraping from xe.com using Selenium
- Validation for amounts, rates, and symbols
- 13-day ahead date calculation
- Simple terminal-based interface with tabulated results

## Features

- Scrapes a list of valid currency codes
- Saves the list to a file (`currencies.txt`)
- Validates user input for amount, symbol, and exchange rate
- Calculates and displays total and per-night income
- Uses `tabulate` for a clean table display

## How to Run

1. Make sure you have Python installed (3.7+ recommended).
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Run the program:  
   ```bash
   python main.py
   ```

## Dependencies

- `selenium`
- `tabulate`

## Author

Daniel Kazemian
