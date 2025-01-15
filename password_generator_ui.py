import tkinter as tk
from tkinter import messagebox
from password_generator import generate_password

class PasswordGeneratorUI:
    def __init__(self, parent):
        self.parent = parent

        self.frame = tk.Frame(parent)
        self.frame.pack(fill="both", expand=True)

        self.create_ui()

    def create_ui(self):
        generator_frame = tk.Frame(self.frame)
        generator_frame.pack(pady=10)

        tk.Label(generator_frame, text="Password Length").grid(row=0, column=0, padx=5, pady=5)
        self.length_entry = tk.Entry(generator_frame, width=10)
        self.length_entry.grid(row=0, column=1, padx=5, pady=5)

        self.uppercase_var = tk.BooleanVar()
        self.lowercase_var = tk.BooleanVar()
        self.numbers_var = tk.BooleanVar()
        self.symbols_var = tk.BooleanVar()

        tk.Checkbutton(generator_frame, text="Uppercase", variable=self.uppercase_var).grid(row=1, column=0, padx=5, pady=5)
        tk.Checkbutton(generator_frame, text="Lowercase", variable=self.lowercase_var).grid(row=1, column=1, padx=5, pady=5)
        tk.Checkbutton(generator_frame, text="Numbers", variable=self.numbers_var).grid(row=1, column=2, padx=5, pady=5)
        tk.Checkbutton(generator_frame, text="Symbols", variable=self.symbols_var).grid(row=1, column=3, padx=5, pady=5)

        tk.Button(generator_frame, text="Generate password", command=self.generate_password).grid(row=2, column=1, padx=5, pady=10)

        self.generated_password_label = tk.Label(generator_frame, text="Password")
        self.generated_password_label.grid(row=3, column=0, columnspan=3, padx=5, pady=10)

    def generate_password(self):
        """Generate a random password"""
        length = self.length_entry.get()
        if not length.isdigit():
            messagebox.showerror("Error", "Please enter a valid length.")
            return

        length = int(length)
        use_uppercase = self.uppercase_var.get()
        use_lowercase = self.lowercase_var.get()
        use_numbers = self.numbers_var.get()
        use_symbols = self.symbols_var.get()

        try:
            password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols)
            self.generated_password_label.config(text=f"Password: {password}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
