import tkinter as tk
from tkinter import ttk

def exchange_currency(currency_combobox, quantity_entry, result_label, response):
    # Currency exchange
    currency_to = currency_combobox.get()
    # Managing errors
    try:
        quantity = float(quantity_entry.get())
        if quantity <= 0:
            result_label.config(text='Invalid quantity. Please enter a positive number.')
            return
    except ValueError:
        result_label.config(text='Invalid quantity. Please enter a valid number.')
        return
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

def create_buttons(root, available_currencies, response):
    # Create buttons and labels
    currency_label = tk.Label(root, text='Choose currency to exchange to:', bg='black', fg='white')
    currency_label.pack()
    currency_combobox = ttk.Combobox(root, values=available_currencies, state='readonly')
    currency_combobox.set(available_currencies[0])
    currency_combobox.pack()
    quantity_label = tk.Label(root, text='Enter quantity in PLN:', bg='black', fg='white')
    quantity_label.pack()
    quantity_entry = tk.Entry(root)
    quantity_entry.pack()
    exchange_button = tk.Button(root, text='Exchange', command=lambda: exchange_currency(currency_combobox, quantity_entry, result_label, response), bg='green', fg='black')
    exchange_button.pack()
    result_label = tk.Label(root, text='', bg='black', fg='white')
    result_label.pack()
