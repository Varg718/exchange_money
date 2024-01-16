import requests
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from ttkthemes import ThemedStyle

def exchange_currency():
    currency_to = currency_combobox.get()
    
    # Wybór ilości do wymiany
    try:
        quantity = float(quantity_entry.get())
        if quantity <= 0:
            result_label.config(text='Invalid quantity. Please enter a positive number.')
            return
    except ValueError:
        result_label.config(text='Invalid quantity. Please enter a valid number.')
        return

    # Wyszukiwanie kursu wymiany
    rate_to = 0
    for rate in response[0]['rates']:
        if currency_to == rate['code']:
            rate_to = float(rate['mid'])
            break

    if rate_to == 0:
        result_label.config(text=f'Error: Unable to find exchange rate for {currency_to}.')
    else:
        result = quantity / rate_to
        result_label.config(text=f'You will receive {result:.2f} {currency_to}!')

# Pobieranie kursów wymiany przy uruchomieniu programu
url = requests.get('http://api.nbp.pl/api/exchangerates/tables/A/')
response = url.json()

# Tworzenie głównego okna
root = tk.Tk()
root.title('Currency Converter')
root.geometry('500x300')  # Ustawienie rozmiaru okna
root.configure(bg='black')  # Ustawienie tła na czarne

# Dodanie tła
background_image = Image.open("C:\\Users\\Komfig\\Desktop\\git_hub_projects\\exchange_project\\output.jpg")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)

# Wybór waluty
currency_label = tk.Label(root, text='Choose currency to exchange to:', bg='black', fg='white')
currency_label.pack()

# Konwertowanie kodu waluty na listę ciągów znaków
available_currencies = [rate['code'] for rate in response[0]['rates']]
currency_combobox = ttk.Combobox(root, values=available_currencies, state='readonly')
currency_combobox.set(available_currencies[0])  # Domyślna waluta
currency_combobox.pack()

# Wprowadzanie ilości do wymiany
quantity_label = tk.Label(root, text='Enter quantity in PLN:', bg='black', fg='white')
quantity_label.pack()

quantity_entry = tk.Entry(root)
quantity_entry.pack()

# Przycisk do wymiany waluty
exchange_button = tk.Button(root, text='Exchange', command=exchange_currency, bg='green', fg='black')
exchange_button.pack()

# Wynik wymiany
result_label = tk.Label(root, text='', bg='black', fg='white')
result_label.pack()
# Przechowywanie referencji do obiektu obrazu w zmiennej globalnej
resized_background_photo = None

# Funkcja do dostosowywania rozmiaru tła do rozmiaru okna
def resize_background(event):
    global resized_background_photo  # Dodaj globalną deklarację
    new_width = event.width
    new_height = event.height
    resized_image = background_image.resize((new_width, new_height), Image.BICUBIC)
    resized_background_photo = ImageTk.PhotoImage(resized_image)
    background_label.configure(image=resized_background_photo)
    background_label.image = resized_background_photo

# Bindowanie funkcji resize_background do zmiany rozmiaru okna
root.bind('<Configure>', resize_background)

# Uruchomienie głównej pętli programu
root.mainloop()

