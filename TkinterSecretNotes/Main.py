from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image


# Başlangıçta paneli ekranın tam ortasında konumlandırmak için
def center_window(window):
    window.update_idletasks()
    width_window = window.winfo_width()
    height_window = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width_window) // 2
    y = (screen_height - height_window) // 2
    window.geometry(f"{width_window}x{height_window}+{x}+{y}")

 #Sifreleme
def caesar_encrypt(message, shift=5):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_amount = shift % 26
            if char.isupper():
                new_char = chr((ord(char) + shift_amount - 65) % 26 + 65)
            else:
                new_char = chr((ord(char) + shift_amount - 97) % 26 + 97)
            encrypted_message += new_char
        else:
            encrypted_message += char
    return encrypted_message

#şifreyi çözme
def caesar_decrypt(encrypted_message, shift=5):
    return caesar_encrypt(encrypted_message, -shift)

def save_and_encrypt():
    if secret_text.get("1.0", END).strip() == "":
        messagebox.showerror("Hata", "Şifrelenecek mesajı giriniz")
        return
    elif Entry_key.get() == "":
        messagebox.showerror("Hata", "Şifre belirleyiniz")
        return
    elif Entry_title.get().strip() == "":
        messagebox.showerror("Hata", "Başlık giriniz")
        return
    f1 = open("secrets.txt", "a")
    title = Entry_title.get().strip()
    f1.write(title + "\n")
    f1.write(caesar_encrypt(secret_text.get("1.0", END).strip("\n") + " " + Entry_key.get()) + "\n")
    f1.close()
    read_file()
    Entry_title.delete(0, END)
    Entry_key.delete(0, END)
    secret_text.delete(1.0, END)

def select_indices(arr):
    selected_elements = []
    my_index = 1  # Başlangıç indeksi
    while my_index < len(arr):
        selected_elements.append(arr[my_index])
        my_index += 2  # 2 adım ilerle
    return selected_elements

#şifrelenmiş metinleri tutan listeyi oluştur
def read_file():
    f1 = open("secrets.txt", "r")
    global file_list
    global file_list2
    file_list = f1.readlines()
    file_list2 = select_indices(file_list)
    f1.close()

isFound = False
index = 0
def get_last_keys(str_list):
    last_words = []
    for s in str_list:
        words = s.split(" ")
        last_words.append(words[-1][:-1])
    return last_words

def get_secret(str_list):
    modified_list = []
    for s in str_list:
        words = s.split()
        if len(words) > 1:
            modified_list.append(' '.join(words[:-1]))
        elif len(words) == 1:
            modified_list.append('')
    return modified_list

def decrypt():
    read_file()
    global isFound
    global last_keys
    global index
    global secrets
    last_keys = get_last_keys(file_list2)
    secrets = get_secret(file_list2)
    for i in range(len(file_list2)):
        if secrets[i] == secret_text.get("1.0", END).strip():
            isFound = True
            index = i
            break
    if secret_text.get("1.0", END).strip() == "":
        messagebox.showerror("Hata", "Şifreli mesajı giriniz")
    elif not isFound:
        messagebox.showerror("Hata", "Böyle bir bilgi yok!")
    elif isFound and Entry_key.get().strip() == "":
        messagebox.showerror("Hata", "Şifreyi giriniz")
    elif isFound and (last_keys[index] == Entry_key.get().strip('\n')):
        secret_text.delete(1.0, END)
        secret_text.insert(END, caesar_decrypt(secrets[index]))
    else:
        messagebox.showerror("Hata", "Hatalı şifre")
    isFound = False

gui = Tk()
gui.title("Secret Notes")
gui.geometry("400x780")
center_window(gui)

secrets = []
file_list = []
file_list2 = []
last_keys = []

# Resmi kucultup ortaya ekle
original_image = Image.open("security.png")
width, height = original_image.size
new_width = width // 4
new_height = height // 4
resized_image = original_image.resize((new_width, new_height))
img = ImageTk.PhotoImage(resized_image)
panel = Label(gui, image=img)
panel.pack()

label_title = Label(gui, text="Enter your title", font=("Arial", 12, "bold"), pady=10)
label_title.pack()

Entry_title = Entry(gui, width=35)
Entry_title.focus()
Entry_title.pack()

label_secret = Label(gui, text="Enter your secret", font=("Arial", 12, "bold"), pady=10)
label_secret.pack()

secret_text = Text(gui, width=35, height=15)
secret_text.config(pady=10)
secret_text.pack()

label_title = Label(gui, text="Enter master key", font=("Arial", 12, "bold"), pady=10)
label_title.pack()

Entry_key = Entry(gui, width=35)
Entry_key.pack()

button_save_encrypt = Button(gui, text="Save & Encrypt", width=18, command=save_and_encrypt)
button_save_encrypt.place(x=130, y=680)

button_decrypt = Button(gui, text="Decrypt", width=18, command=decrypt)
button_decrypt.place(x=130, y=720)

gui.mainloop()
