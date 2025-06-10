from datetime import datetime, timedelta
from typing import Tuple, List
from tabulate import tabulate
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


currencies_txt: str = 'currencies.txt'

def web_scraper() -> None:

    driver: webdriver = webdriver.Chrome()
    driver.get('https://www.xe.com/currency/')

    try:
        # Wait until currency list is visible (adjust selector as needed)
        currencies: List[WebElement] = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'currencyCode'))
        )
        
        with open(currencies_txt, 'w') as file:
            for currency in currencies:
                file.write(currency.text.replace(" -", "") + '\n')


    except Exception as e:
        print("❌ Error occurred:", e)

    finally:
        driver.quit()

def text_opener() -> List[str]:
    with open(currencies_txt, 'r') as file:
        currencies_list: List[str] = [line.split("\n")[0] for line in file]
    return currencies_list


def symbol_checker() -> str:
    symbol_list: List[str] = text_opener()
    
    while True:
        symbol: str = input("Symbol: ").strip().upper()    
        if symbol in symbol_list:
            return symbol
        else:
            print("❌ Invalid currency symbol. Please try again.")


def float_checker(printable_name: str) -> float:
    while True:
        number: str = input(printable_name)
        try:
            return float(number)
        except ValueError:
            print(f"Enter {printable_name}!")

def intager_checker(printable_name) -> int:
    while True:
        count: int = int(input(printable_name))
        try:
            return int(count)
        except ValueError:
            print(f"Enter {printable_name}!")


def calculator(escape_symbol: str) -> None:

    num_list: List[float] = []

    while True:
       
        amount: float = float_checker("Enter the amount: ")
        symbol: str = symbol_checker()
        
        if symbol == escape_symbol:
            num_list.append(amount)
        else:
            rate: float = float_checker("Enter the rate: ")
            result_in_lira: float = amount * rate
            num_list.append(result_in_lira)

        end: str = input("Do you want to countuinue? (yes or no or leave it empty if you wish yes)\n").strip().lower()
        if end == 'no':
            break

    result: float = sum(num_list)
    night: int = intager_checker("Enter number of night: ")
    income_per_night: float = result / night

    items: List[List[str]] = [
        [f"Total rate for {night} night", f"{result:,.8f} TRY", f"{result:,.2f} TRY"],
        [f"Per night", f"{income_per_night:,.8f} TRY", f"{income_per_night:,.2f} TRY"]
    ]
    headers: List[str] = ["Type", "Full Amount", "Rounded amount"]
    print("\n", tabulate(items, headers=headers, tablefmt="grid"), "\n")


def calculate_13_day_ahead() -> Tuple[str,str]:
    today: datetime = datetime.today()
    fourteen_days_ahead: datetime = today + timedelta(days=13)
    return today.strftime('%Y-%m-%d'), fourteen_days_ahead.strftime('%Y-%m-%d')


def main() -> None:

    while True:
        today, fourteen_days_ahead = calculate_13_day_ahead()
        print("\n", "Today:", today)
        print("14 days ahead:", fourteen_days_ahead, "\n")

        calculator("TRY")
        exit: str = input("Do you want to finish? (yes or no)").strip().upper()
        if exit == 'Yes':
            break

if __name__ == '__main__':
    main()