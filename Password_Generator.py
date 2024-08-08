import tkinter as tk
from tkinter import ttk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PASSWORD GENARAIZER 🎲")
        self.root.geometry("500x300")
        self.root.configure(bg='#2b2b2b')

        style = ttk.Style()
        style.theme_use('clam')

        # Labels and Scales with modern styling
        self.char_label = ttk.Label(self.root, text="Quantidade de caracteres", background='#2b2b2b', foreground='white', font=("Arial", 10))
        self.char_label.pack(pady=(10, 0))

        self.char_value_label = ttk.Label(self.root, text="5", background='#2b2b2b', foreground='white', font=("Arial", 10))
        self.char_value_label.pack()

        self.char_scale = ttk.Scale(self.root, from_=1, to=20, orient=tk.HORIZONTAL, command=self.update_char_value)
        self.char_scale.set(5)
        self.char_scale.pack(fill='x', padx=20, pady=(0, 10))

        self.num_label = ttk.Label(self.root, text="Quantidade de números", background='#2b2b2b', foreground='white', font=("Arial", 10))
        self.num_label.pack(pady=(10, 0))

        self.num_value_label = ttk.Label(self.root, text="2", background='#2b2b2b', foreground='white', font=("Arial", 10))
        self.num_value_label.pack()

        self.num_scale = ttk.Scale(self.root, from_=0, to=10, orient=tk.HORIZONTAL, command=self.update_num_value)
        self.num_scale.set(2)
        self.num_scale.pack(fill='x', padx=20, pady=(0, 20))

        # Entry to display generated password with better styling
        self.password_var = tk.StringVar()
        self.password_entry = ttk.Entry(self.root, textvariable=self.password_var, font=("Arial", 14), width=24, justify='center')
        self.password_entry.pack(pady=(0, 20))

        # Buttons with improved styles
        self.generate_button = ttk.Button(self.root, text="Gerar Senha", command=self.generate_password)
        self.generate_button.pack(pady=(0, 5))

        self.copy_button = ttk.Button(self.root, text="Copiar Senha", command=self.copy_to_clipboard)
        self.copy_button.pack(pady=(0, 10))

    def update_char_value(self, value):
        self.char_value_label.config(text=f"{int(float(value))}")

    def update_num_value(self, value):
        self.num_value_label.config(text=f"{int(float(value))}")

    def generate_password(self):
        num_chars = int(self.char_scale.get())
        num_digits = int(self.num_scale.get())

        chars = random.choices(string.ascii_letters, k=num_chars)
        digits = random.choices(string.digits, k=num_digits)

        password_list = chars + digits
        random.shuffle(password_list)

        password = ''.join(password_list)
        self.password_var.set(password)

    def copy_to_clipboard(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.password_var.get())
        self.root.update()

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
