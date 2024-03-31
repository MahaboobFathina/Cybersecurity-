import tkinter as tk

class LoginPage(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Fake Login Page")

        self.username_label = tk.Label(self, text="Username")
        self.username_label.pack()

        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_label = tk.Label(self, text="Password")
        self.password_label.pack()

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.submit_button = tk.Button(self, text="Submit", command=self.submit_credentials)
        self.submit_button.pack()

        self.message_label = tk.Label(self, text="")
        self.message_label.pack()

    def submit_credentials(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        self.message_label.config(text=f"Login successful for {username}!")

if __name__ == "__main__":
    app = LoginPage()
    app.mainloop()
