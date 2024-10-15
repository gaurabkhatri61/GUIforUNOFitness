import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import json
import os

class UNOFitnessGUI:
    PLAN_PRICES = {"Beginner": 1000.00, "Intermediate": 2000.00, "Elite": 3000.00}
    SAUNA_PRICE_PER_SESSION = 1500.00
    SWIMMING_PRICE_PER_SESSION = 500.00
    PRIVATE_TRAINER_PRICE_PER_HOUR = 500.00
    WEEKS_IN_MONTH = 4
    USERS_FILE = "users.json"

    def __init__(remember, start):
        remember.start = start
        remember.start.title("UNO Fitness Program")
        remember.style = ttk.Style()
        remember.style.configure("TFrame", background="white")
        remember.style.configure("TLabel", background="white", foreground="black", font=("Arial", 16))
        remember.style.configure("TButton", background="white", foreground="black", font=("Arial", 16))
        remember.style.configure("TCheckbutton", background="white", foreground="black", font=("Arial", 16))
        remember.style.configure("TEntry", background="white", foreground="black", font=("Arial", 16))
        remember.style.configure("TCombobox", background="white", foreground="black", font=("Arial", 16)) 
        remember.create_login_page()

    def create_login_page(remember):
        remember.login_frame = ttk.Frame(remember.start, padding="20")
        remember.login_frame.grid(column=0, row=0, sticky=(tk.W, tk.N, tk.E, tk.S))
        
        login_title = ttk.Label(remember.login_frame, text="Get started with UNO Fitness Program", font=("Times New Roman", 18, "bold"))
        login_title.grid(column=0, row=0, columnspan=2, pady=10)

        username_label = ttk.Label(remember.login_frame, text="Username:")
        username_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        remember.username_entry = ttk.Entry(remember.login_frame, width=30)
        remember.username_entry.grid(column=1, row=1, sticky=(tk.W, tk.E), padx=5, pady=5)

        password_label = ttk.Label(remember.login_frame, text="Password:")
        password_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        remember.password_entry = ttk.Entry(remember.login_frame, show="*", width=30)
        remember.password_entry.grid(column=1, row=2, sticky=(tk.W, tk.E), padx=5, pady=5)

        login_button = ttk.Button(remember.login_frame, text="Login", command=remember.check_login)
        login_button.grid(column=0, row=3, columnspan=2, pady=10)

        register_button = ttk.Button(remember.login_frame, text="Register", command=remember.create_registration_window)
        register_button.grid(column=0, row=4, columnspan=2, pady=10)
        
        remember.login_frame.columnconfigure(1, weight=1)
        remember.login_frame.rowconfigure(0, weight=1)

    def check_login(remember):
        username = remember.username_entry.get()
        password = remember.password_entry.get()

        if not os.path.exists(remember.USERS_FILE):
            messagebox.showerror("Login Failed", "Invalid username or password")
            return

        with open(remember.USERS_FILE, "r") as file:
            users = json.load(file)

        user = users.get(username)

        if user and user["password"] == password:
            remember.login_frame.destroy()
            remember.plan = user["plan"]
            remember.sauna_sessions = user["sauna_sessions"]
            remember.swimming_sessions = user["swimming_sessions"]
            remember.coaching_hours = user["coaching_hours"]
            remember.create_main_frame()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def create_registration_window(remember):
        remember.registration_window = tk.Toplevel(remember.start)
        remember.registration_window.title("Register for UNO Fitness Program")

        name_label = ttk.Label(remember.registration_window, text="Customer Name:")
        name_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        remember.name_entry_reg = ttk.Entry(remember.registration_window, width=30)
        remember.name_entry_reg.grid(column=1, row=0, sticky=(tk.W, tk.E), padx=5, pady=5)

        password_label = ttk.Label(remember.registration_window, text="Password:")
        password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        remember.password_entry_reg = ttk.Entry(remember.registration_window, show="*", width=30)
        remember.password_entry_reg.grid(column=1, row=1, sticky=(tk.W, tk.E), padx=5, pady=5)

        current_weight_label = ttk.Label(remember.registration_window, text="Current Weight (kg):")
        current_weight_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        remember.current_weight_entry_reg = ttk.Entry(remember.registration_window, width=30)
        remember.current_weight_entry_reg.grid(column=1, row=2, sticky=(tk.W, tk.E), padx=5, pady=5)

        target_weight_label = ttk.Label(remember.registration_window, text="Target Weight Category:")
        target_weight_label.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
        remember.target_weight_combobox_reg = ttk.Combobox(remember.registration_window, width=28, values=["Maintain Weight", "Lose Weight", "Gain Weight"])
        remember.target_weight_combobox_reg.grid(column=1, row=3, sticky=(tk.W, tk.E), padx=5, pady=5)

        plan_label = ttk.Label(remember.registration_window, text="Training Plan:")
        plan_label.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
        remember.selected_plan_reg = tk.StringVar()
        plans = ["Beginner", "Intermediate", "Elite"]
        for i, plan in enumerate(plans):
            ttk.Radiobutton(remember.registration_window, text=plan, variable=remember.selected_plan_reg, value=plan).grid(column=1, row=i+4, sticky=tk.W, padx=5, pady=2)

        sauna_label = ttk.Label(remember.registration_window, text="Sauna Sessions:")
        sauna_label.grid(column=0, row=7, sticky=tk.W, padx=5, pady=5)
        remember.sauna_spinbox_reg = ttk.Spinbox(remember.registration_window, from_=0, to=100, width=28)
        remember.sauna_spinbox_reg.grid(column=1, row=7, sticky=(tk.W, tk.E), padx=5, pady=5)

        swimming_label = ttk.Label(remember.registration_window, text="Swimming Sessions:")
        swimming_label.grid(column=0, row=8, sticky=tk.W, padx=5, pady=5)
        remember.swimming_spinbox_reg = ttk.Spinbox(remember.registration_window, from_=0, to=100, width=28)
        remember.swimming_spinbox_reg.grid(column=1, row=8, sticky=(tk.W, tk.E), padx=5, pady=5)

        coaching_hours_label = ttk.Label(remember.registration_window, text="Private Coaching Hours:")
        coaching_hours_label.grid(column=0, row=9, sticky=tk.W, padx=5, pady=5)
        remember.coaching_hours_spinbox_reg = ttk.Spinbox(remember.registration_window, from_=0, to=100, width=28)
        remember.coaching_hours_spinbox_reg.grid(column=1, row=9, sticky=(tk.W, tk.E), padx=5, pady=5)

        register_button = ttk.Button(remember.registration_window, text="Register", command=remember.register_user)
        register_button.grid(column=0, row=10, columnspan=2, pady=10)

        remember.registration_window.columnconfigure(1, weight=1)
        remember.registration_window.rowconfigure(0, weight=1)

    def register_user(remember):
        username = remember.name_entry_reg.get()
        password = remember.password_entry_reg.get()
        plan = remember.selected_plan_reg.get()
        sauna_sessions = int(remember.sauna_spinbox_reg.get())
        swimming_sessions = int(remember.swimming_spinbox_reg.get())
        coaching_hours = int(remember.coaching_hours_spinbox_reg.get())

        new_user = {
            "password": password,
            "plan": plan,
            "sauna_sessions": sauna_sessions,
            "swimming_sessions": swimming_sessions,
            "coaching_hours": coaching_hours
        }

        if os.path.exists(remember.USERS_FILE):
            with open(remember.USERS_FILE, "r") as file:
                users = json.load(file)
        else:
            users = {}

        if username in users:
            messagebox.showerror("Registration Failed", "Username already exists")
        else:
            users[username] = new_user
            with open(remember.USERS_FILE, "w") as file:
                json.dump(users, file, indent=4)
            messagebox.showinfo("Registration Successful", "You have been registered successfully.")
            remember.registration_window.destroy()

    def create_main_frame(remember):
        remember.main_frame = ttk.Frame(remember.start, padding="20")
        remember.main_frame.grid(column=0, row=0, sticky=(tk.W, tk.N, tk.E, tk.S))

        # Calculate
        plan_price = remember.PLAN_PRICES.get(remember.plan, 0)
        sauna_cost = remember.sauna_sessions * remember.SAUNA_PRICE_PER_SESSION
        swimming_cost = remember.swimming_sessions * remember.SWIMMING_PRICE_PER_SESSION
        coaching_cost = remember.coaching_hours * remember.PRIVATE_TRAINER_PRICE_PER_HOUR
        total_cost = plan_price + sauna_cost + swimming_cost + coaching_cost

        # Display
        result_message = (
            f"Training Plan: {remember.plan}\n"
            f"Sauna Sessions: {remember.sauna_sessions}\n"
            f"Swimming Sessions: {remember.swimming_sessions}\n"
            f"Private Coaching Hours: {remember.coaching_hours}\n"
            f"Total Cost: NPR {total_cost:.2f}"
        )

        result_label = ttk.Label(remember.main_frame, text=result_message, font=("Arial", 16))
        result_label.grid(column=0, row=0, sticky=(tk.W, tk.E), padx=10, pady=10)

        remember.main_frame.columnconfigure(0, weight=1)
        remember.main_frame.rowconfigure(0, weight=1)

def start_building():
    start = tk.Tk()
    app = UNOFitnessGUI(start)
    start.mainloop()

if __name__ == "__main__":
    start_building()
