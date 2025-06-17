from tkinter import Tk, Label, Entry, Button, StringVar
from tkinter.ttk import Separator
from typing import List

num_list: List[float] = []

def add_amount(amount_var: StringVar, symbol_var: StringVar, rate_var: StringVar, result_label: Label) -> None:
    try:
        amount: float = float(amount_var.get())
        symbol: str = symbol_var.get().upper()
        rate: float = float(rate_var.get())

        if symbol == "TRY":
            num_list.append(amount)
        else:
            result: float = amount * rate
            num_list.append(result)

        result_label.config(text=f"✅ Added: {num_list[-1]:,.2f} TRY", fg="#006266")
    except ValueError:
        result_label.config(text="⚠️ Please enter valid numbers", fg="red")

def calculate_total(nights_var: StringVar, total_label: Label) -> None:
    try:
        nights: int = int(nights_var.get())
        total: float = sum(num_list)
        per_night: float = total / nights
        total_label.config(
            text=f"Total: {total:,.2f} TRY\nPer Night: {per_night:,.2f} TRY", fg="#2d3436"
        )
    except (ValueError, ZeroDivisionError):
        total_label.config(text="⚠️ Please enter a valid number of nights", fg="red")

def main() -> None:
    window: Tk = Tk()
    window.title("Daily Income Calculator")
    window.geometry("400x500")
    window.config(bg="#81ecec")

    # === Variables ===
    amount_var: StringVar = StringVar()
    symbol_var: StringVar = StringVar()
    rate_var: StringVar = StringVar()
    nights_var: StringVar = StringVar()

    label_fg: str = "#2d3436"
    entry_bg: str = "#ffffff"
    entry_fg: str = "#2d3436"
    button_bg: str = "#55efc4"
    button_fg: str = "#006266"
    result_bg: str = "#dfe6e9"

    Label(window, text="💰 Amount:", bg="#81ecec", fg=label_fg, font=("Segoe UI", 10)).pack()
    Entry(window, textvariable=amount_var, bg=entry_bg, fg=entry_fg, insertbackground=entry_fg).pack()

    Label(window, text="💱 Currency Symbol (e.g., USD, TRY):", bg="#81ecec", fg=label_fg, font=("Segoe UI", 10)).pack()
    Entry(window, textvariable=symbol_var, bg=entry_bg, fg=entry_fg, insertbackground=entry_fg).pack()

    Label(window, text="📈 Conversion Rate to TRY:", bg="#81ecec", fg=label_fg, font=("Segoe UI", 10)).pack()
    Entry(window, textvariable=rate_var, bg=entry_bg, fg=entry_fg, insertbackground=entry_fg).pack()

    result_label: Label = Label(window, text="", bg=result_bg, fg=label_fg)
    result_label.pack(pady=5)

    Button(window, text="➕ Add", bg=button_bg, fg=button_fg, relief="groove", bd=2,
           font=("Segoe UI", 10, "bold"),
           command=lambda: add_amount(amount_var, symbol_var, rate_var, result_label)).pack(pady=10)

    Separator(window).pack(pady=5, fill='x')

    Label(window, text="🌙 Nights:", bg="#81ecec", fg=label_fg, font=("Segoe UI", 10)).pack()
    Entry(window, textvariable=nights_var, bg=entry_bg, fg=entry_fg, insertbackground=entry_fg).pack()

    total_label: Label = Label(window, text="", bg=result_bg, fg=label_fg)
    total_label.pack(pady=10)

    Button(window, text="✅ Calculate", bg=button_bg, fg=button_fg, relief="groove", bd=2,
           font=("Segoe UI", 10, "bold"),
           command=lambda: calculate_total(nights_var, total_label)).pack(pady=10)

    window.mainloop()


if __name__ == "__main__":
    main()
