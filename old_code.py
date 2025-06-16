from tabulate import tabulate
from selenium import webdriver
from typing import Tuple, List
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

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

        end: str = input("Do you want to continue? (yes or no or leave it empty if you wish yes)\n").strip().lower()
        if end == 'no':
            break

    result: float = sum(num_list)
    night: int = integer_checker("Enter number of night: ")
    income_per_night: float = result / night

    items: List[List[str]] = [
        [f"Total rate for {night} night", f"{result:,.8f} TRY", f"{result:,.2f} TRY"],
        [f"Per night", f"{income_per_night:,.8f} TRY", f"{income_per_night:,.2f} TRY"]
    ]
    headers: List[str] = ["Type", "Full Amount", "Rounded amount"]
    print("\n", tabulate(items, headers=headers, tablefmt="grid"), "\n")


def calculate_13_day_ahead() -> Tuple[str, str]:
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

# if __name__ == '__main__':
#     main()



# def load_calculator_page() -> None:
#     """
#     This function will load calculator page and show calculator.
#
#     Returns: Is none
#
#     """
#
#     page_reset()
#
#     screen: Text = Text(content_frame, height=10, width=250, bg='#ff6600', font=('TkFixFont', 10))
#     screen.config(state='disabled')
#     screen.pack(padx=30, pady=30)
#
#     # Add a Label which is "Amount"
#     Label(content_frame,
#           text="Amount:",
#           bg='#a3c3ff',
#           font=('Arial', 12, 'bold')).pack()
#     # Add an Entry which is for "Amount"
#     amount_entry: Entry = Entry(content_frame, font=('Arial', 11))
#     amount_entry.pack()
#
#     # Add a Label which is "Currency symbol"
#     Label(content_frame,
#           text="Currency symbol:",
#           bg='#a3c3ff',
#           font=('Arial', 12, 'bold')).pack()
#
#     # Add an Entry which is for "Currency symbol"
#     symbol_entry: Entry = Entry(content_frame, font=('Arial', 11))
#     symbol_entry.pack()
#
#     # Add a Label which is "Rate"
#     Label(content_frame,
#           text="Rate:",
#           bg='#a3c3ff',
#           font=('Arial', 12, 'bold')).pack()
#
#     # Add an Entry which is for "Rate"
#     rate_entry: Entry = Entry(content_frame, font=('Arial', 11))
#     rate_entry.pack()
#
#     # Add an "ADD" button for adding my numbers for calculation
#     add_button: Button = Button(content_frame,
#                                  text='Add',
#                                  bg="#08e966",
#                                  fg='black',
#                                  font=('Arial', 11, 'bold'),
#                                  width=10,
#                                  command=lambda: add(amount_entry, symbol_entry, rate_entry))
#     add_button.pack()
#     # Add a "Finish" button for saying done; which means there is no other input left to calculate
#     finish_button: Button = Button(content_frame,
#                                  text='Finish',
#                                  bg="#08e966",
#                                  fg='black',
#                                  font=('Arial', 11, 'bold'),
#                                  width=10,
#                                  command=finish)
#     finish_button.pack()
