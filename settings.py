import requests
from PIL import Image, ImageTk

def get_exchange_rates():
    # Get exchange reates from API
    url = requests.get('http://api.nbp.pl/api/exchangerates/tables/A/')
    response = url.json()
    return response

def resize_background(event, background_image, background_label):
    #Adjust background size to window size
    new_width = event.width
    new_height = event.height
    resized_image = background_image.resize((new_width, new_height), Image.BICUBIC)
    resized_background_photo = ImageTk.PhotoImage(resized_image)
    background_label.configure(image=resized_background_photo)
    background_label.image = resized_background_photo
