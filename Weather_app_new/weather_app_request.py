import requests
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import re

def center_window(window):
    window.update_idletasks()
    width_window = window.winfo_width()
    height_window = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width_window) // 2
    y = (screen_height - height_window) // 2
    window.geometry(f"{width_window}x{height_window}+{x}+{y}")


def show_weather_info(temp, desc, city):

    weather_window = Toplevel(gui)
    weather_window.geometry("500x300")
    #center_window(weather_window)
    weather_window.title(f'{city} Weather Information')


    # Temperature label location
    temperature_label = Label(weather_window, text=f"{temp} °C", font=("Arial", 12, "bold"))
    temperature_label.pack()


    # weather label location
    weather_label = Label(weather_window, text=desc, font=("Arial", 12, "bold"))
    weather_label.pack()

def make_request(url):
    response = requests.get(url)
    return response


def is_valid_country_name(name):
    # Ülke ismi sadece harf ve boşluk içermelidir
    return bool(re.match("^[A-Za-z ]+$", name))


def enter_func():
    try:
        city = Entry_country.get().strip()
        if not is_valid_country_name(city):
            raise ValueError("Geçersiz ülke ismi!")
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        response = make_request(url)
        if response.status_code == 200:
            data = response.json()
            temp = int(data['main']['temp'] - 273)
            desc = data['weather'][0]['description']
            show_weather_info(temp, desc, city)
        else:
            messagebox.showerror("Error!", f"API Error: {response.status_code}")

    except requests.RequestException as e:
        messagebox.showerror("Error!", f"Request Error: {e}")
    except ValueError as e:
        messagebox.showerror("Error!", f"Value Error: {e}")
    except KeyError as e:
        messagebox.showerror("Error!", f"Key Error: {e}")
    except Exception as e:
        messagebox.showerror("Error!", f"An unexpected error occurred: {e}")

#*********https://home.openweathermap.org/ sitesinden API alıp koda ekleyiniz************
api_key = 'enter_api_key'

gui = Tk()
gui.title("Weather")
gui.geometry("300x300")
center_window(gui)


label_country = Label(gui, text="Enter your country", font=("Arial", 12, "bold"), pady=10)
label_country.pack()

Entry_country = Entry(gui, width=35)
Entry_country.focus()
Entry_country.pack()

button = Button(gui, text="Enter", width=18, command=enter_func)
button.pack(pady=20)


gui.mainloop()