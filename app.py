from tkinter import Tk, Label, Entry, Button, StringVar
from tkinter.ttk import Separator
from typing import List, Dict

num_list: List[float] = [] # Store all entered amounts in TRY

def add_amount(amount_var: StringVar, symbol_var: StringVar, rate_var: StringVar, result_label: Label) -> None:
    """
    Add a new currency amount converted to TRY to the total.

    Args:
        amount_var (StringVar): Tkinter variable containing the amount input.
        symbol_var (StringVar): Currency symbol input (e.g., USD).
        rate_var (StringVar): Conversion rate input.
        result_label (Label): Label to display confirmation or error messages.

    Returns:
        None
    """
    try:
        amount: float = float(amount_var.get())
        symbol: str = symbol_var.get().upper()
        rate: float = float(rate_var.get())

        if symbol == "TRY":
            result: float = amount
        else:
            result: float = amount * rate

        num_list.append(result)
        result_label.config(text=f"✅ Added: {result:,.2f} TRY", fg="#006266")
    except ValueError:
        result_label.config(text="⚠️ Please enter valid numbers", fg="red")


def calculate_total(nights_var: StringVar, total_label: Label) -> None:
    """
    Calculate total income and per-night income based on user input.

    Args:
        nights_var (StringVar): Number of nights to divide total income by.
        total_label (Label): Label to display result.

    Returns:
        None
    """
    try:
        nights: int = int(nights_var.get())
        total: float = sum(num_list)
        per_night: float = total / nights
        total_label.config(
            text=f"Total: {total:,.2f} TRY\nPer Night: {per_night:,.2f} TRY", fg="#2d3436"
        )
    except (ValueError, ZeroDivisionError):
        total_label.config(text="⚠️ Please enter a valid number of nights", fg="red")


def clean() -> None:
    """
    Placeholder to clear all input fields and result labels.

    Returns:
        None
    """
    pass

def switch_to_dark_mode() -> None:
    """
    Placeholder for toggling the app between light and dark themes.

    Returns:
        None
    """

    COLORS.update({
        "background": "#2d3436",
        "label_fg": "#ffffff",
        "entry_bg": "#636e72",
        "entry_fg": "#ffffff",
        "button_bg": "#00cec9",
        "button_fg": "#ffffff",
        "result_bg": "#3d3d3d",
    })


def save() -> None:
    """
    Placeholder for saving data as a file (e.g., PDF or CSV).

    Returns:
        None
    """
    pass

# === Color Palette ===
COLORS: Dict[str, str] = {
    "background": "#81ecec",
    "label_fg": "#2d3436",
    "entry_bg": "#ffffff",
    "entry_fg": "#2d3436",
    "button_bg": "#55efc4",
    "button_fg": "#006266",
    "result_bg": "#dfe6e9",
}

def main() -> None:
    """
    Launch the Daily Income Calculator GUI application.
    """
    # === App Root ===
    window: Tk = Tk()
    window.title("Daily Income Calculator")
    window.geometry("400x500")
    window.config(bg=COLORS["background"])

    # === Variables ===
    amount_var: StringVar = StringVar()
    symbol_var: StringVar = StringVar()
    rate_var: StringVar = StringVar()
    nights_var: StringVar = StringVar()

    # === Calculator Page ===
    Label(window, text="💰 Amount:", bg=COLORS["background"], fg=COLORS["label_fg"], font=("Segoe UI", 10)).pack()
    Entry(window, textvariable=amount_var, bg=COLORS["entry_bg"], fg=COLORS["entry_fg"], insertbackground=COLORS["entry_fg"]).pack()

    Label(window, text="💱 Currency Symbol (e.g., USD, TRY):", bg=COLORS["background"], fg=COLORS["label_fg"], font=("Segoe UI", 10)).pack()
    Entry(window, textvariable=symbol_var, bg=COLORS["entry_bg"], fg=COLORS["entry_fg"], insertbackground=COLORS["entry_fg"]).pack()

    Label(window, text="📈 Conversion Rate to TRY:", bg=COLORS["background"], fg=COLORS["label_fg"], font=("Segoe UI", 10)).pack()
    Entry(window, textvariable=rate_var, bg=COLORS["entry_bg"], fg=COLORS["entry_fg"], insertbackground=COLORS["entry_fg"]).pack()

    result_label: Label = Label(window, text="", bg=COLORS["result_bg"], fg=COLORS["label_fg"])
    result_label.pack(pady=5)

    Button(window, text="➕ Add", bg=COLORS["button_bg"], fg=COLORS["button_fg"], relief="groove", bd=2,
           font=("Segoe UI", 10, "bold"),
           command=lambda: add_amount(amount_var, symbol_var, rate_var, result_label)).pack(pady=10)

    Separator(window).pack(pady=5, fill='x')

    Label(window, text="🌙 Nights:", bg=COLORS["background"], fg=COLORS["label_fg"], font=("Segoe UI", 10)).pack()
    Entry(window, textvariable=nights_var, bg=COLORS["entry_bg"], fg=COLORS["entry_fg"], insertbackground=COLORS["entry_fg"]).pack()

    total_label: Label = Label(window, text="", bg=COLORS["result_bg"], fg=COLORS["label_fg"])
    total_label.pack(pady=10)

    Button(window, text="✅ Calculate", bg=COLORS["button_bg"], fg=COLORS["button_fg"], relief="groove", bd=2,
           font=("Segoe UI", 10, "bold"),
           command=lambda: calculate_total(nights_var, total_label)).pack(pady=10)

    window.mainloop()


if __name__ == "__main__":
    main()
