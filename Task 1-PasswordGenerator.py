import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        use_letters = letters_var.get()
        use_numbers = numbers_var.get()
        use_symbols = symbols_var.get()

        characters = ''
        if use_letters:
            characters += string.ascii_letters
        if use_numbers:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Please select at least one character type.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length.")

# Create window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x250")
root.config(bg="#f0f0f0")

# Password length
tk.Label(root, text="Password Length:", bg="#f0f0f0").pack(pady=5)
length_entry = tk.Entry(root, width=10)
length_entry.pack()

# Checkboxes
letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters", variable=letters_var, bg="#f0f0f0").pack(anchor='w', padx=40)
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var, bg="#f0f0f0").pack(anchor='w', padx=40)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var, bg="#f0f0f0").pack(anchor='w', padx=40)

# Generate button
tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white").pack(pady=10)

# Output field
tk.Label(root, text="Generated Password:", bg="#f0f0f0").pack(pady=5)
password_entry = tk.Entry(root, width=40)
password_entry.pack()

# Run the app
root.mainloop()
