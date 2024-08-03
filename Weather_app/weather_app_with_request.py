import requests
from tkinter import *

def center_window(window):
    window.update_idletasks()
    width_window = window.winfo_width()
    height_window = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width_window) // 2
    y = (screen_height - height_window) // 2
    window.geometry(f"{width_window}x{height_window}+{x}+{y}")
def make_request(url):
    response = requests.get(url)
    return response


'''api_key = 'de4b72a17b612d8b1b3b5c7bd9066379'

city = input('Enter city name: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = make_request(url)
if response.status_code == 200:
    data = response.json()
    temp = int(data['main']['temp'] - 273)
    desc = data['weather'][0]['description']
    '''
gui = Tk()
gui.title("Weather")
gui.geometry("400x780")
center_window(gui)

gui.mainloop()