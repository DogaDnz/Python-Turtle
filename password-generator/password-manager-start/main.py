from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(5, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(1, 3))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    pass_input.insert(0, password)
    pyperclip.copy(password)






# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    email = email_input.get()
    password = pass_input.get()
    cntn = True

    while cntn:
        if len(website) == 0 or len(website) == 0:
            cntn = False
            messagebox.showinfo(message="Please do not leave any empty fields!")
            break

        yes_or_no = messagebox.askokcancel(title=website,
                                           message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \n Is it ok to save?")

        if yes_or_no:
            with open("data.txt", "a") as f:
                f.write(f"{website} | {email} | {password}\n")
            website_input.delete(0, END)
            email_input.delete(0, END)
            pass_input.delete(0, END)
            break


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website: ", font=("Arial", 14), fg="black")
website_label.grid(row=1, column=0)

website_input = Entry(width=60)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()


email_label = Label(window, text="Email/Username", font=("Arial", 14), fg="black")
email_label.grid(row=2, column=0)

email_input = Entry(width=60)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "angela@gmail.com")

pass_label = Label(window, text="Password", font=("Arial", 14), fg="black")
pass_label.grid(row=3, column=0)

pass_input = Entry(width=25)
pass_input.grid(row=3, column=1)

fnd_password = Button(text="Generate Password: ", font=("Arial", 12), fg="black", width=18)
fnd_password.grid(row=3, column=2)
add_button = Button(text="Add", width=30, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()