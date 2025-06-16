from tkinter import Tk, Button, Frame, Widget, Text, Label, Entry
from PIL import Image, ImageTk, ImageFile
from typing import Callable, Tuple



def page_reset() -> None:
    """
    Clear previous content.

    Returns:
        None
    """

    for widget in content_frame.winfo_children():
        widget.destroy()  # Clear previous content

def add() -> str:
    # this one will add input to the list
    return "Add() function isn't complete"


def finish() -> str:
    # this function suppose to calculate all the inputs and show them on screen
    return "finish() function isn't complete"


def load_calculator_page() -> None:

    page_reset()

    screen: Text = Text(content_frame, height=10, width=250, bg='#ff6600', font=('TkFixFont', 10))
    screen.config(state='disabled')
    screen.pack(padx=30, pady=30)

    # TODO: Add a Label which is "Amount"
    Label(content_frame,
          text="Amount:",
          bg='#a3c3ff',
          font=('Arial', 12, 'bold')).pack()
    # TODO: Add a Entry which is for "Amount"
    amount_entry: Entry = Entry(content_frame, font=('Arial', 11))
    amount_entry.pack()

    # TODO: Add a Label which is "Currency symbol"
    Label(content_frame,
          text="Currency symbol:",
          bg='#a3c3ff',
          font=('Arial', 12, 'bold')).pack()
    # TODO: Add a Entry which is for "Currency symbol"
    symbol_entry: Entry = Entry(content_frame, font=('Arial', 11))
    symbol_entry.pack()

    # TODO: Add a Label which is "Rate"
    Label(content_frame,
          text="Rate:",
          bg='#a3c3ff',
          font=('Arial', 12, 'bold')).pack()
    # TODO: Add a Entry which is for "Rate"
    rate_entry: Entry = Entry(content_frame, font=('Arial', 11))
    rate_entry.pack()

    # TODO: Add a "ADD" button for adding my numbers for calculation
    add_button: Button = Button(content_frame,
                                 text='Add',
                                 bg="#08e966",
                                 fg='black',
                                 font=('Arial', 11, 'bold'),
                                 width=10,
                                 command=lambda: add)
    add_button.pack()
    # TODO: Add a "Finish" button for saying done; which means there is no other input left to calculate
    finish_button: Button = Button(content_frame,
                                 text='Finish',
                                 bg="#08e966",
                                 fg='black',
                                 font=('Arial', 11, 'bold'),
                                 width=10,
                                 command=lambda: finish)
    finish_button.pack()


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




if __name__ == '__main__':
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
    create_menu_button(menu_frame, "calculator_icon.png", (32, 32), load_calculator_page) # icons link: https://www.flaticon.com/free-icons/calculator

    window.mainloop()


# if __name__ == "__main__":
#     main()
