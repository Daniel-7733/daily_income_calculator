from tkinter import Tk, Button, Frame, PhotoImage, Widget
from PIL import Image, ImageTk, ImageFile
from typing import Callable, Tuple


def load_calculator_page() -> None:
    pass


 # TODO: (In create_menu_button) I would like to highlight the buttom that I am on it; that will show the person, which page he or she is on it
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
    window.geometry("350x600")
    window.title("Currency Converter")
    window.config(bg="#b3c6ff")

    # === Grid layout with 2 rows ===
    window.grid_rowconfigure(1, weight=1)  # content frame should expand
    window.grid_columnconfigure(0, weight=1)  # only one column

    # Top menu/sidebar (like a navigation bar)
    menu_frame: Frame = Frame(window, bg='#595959', height=100)
    menu_frame.grid(row=3, column=0, sticky="ew")
    menu_frame.grid_propagate(False)

    # Main content frame
    content_frame: Frame = Frame(window, bg="#b3c6ff")
    content_frame.grid(row=1, column=0, sticky="nsew")

    # Menu button
    create_menu_button(menu_frame, r"daily_income_calculator\Calculator_icon.svg.png", (32, 32), load_calculator_page)

    window.mainloop()


if __name__ == "__main__":
    main()
