import tkinter as tk
from database import DatabaseManager
from password_manager_ui import PasswordManagerUI
from password_generator_ui import PasswordGeneratorUI

class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")

        # Database management
        self.db_manager = DatabaseManager()

        # Tabs
        self.notebook = tk.ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True)

        # Password manager tab
        self.password_manager_tab = tk.Frame(self.notebook)
        self.notebook.add(self.password_manager_tab, text="Password manager")
        PasswordManagerUI(self.password_manager_tab, self.db_manager)

        # Password generator tab
        self.password_generator_tab = tk.Frame(self.notebook)
        self.notebook.add(self.password_generator_tab, text="Password generator")
        PasswordGeneratorUI(self.password_generator_tab)

    def on_close(self):
        """Close program and database"""
        self.db_manager.close()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManagerApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()
