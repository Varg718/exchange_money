import requests
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from ttkthemes import ThemedStyle
from settings import get_exchange_rates, resize_background
from buttons import create_buttons

def main():
    # Get exchange rates
    response = get_exchange_rates()

    # Create main window
    root = tk.Tk()
    root.title('Currency Converter')
    root.geometry('500x300') 
    root.configure(bg='black')

    # Add background
    background_image = Image.open(r"/home/robertw/Desktop/git_hub_projects/exchange_project/output.jpg")
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(root, image=background_photo)
    background_label.place(relwidth=1, relheight=1)

    # Convert currency code to a list of str
    available_currencies = [rate['code'] for rate in response[0]['rates']]

    # Create buttons and labels
    create_buttons(root, available_currencies, response)

    # Bind resize_background function to window
    root.bind('<Configure>', resize_background)

    # Run the main program loop
    root.mainloop()

if __name__ == "__main__":
    main()
