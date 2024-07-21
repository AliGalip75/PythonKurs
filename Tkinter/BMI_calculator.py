from tkinter import *

gui = Tk()
gui.title("BMI Calculator")
gui.geometry("300x200")

global s1, s2
s1 = StringVar()
s2 = StringVar()


def calculate_BMI():

    try:
        if not s1.get() or not s2.get():
            label3.config(text="İki alanı da girmelisiniz!")
            return None
        weight = float(s1.get())
        height = float(s2.get())
        BMI = weight / (height * height)
        label3.config(text=f"Your BMI is {str(BMI)[0:5]},you are {bmi_status(BMI)}")
    except ValueError:
        label3.config(text="Lütfen sayı giriniz!")
    except ZeroDivisionError:
        label3.config(text="Boyunuz sıfır olamaz!")

def bmi_status(BMI):
    if 18.5 <= BMI < 25:
        return "Normal"
    elif 25 <= BMI < 30:
        return "Average"
    elif 30 <= BMI < 40:
        return "Overweight"
    else:
        return "Not Normal"


calculate_button = Button(gui, text="Calculate", width=16, height=1, command=calculate_BMI)
calculate_button.place(x=90, y=120)

label1 = Label(gui, text="Enter your Weight (kg)")
label1.place(x=90, y=0)

entry1 = Entry(gui, width=20, textvariable=s1)
entry1.place(x=90, y=30)

label2 = Label(gui, text="Enter your height (m)")
label2.place(x=90, y=60)

entry2 = Entry(gui, width=20, textvariable=s2)
entry2.place(x=90, y=90)

label3 = Label(gui)
label3.place(x=90, y=160)

gui.mainloop()
