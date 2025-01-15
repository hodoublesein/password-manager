import tkinter as tk
from tkinter import ttk, messagebox

class PasswordManagerUI:
    def __init__(self, parent, db_manager):
        self.parent = parent
        self.db_manager = db_manager

        # UI
        self.frame = ttk.Frame(parent)
        self.frame.pack(fill="both", expand=True)

        self.create_ui()

    def create_ui(self):
        # Create/Update form
        form_frame = tk.Frame(self.frame)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Account:").grid(row=0, column=0, padx=5, pady=5)
        self.account_entry = tk.Entry(form_frame, width=30)
        self.account_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Username:").grid(row=1, column=0, padx=5, pady=5)
        self.username_entry = tk.Entry(form_frame, width=30)
        self.username_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Password:").grid(row=2, column=0, padx=5, pady=5)
        self.password_entry = tk.Entry(form_frame, width=30, show="*")
        self.password_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(form_frame, text="Save", command=self.save_password).grid(row=3, column=0, padx=5, pady=5)
        tk.Button(form_frame, text="Update", command=self.update_password).grid(row=3, column=1, padx=5, pady=5)

        # Table
        self.tree = ttk.Treeview(self.frame, columns=("account", "username", "password"), show="headings")
        self.tree.heading("account", text="Account")
        self.tree.heading("username", text="Username")
        self.tree.heading("password", text="Password")
        self.tree.pack(fill="both", expand=True, pady=10)

        self.tree.bind("<Double-1>", self.fill_form)
        self.load_passwords()

    def load_passwords(self):
        """Loading passwords from Db"""
        for row in self.tree.get_children():
            self.tree.delete(row)

        for row in self.db_manager.fetch_all_passwords():
            self.tree.insert("", "end", iid=row[0], values=row[1:])

    def save_password(self):
        """Saving password in Db"""
        account = self.account_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not account or not password:
            messagebox.showerror("Error", "Please enter the required information.")
            return

        self.db_manager.add_password(account, username, password)
        self.load_passwords()
        self.clear_form()

    def update_password(self):
        """Update the selected password"""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a line.")
            return

        account = self.account_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not account or not password:
            messagebox.showerror("Error", "Please enter the required information.")
            return

        item_id = int(selected_item[0])
        self.db_manager.update_password(item_id, account, username, password)
        self.load_passwords()
        self.clear_form()

    def fill_form(self, event):
        """Filing form with the selected data"""
        selected_item = self.tree.selection()[0]
        values = self.tree.item(selected_item)["values"]
        self.account_entry.delete(0, tk.END)
        self.account_entry.insert(0, values[0])
        self.username_entry.delete(0, tk.END)
        self.username_entry.insert(0, values[1])
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, values[2])

    def clear_form(self):
        """Clear the form"""
        self.account_entry.delete(0, tk.END)
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
