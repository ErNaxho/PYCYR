import tkinter as tk
from tkinter import messagebox

class ATMSimulator:
    def __init__(self, root):
        self.balance = 0

        self.root = root
        self.root.title("ATM Simulator")

        self.balance_label = tk.Label(root, text=f"Balance: ${self.balance}", font=("Arial", 14))
        self.balance_label.pack(pady=10)

        self.amount_label = tk.Label(root, text="Enter Amount:", font=("Arial", 12))
        self.amount_label.pack()

        self.amount_entry = tk.Entry(root, font=("Arial", 12))
        self.amount_entry.pack(pady=5)

        self.deposit_button = tk.Button(root, text="Deposit", font=("Arial", 12), command=self.deposit)
        self.deposit_button.pack(pady=5)

        self.withdraw_button = tk.Button(root, text="Withdraw", font=("Arial", 12), command=self.withdraw)
        self.withdraw_button.pack(pady=5)

    def deposit(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                raise ValueError("Amount must be positive.")
            self.balance += amount
            self.update_balance()
            messagebox.showinfo("Success", f"${amount} deposited successfully!")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def withdraw(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                raise ValueError("Amount must be positive.")
            if amount > self.balance:
                raise ValueError("Insufficient balance.")
            self.balance -= amount
            self.update_balance()
            messagebox.showinfo("Success", f"${amount} withdrawn successfully!")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def update_balance(self):
        self.balance_label.config(text=f"Balance: ${self.balance}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ATMSimulator(root)
    root.mainloop()