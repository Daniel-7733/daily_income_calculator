from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from tkinter import Label, StringVar
from selenium import webdriver
from typing import List




currencies_txt: str = 'currencies.txt'


def web_scraper() -> None:
    # TODO: This function need to update currency symbol update each month. (But I need to keep the original information in case if the site change

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


def integer_checker(printable_name) -> int:
    while True:
        count: int = int(input(printable_name))
        try:
            return int(count)
        except ValueError:
            print(f"Enter {printable_name}!")


# Global list to hold income in TRY
num_list: List[float] = []

def add_amount(amount_var: StringVar, symbol_var: StringVar, rate_var: StringVar, result_label: Label) -> None:
    try:
        amount: float = float(amount_var.get())
        symbol: str = symbol_var.get().upper()
        rate: float = float(rate_var.get())

        if symbol == "TRY":
            num_list.append(amount) # TODO: This part need some changes because it doesn't need rate (rate is 1)
        else:
            result: float = amount * rate
            num_list.append(result)

        result_label.config(text=f"✅ Added: {num_list[-1]:,.2f} TRY", fg="green")
    except ValueError:
        result_label.config(text="⚠️ Please enter valid numbers", fg="red")


def calculate_total(nights_var: StringVar, total_label: Label) -> None:
    try:
        nights: int = int(nights_var.get())
        total: float = sum(num_list)
        per_night: float = total / nights
        total_label.config(
            text=f"Total: {total:,.2f} TRY\nPer Night: {per_night:,.2f} TRY", fg="blue"
        )
    except (ValueError, ZeroDivisionError):
        total_label.config(text="⚠️ Please enter a valid number of nights", fg="red")


# TODO: I need a function to save data and give PDF as a report at the end.
def report() -> None:
    raise NotImplementedError("report() Is not built yet")
