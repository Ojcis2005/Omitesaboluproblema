import customtkinter
customtkinter.set_appearance_mode("Sistem")
customtkinter.set_default_color_theme("dark-blue")
import tkinter
root = customtkinter.CTk()
root.geometry("500x350")
def login():
    print("Datu ievade")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text= "Ievadiet ražu", text_font=("Roboto", 24))
label.pack(pafy=12, padx=10)

entry1 = customtkinter.CtkEntery(master=frame, placeholder_text="auglis")
entry1.pac(pady=12, padx=10)

entry2 = customtkinter.CtkEntery(master=frame, placeholder_text="dārzenis")
entry2.pac(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="aaa")
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="bbbb")
checkbox.pack(pady=12, padx=10)

root.mainloop()