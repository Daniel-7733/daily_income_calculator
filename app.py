from tkinter import Tk, Button, Frame, Widget, Label, Entry, StringVar
from calculator import add_amount, calculate_total
from PIL import Image, ImageTk, ImageFile
from typing import Callable, Tuple
from tkinter.ttk import Separator




def page_reset() -> None:
    """
    Clear previous content.

    Returns:
        None
    """

    for widget in content_frame.winfo_children():
        widget.destroy()  # Clear previous content


# TODO: (In create_menu_button) I would like to highlight the bottom that I am on it; that will show the person, which page he or she is on it
def create_menu_button(parent: Widget, image_path: str, size: Tuple[int, int], command: Callable[[], None]) -> Button:
    """Creates a sidebar/menu button with an image and click action.

    Args:
        parent: The parent tkinter widget to attach the button to.
        image_path: The path to the icon/image file.
        size: A tuple (width, height) for resizing the image.
        command: A no-argument function to call when the button is clicked.

    Returns:
        The created tkinter Button widget.
    """
        
    button_frame: Frame = Frame(parent, bg="#0755e7")
    button_frame.pack(fill='none', pady=5)

    img: ImageFile = Image.open(image_path)
    img: Image.Image = img.resize(size, Image.Resampling.LANCZOS)
    icon: ImageTk.PhotoImage = ImageTk.PhotoImage(img)

    button: Button = Button(
        button_frame,
        image=icon,
        bg='#a3c3ff',
        bd=0,
        anchor='w',
        command=command
    )
    button.image = icon  # Prevent garbage collection
    button.pack(side='bottom', fill='none', expand=True)

    return button



def main() -> None:
    window: Tk = Tk()
    window.title("Daily Income Calculator")
    window.geometry("400x500")
    window.config(bg="#e6f0ff")

    # === Input Fields ===
    amount_var: StringVar = StringVar()
    symbol_var: StringVar = StringVar()
    rate_var: StringVar = StringVar()
    nights_var: StringVar = StringVar()

    Label(window, text="💰 Amount:", bg="#e6f0ff").pack()
    Entry(window, textvariable=amount_var).pack()

    Label(window, text="💱 Currency Symbol (e.g., USD, TRY):", bg="#e6f0ff").pack()
    Entry(window, textvariable=symbol_var).pack()

    Label(window, text="📈 Conversion Rate to TRY:", bg="#e6f0ff").pack()
    Entry(window, textvariable=rate_var).pack()

    result_label: Label = Label(window, text="", bg="#e6f0ff")
    result_label.pack(pady=5)

    Button(window, text="➕ Add", command=lambda: add_amount(amount_var, symbol_var, rate_var, result_label)).pack(pady=10)

    Separator(window).pack(pady=5, fill='x')

    Label(window, text="🌙 Nights:", bg="#e6f0ff").pack()
    Entry(window, textvariable=nights_var).pack()

    total_label: Label = Label(window, text="", bg="#e6f0ff")
    total_label.pack(pady=10)

    Button(window, text="✅ Calculate", command=lambda: calculate_total(nights_var, total_label)).pack(pady=10)

    window.mainloop()


if __name__ == "__main__":
    main()
