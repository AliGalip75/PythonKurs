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


def search_element(matrix, target):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                return i + 1


def show_weather_info(temp, desc, city):

    icon_one = ["clear sky"]

    icon_two = ["few clouds"]

    icon_three = ["scattered clouds"]

    icon_four = ["broken clouds", "overcast clouds"]

    icon_nine = ["light intensity drizzle", "drizzle", "heavy intensity drizzle", "light intensity drizzle rain", "drizzle rain", "heavy intensity drizzle rain",
                 "shower rain and drizzle", "heavy shower rain and drizzle", "shower drizzle", "light intensity shower rain", "shower rain", "heavy intensity shower rain",
                 "ragged shower rain"]

    icon_ten = ["light rain", "moderate rain", "heavy intensity rain", "very heavy rain", "extreme rain"]

    icon_eleven = ["thunderstorm with light rain", "thunderstorm with rain", "thunderstorm with heavy rain", "light thunderstorm", "thunderstorm", "heavy thunderstorm",
                   "ragged thunderstorm", "thunderstorm with light drizzle", "thunderstorm with drizzle", "thunderstorm with heavy drizzle"]

    icon_threeteen = ["freezing rain", "light snow", "light snow", "snow", "heavy snow", "sleet", "light shower sleet", "shower sleet", "light rain and snow", "rain and snow",
                      "light shower snow", "shower snow", "heavy shower snow"]

    icon_fifty = ["mist", "smoke", "haze", "sand/dust whirls", "fog", "sand", "dust", "volcanic ash", "squalls", "tornado"]

    icons = [icon_one, icon_two, icon_three, icon_four, icon_nine, icon_ten, icon_eleven, icon_threeteen, icon_fifty]

    index = search_element(icons, desc)
    if index == 1:
        show_png = "image1"
    elif index == 2:
        show_png = "image2"
    elif index == 3:
        show_png = "image3"
    elif index == 4:
        show_png = "image4"
    elif index == 5:
        show_png = "image9"
    elif index == 6:
        show_png = "image10"
    elif index == 7:
        show_png = "image11"
    elif index == 8:
        show_png = "image13"
    else:
        show_png = "image50"

    weather_window = Toplevel(gui)
    weather_window.geometry("500x300")
    #center_window(weather_window)
    weather_window.title(f'{city} Weather Information')

    # Temperature png and label
    temperature_image = Image.open("pngs/celsius.png")
    resized_temperature_image = temperature_image.resize((150, 150))
    img = ImageTk.PhotoImage(resized_temperature_image)
    panel1 = Label(weather_window, image=img)
    panel1.image = img
    panel1.place(x=30, y=30)

    # Temperature label location
    temperature_label = Label(weather_window, text=f"{temp} °C", font=("Arial", 12, "bold"))
    temperature_label.place(x=65, y=200)

    # weather png and label
    temperature_image = Image.open(f"pngs/{show_png}.png")
    resized_temperature_image = temperature_image.resize((120, 120))
    weather_image = ImageTk.PhotoImage(resized_temperature_image)
    panel2 = Label(weather_window, image=weather_image)
    panel2.image = weather_image
    panel2.place(x=290, y=65)

    # weather label location
    weather_label = Label(weather_window, text=desc, font=("Arial", 12, "bold"))
    weather_label.place(x=310, y=200)

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


api_key = 'de4b72a17b612d8b1b3b5c7bd9066379'

gui = Tk()
gui.title("Weather")
gui.geometry("300x300")
center_window(gui)

original_image = Image.open("pngs/weather.png")
width, height = original_image.size
new_width = width // 4
new_height = height // 4
resized_image = original_image.resize((new_width, new_height))
img = ImageTk.PhotoImage(resized_image)
panel = Label(gui, image=img)
panel.pack()

label_country = Label(gui, text="Enter your country", font=("Arial", 12, "bold"), pady=10)
label_country.pack()

Entry_country = Entry(gui, width=35)
Entry_country.focus()
Entry_country.pack()

button = Button(gui, text="Enter", width=18, command=enter_func)
button.pack(pady=20)


gui.mainloop()