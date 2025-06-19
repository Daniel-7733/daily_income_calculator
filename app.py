from tkinter import Tk, Label, Entry, Button, StringVar, filedialog
from typing import List, Dict, Union
from tkinter.ttk import Separator
from fpdf.enums import XPos, YPos
from csv import DictWriter
from fpdf import FPDF



# === Global Data Stores ===
entries: List[Dict[str, Union[float, str]]] = []

# === Add Amount ===
def add_amount(amount_var: StringVar, symbol_var: StringVar, rate_var: StringVar, result_label: Label) -> None:
    try:
        amount: float = float(amount_var.get())
        symbol: str = symbol_var.get().upper()
        rate: float = float(rate_var.get())

        converted: float = amount if symbol == "TRY" else amount * rate

        entries.append({
            "amount": amount,
            "symbol": symbol,
            "rate": rate,
            "converted": converted
        })

        result_label.config(text=f"✅ Added: {converted:,.2f} TRY", fg="#006266")
    except ValueError:
        result_label.config(text="⚠️ Please enter valid numbers", fg="red")

# === Calculate Total ===
def calculate_total(nights_var: StringVar, total_label: Label) -> None:
    try:
        nights: int = int(nights_var.get())
        total: float = sum(entry["converted"] for entry in entries)
        per_night: float = total / nights

        entries.append({
            "nights": nights,
            "total": total,
            "per_night": per_night
        })

        total_label.config(text=f"Total: {total:,.2f} TRY\nPer Night: {per_night:,.2f} TRY", fg="#2d3436")
    except (ValueError, ZeroDivisionError):
        total_label.config(text="⚠️ Please enter a valid number of nights", fg="red")

# === Save as PDF ===
def save(nights_var: StringVar) -> None:
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, text="Daily Income Report", new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
    pdf.ln(5)

    pdf.set_font("Arial", size=11)
    pdf.cell(0, 10, text="Inputs:", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    converted_entries = [entry for entry in entries if "converted" in entry]
    for idx, entry in enumerate(converted_entries, start=1):
        line = f"{idx}. {entry['amount']} {entry['symbol']} @ {entry['rate']} -> {entry['converted']:,.2f} TRY"
        pdf.multi_cell(0, 10, text=line)

    try:
        nights = int(nights_var.get())
        total = sum(item["converted"] for item in converted_entries)
        per_night = total / nights

        pdf.ln(5)
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, text="Summary:", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.multi_cell(0, 10, text=f"Total: {total:,.2f} TRY\nNights: {nights}\nPer Night: {per_night:,.2f} TRY")
    except (ValueError, ZeroDivisionError):
        pdf.multi_cell(0, 10, text="⚠️ Could not calculate summary: invalid number of nights.")

    file_path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")],
        title="Save PDF As"
    )

    if file_path:
        pdf.output(file_path)
        print(f"✅ File saved as: {file_path}")
    else:
        print("❌ Save operation cancelled.")


# === Save as CSV ===
def save_as_csv() -> None:
    file_path: str = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv")],
        title="Save CSV As"
    )

    if file_path:
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = DictWriter(file, fieldnames=["amount", "symbol", "rate", "converted"])
            writer.writeheader()
            for entry in entries:
                if "amount" in entry:
                    writer.writerow(entry)
        print(f"✅ CSV saved to {file_path}")

# === Placeholder Functions ===
def clean() -> None:
    pass

def switch_to_dark_mode() -> None:
    COLORS.update({
        "background": "#2d3436",
        "label_fg": "#ffffff",
        "entry_bg": "#636e72",
        "entry_fg": "#ffffff",
        "button_bg": "#00cec9",
        "button_fg": "#ffffff",
        "result_bg": "#3d3d3d",
    })

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

# === Main App ===
def main() -> None:
    window: Tk = Tk()
    window.title("Daily Income Calculator")
    window.geometry("400x500")
    window.config(bg=COLORS["background"])

    amount_var: StringVar = StringVar()
    symbol_var: StringVar = StringVar()
    rate_var: StringVar = StringVar()
    nights_var: StringVar = StringVar()

    Label(window, text="💰 Amount:", bg=COLORS["background"], fg=COLORS["label_fg"], font=("Segoe UI", 10)).pack()
    Entry(window, textvariable=amount_var, bg=COLORS["entry_bg"], fg=COLORS["entry_fg"], insertbackground=COLORS["entry_fg"]).pack()

    Label(window, text="💱 Currency Symbol (e.g., USD, TRY):", bg=COLORS["background"], fg=COLORS["label_fg"], font=("Segoe UI", 10)).pack()
    Entry(window, textvariable=symbol_var, bg=COLORS["entry_bg"], fg=COLORS["entry_fg"], insertbackground=COLORS["entry_fg"]).pack()

    Label(window, text="📈 Conversion Rate to TRY:", bg=COLORS["background"], fg=COLORS["label_fg"], font=("Segoe UI", 10)).pack()
    Entry(window, textvariable=rate_var, bg=COLORS["entry_bg"], fg=COLORS["entry_fg"], insertbackground=COLORS["entry_fg"]).pack()

    result_label: Label = Label(window, text="", bg=COLORS["result_bg"], fg=COLORS["label_fg"])
    result_label.pack(pady=5)

    Button(window, text="➕ Add", bg=COLORS["button_bg"], fg=COLORS["button_fg"], relief="groove", bd=2, font=("Segoe UI", 10, "bold"),
           command=lambda: add_amount(amount_var, symbol_var, rate_var, result_label)).pack(pady=10)

    Separator(window).pack(pady=5, fill='x')

    Label(window, text="🌙 Nights:", bg=COLORS["background"], fg=COLORS["label_fg"], font=("Segoe UI", 10)).pack()
    Entry(window, textvariable=nights_var, bg=COLORS["entry_bg"], fg=COLORS["entry_fg"], insertbackground=COLORS["entry_fg"]).pack()

    total_label: Label = Label(window, text="", bg=COLORS["result_bg"], fg=COLORS["label_fg"])
    total_label.pack(pady=10)

    Button(window, text="✅ Calculate", bg=COLORS["button_bg"], fg=COLORS["button_fg"], relief="groove", bd=2,
           font=("Segoe UI", 10, "bold"),
           command=lambda: calculate_total(nights_var, total_label)).pack(pady=10)

    Button(window, text="💾 Save", bg=COLORS["button_bg"], fg=COLORS["button_fg"], font=("Segoe UI", 10, "bold"),
           relief="groove", bd=2, command=lambda: save(nights_var)).pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    main()