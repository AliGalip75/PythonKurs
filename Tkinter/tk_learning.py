from tkinter import *

gui = Tk()
FONT = ('Arial', 20, 'normal')
gui.title("Python User Interface")
gui.geometry("600x600")

def clicked_button():
    print(my_entry.get())
    print(my_text.get("1.3", END))
    #1.3 -> 1. line , 3.char

def spinbox_selected():
    print(my_spinbox.get())

def checkbutton_selected():
    print(check_state.get())


def radio_selected():
    print(radio_state.get())

def listbox_selected(event):
    print(my_listbox.get(my_listbox.curselection()))

my_label = Label(gui, text="This is a label", fg="black", bg="yellow")
#my_label.pack()
#my_label.place(x=10, y=10)
#my_label.grid(row=0,column=0)

my_button = Button(gui, text="I am a button", command=clicked_button)
my_button.pack()
#my_button.place(x=0,y=0)
#my_button.grid(row=0,column=1)


my_entry = Entry(gui)
my_entry.pack(padx=10,pady=10)
#my_entry.grid(row=1,column=1)

my_text = Text(height=10, width=30, bg="yellow")
my_text.pack()

my_scale = Scale(gui, from_=0, to=50)
my_scale.pack()

my_spinbox = Spinbox(from_=0, to=50, command=spinbox_selected)
my_spinbox.pack()

check_state = IntVar()
my_checkbutton = Checkbutton(text="check", variable=check_state, command=checkbutton_selected)
my_checkbutton.pack()

radio_state = IntVar()
my_radiobutton = Radiobutton(text="1. option", value=10, variable=radio_state, command=radio_selected)
my_radiobutton2 = Radiobutton(text="2. option", value=20, variable=radio_state, command=radio_selected)
my_radiobutton.pack()
my_radiobutton2.pack()


my_listbox = Listbox()
name_list = ["ali", "galip", "yetiş"]
for i in range(len(name_list)):
    my_listbox.insert(i,name_list[i])
my_listbox.bind("<<ListboxSelect>>", listbox_selected)
my_listbox.pack()

gui.mainloop()
