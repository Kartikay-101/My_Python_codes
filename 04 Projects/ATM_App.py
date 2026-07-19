"""MKB ATM — a colourful interactive desktop version of the console project.

Run with: py "04 Projects/ATM_App.py"
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


class MKBATM(tk.Tk):
    BG = "#081A2D"
    PANEL = "#102A43"
    CARD = "#143B5B"
    WHITE = "#F6FAFE"
    MUTED = "#9DB8D0"
    BLUE = "#29A8FF"
    PURPLE = "#806CFF"
    GREEN = "#35D07F"
    RED = "#FF6B7A"

    def __init__(self):
        super().__init__()
        self.title("MKB ATM | Digital Banking")
        self.geometry("1030x650")
        self.minsize(880, 580)
        self.configure(bg=self.BG)
        self.account = None
        self.transactions = []
        self.visible_balance = 0.0
        self.setup_style()
        self.show_create_account()

    def setup_style(self):
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("MKB.TEntry", fieldbackground="#EDF4FA", foreground="#102A43", borderwidth=0, padding=11)

    def clear(self):
        for child in self.winfo_children():
            child.destroy()

    def label(self, parent, text, size=11, color=None, bold=False, **kwargs):
        return tk.Label(parent, text=text, font=("Segoe UI", size, "bold" if bold else "normal"),
                        bg=kwargs.pop("bg", parent.cget("bg")), fg=color or self.WHITE, **kwargs)

    def action_button(self, parent, text, command, color=None, **kwargs):
        return tk.Button(parent, text=text, command=command, cursor="hand2", relief="flat", bd=0,
                         font=("Segoe UI", 10, "bold"), bg=color or self.BLUE, fg="white",
                         activebackground=color or self.BLUE, activeforeground="white", padx=14, pady=10, **kwargs)

    def show_create_account(self):
        self.clear()
        page = tk.Frame(self, bg=self.BG)
        page.pack(fill="both", expand=True)
        # Decorative left panel
        art = tk.Frame(page, bg="#0D3150", width=390)
        art.pack(side="left", fill="both")
        art.pack_propagate(False)
        self.label(art, "MKB", 28, bold=True, bg="#0D3150").pack(anchor="w", padx=45, pady=(55, 0))
        self.label(art, "DIGITAL BANKING", 9, self.BLUE, bold=True, bg="#0D3150").pack(anchor="w", padx=48)
        self.label(art, "Banking that\nfeels effortless.", 30, bold=True, bg="#0D3150", justify="left").pack(anchor="w", padx=45, pady=(92, 16))
        self.label(art, "Create an account, manage your balance,\nand keep track of every transaction.", 11, self.MUTED, bg="#0D3150", justify="left").pack(anchor="w", padx=48)
        bank_card = tk.Frame(art, bg=self.PURPLE, padx=22, pady=16)
        bank_card.pack(side="bottom", fill="x", padx=45, pady=52)
        self.label(bank_card, "MKB • PREMIUM", 10, bold=True, bg=self.PURPLE).pack(anchor="w")
        self.label(bank_card, "••••  ••••  ••••  2026", 16, bg=self.PURPLE).pack(anchor="w", pady=(25, 7))
        self.label(bank_card, "YOUR BANKING, YOUR WAY", 8, "#EDEAFF", bg=self.PURPLE).pack(anchor="w")

        content = tk.Frame(page, bg=self.WHITE)
        content.pack(side="left", fill="both", expand=True)
        form = tk.Frame(content, bg=self.WHITE, width=430)
        form.place(relx=.5, rely=.5, anchor="center")
        self.label(form, "Open your account", 25, self.BG, True, bg=self.WHITE).pack(anchor="w")
        self.label(form, "It only takes a moment to get started.", 11, "#61758A", bg=self.WHITE).pack(anchor="w", pady=(5, 17))
        self.name = self.input(form, "FULL NAME")
        self.phone = self.input(form, "PHONE NUMBER", prefix="+91")
        self.email = self.input(form, "EMAIL ADDRESS")
        self.pin = self.input(form, "CREATE 4-DIGIT PIN", show="●")
        self.balance = self.input(form, "INITIAL DEPOSIT", prefix="₹")
        self.action_button(form, "Create my account  →", self.create_account).pack(fill="x", pady=(20, 0))

    def input(self, parent, caption, prefix=None, show=None):
        self.label(parent, caption, 8, "#4B6074", True, bg=self.WHITE).pack(anchor="w", pady=(8, 4))
        line = tk.Frame(parent, bg="#EDF4FA")
        line.pack(fill="x")
        if prefix:
            self.label(line, prefix, 11, "#607A93", bold=True, bg="#EDF4FA").pack(side="left", padx=(11, 0))
        field = ttk.Entry(line, style="MKB.TEntry", show=show, font=("Segoe UI", 11))
        field.pack(side="left", fill="x", expand=True)
        return field

    def create_account(self):
        name, phone, email = self.name.get().strip().title(), self.phone.get().strip(), self.email.get().strip()
        pin, deposit = self.pin.get().strip(), self.balance.get().strip()
        if not name.replace(" ", "").isalpha(): return self.alert("A full name should contain letters only.")
        if not (phone.isdigit() and len(phone) == 10 and phone[0] in "6789"): return self.alert("Enter a valid 10-digit Indian phone number.")
        if email.count("@") != 1 or not email.lower().endswith(".com"): return self.alert("Enter an email address ending in .com.")
        if not (pin.isdigit() and len(pin) == 4): return self.alert("Your PIN must contain exactly four digits.")
        try:
            balance = float(deposit)
            if balance <= 0: raise ValueError
        except ValueError:
            return self.alert("Initial deposit must be a number greater than ₹0.")
        self.account = {"name": name, "phone": phone, "email": email, "pin": pin, "balance": balance}
        self.transactions = [("Account opened", balance, datetime.now().strftime("Today • %I:%M %p"))]
        self.show_login(True)

    def show_login(self, just_created=False):
        self.clear()
        page = tk.Frame(self, bg=self.BG)
        page.pack(fill="both", expand=True)
        orb = tk.Canvas(page, bg=self.BG, highlightthickness=0)
        orb.place(relwidth=1, relheight=1)
        orb.create_oval(-170, -140, 250, 280, fill="#123D61", outline="")
        orb.create_oval(790, 370, 1150, 730, fill="#172F67", outline="")
        card = tk.Frame(page, bg=self.WHITE, padx=52, pady=45)
        card.place(relx=.5, rely=.5, anchor="center", width=445)
        self.label(card, "MKB", 22, self.BLUE, True, bg=self.WHITE).pack()
        self.label(card, "Welcome back", 24, self.BG, True, bg=self.WHITE).pack(pady=(27 if just_created else 14, 5))
        message = "Your account is ready. Enter your PIN to continue." if just_created else "Enter your secure 4-digit PIN to continue."
        self.label(card, message, 10, "#60758A", bg=self.WHITE, wraplength=320, justify="center").pack()
        self.login_pin = self.input(card, "ATM PIN", show="●")
        self.login_pin.focus()
        self.login_pin.bind("<Return>", lambda event: self.login())
        self.action_button(card, "Unlock dashboard  →", self.login).pack(fill="x", pady=(22, 10))
        tk.Button(card, text="← Create another account", command=self.show_create_account, bg=self.WHITE, fg=self.BLUE, bd=0, cursor="hand2", font=("Segoe UI", 9, "bold")).pack()

    def login(self):
        if self.login_pin.get() == self.account["pin"]:
            self.show_dashboard()
        else:
            self.alert("That PIN does not match. Please try again.")
            self.login_pin.delete(0, tk.END)

    def show_dashboard(self):
        self.clear()
        shell = tk.Frame(self, bg=self.BG)
        shell.pack(fill="both", expand=True)
        side = tk.Frame(shell, bg="#0B2238", width=220)
        side.pack(side="left", fill="y")
        side.pack_propagate(False)
        self.label(side, "MKB", 24, self.BLUE, True, bg="#0B2238").pack(anchor="w", padx=26, pady=(34, 0))
        self.label(side, "DIGITAL BANKING", 8, self.MUTED, True, bg="#0B2238").pack(anchor="w", padx=28)
        self.label(side, "MENU", 8, "#5B7993", True, bg="#0B2238").pack(anchor="w", padx=27, pady=(60, 9))
        for text, command in [("⌂   Dashboard", self.show_dashboard), ("＋  Add money", self.deposit), ("↓   Withdraw", self.withdraw), ("◷   Activity", self.show_history), ("⚙   Account settings", self.show_info)]:
            tk.Button(side, text=text, anchor="w", command=command, bg="#0B2238", fg=self.MUTED, activebackground="#173D5D", activeforeground="white", bd=0, padx=27, pady=11, font=("Segoe UI", 10), cursor="hand2").pack(fill="x")
        tk.Button(side, text="↪  Sign out", anchor="w", command=self.show_login, bg="#0B2238", fg=self.RED, activebackground="#173D5D", bd=0, padx=27, pady=11, font=("Segoe UI", 10, "bold"), cursor="hand2").pack(side="bottom", fill="x", pady=27)
        main = tk.Frame(shell, bg=self.BG, padx=35, pady=29)
        main.pack(side="left", fill="both", expand=True)
        top = tk.Frame(main, bg=self.BG)
        top.pack(fill="x")
        self.label(top, f"Good day, {self.account['name'].split()[0]}!", 23, bold=True, bg=self.BG).pack(side="left")
        self.label(top, datetime.now().strftime("%A, %d %B"), 10, self.MUTED, bg=self.BG).pack(side="right", pady=8)
        self.label(main, "Here is your financial overview.", 10, self.MUTED, bg=self.BG).pack(anchor="w", pady=(2, 20))
        cards = tk.Frame(main, bg=self.BG)
        cards.pack(fill="x")
        balance_card = tk.Frame(cards, bg=self.CARD, padx=25, pady=20)
        balance_card.pack(side="left", fill="x", expand=True, padx=(0, 9))
        self.label(balance_card, "AVAILABLE BALANCE", 9, "#A9CAE2", True, bg=self.CARD).pack(anchor="w")
        self.balance_label = self.label(balance_card, "₹0.00", 30, bold=True, bg=self.CARD)
        self.balance_label.pack(anchor="w", pady=(7, 12))
        self.label(balance_card, "●  Account active", 9, self.GREEN, bg=self.CARD).pack(anchor="w")
        self.visible_balance = 0
        self.animate_balance()
        quick = tk.Frame(cards, bg=self.PURPLE, padx=22, pady=20, width=205)
        quick.pack(side="left", fill="y", padx=(9, 0))
        quick.pack_propagate(False)
        self.label(quick, "QUICK ACTION", 9, "#DDD8FF", True, bg=self.PURPLE).pack(anchor="w")
        self.label(quick, "Need cash?", 17, bold=True, bg=self.PURPLE).pack(anchor="w", pady=(9, 12))
        self.action_button(quick, "Withdraw  →", self.withdraw, "#5B4DD8").pack(anchor="w")
        self.label(main, "MAKE A MOVE", 9, self.MUTED, True, bg=self.BG).pack(anchor="w", pady=(25, 10))
        actions = tk.Frame(main, bg=self.BG)
        actions.pack(fill="x")
        for text, detail, color, command in [("Add money", "Deposit funds", self.BLUE, self.deposit), ("Withdraw", "Take out cash", self.RED, self.withdraw), ("Balance", "View account total", self.GREEN, self.show_balance), ("Change PIN", "Keep it secure", self.PURPLE, self.change_pin)]:
            tile = tk.Button(actions, text=f"{text}\n{detail}   →", command=command, justify="left", anchor="w", cursor="hand2", font=("Segoe UI", 10, "bold"), bg="#102A43", fg="white", activebackground=color, activeforeground="white", bd=0, padx=16, pady=15)
            tile.pack(side="left", fill="x", expand=True, padx=4)
        self.label(main, "RECENT ACTIVITY", 9, self.MUTED, True, bg=self.BG).pack(anchor="w", pady=(25, 9))
        activity = tk.Frame(main, bg="#102A43", padx=18, pady=9)
        activity.pack(fill="both", expand=True)
        latest = list(reversed(self.transactions[-3:]))
        for kind, amount, timestamp in latest:
            row = tk.Frame(activity, bg="#102A43")
            row.pack(fill="x", pady=7)
            sign_color = self.GREEN if amount >= 0 else self.RED
            self.label(row, "●", 13, sign_color, bg="#102A43").pack(side="left")
            self.label(row, kind, 10, bold=True, bg="#102A43").pack(side="left", padx=9)
            self.label(row, timestamp, 9, self.MUTED, bg="#102A43").pack(side="left")
            self.label(row, ("+" if amount >= 0 else "") + self.money(amount), 10, sign_color, True, bg="#102A43").pack(side="right")

    def animate_balance(self):
        target = self.account["balance"]
        step = max(target / 22, 1)
        self.visible_balance = min(target, self.visible_balance + step)
        self.balance_label.configure(text=self.money(self.visible_balance))
        if self.visible_balance < target:
            self.after(18, self.animate_balance)

    def amount_dialog(self, title, subtitle, confirm):
        window = tk.Toplevel(self)
        window.title(title)
        window.configure(bg=self.WHITE)
        window.resizable(False, False)
        window.transient(self); window.grab_set()
        frame = tk.Frame(window, bg=self.WHITE, padx=36, pady=30)
        frame.pack()
        self.label(frame, title, 19, self.BG, True, bg=self.WHITE).pack(anchor="w")
        self.label(frame, subtitle, 10, "#62798E", bg=self.WHITE).pack(anchor="w", pady=(3, 16))
        amount = self.input(frame, "AMOUNT", prefix="₹")
        amount.focus()
        def submit():
            try:
                value = float(amount.get())
                if value <= 0: raise ValueError
            except ValueError:
                return self.alert("Enter an amount greater than ₹0.", window)
            if confirm(value): window.destroy()
        self.action_button(frame, "Confirm  →", submit).pack(fill="x", pady=(20, 0))
        amount.bind("<Return>", lambda event: submit())

    def deposit(self):
        self.amount_dialog("Add money", "Deposit funds into your MKB account.", self.complete_deposit)

    def complete_deposit(self, amount):
        self.account["balance"] += amount
        self.transactions.append(("Money added", amount, datetime.now().strftime("Today • %I:%M %p")))
        self.show_dashboard(); self.toast(f"₹{amount:,.2f} added successfully")
        return True

    def withdraw(self):
        self.amount_dialog("Withdraw cash", "Choose how much you would like to withdraw.", self.complete_withdrawal)

    def complete_withdrawal(self, amount):
        if amount > self.account["balance"]:
            self.alert("Insufficient balance for this withdrawal.")
            return False
        self.account["balance"] -= amount
        self.transactions.append(("Cash withdrawal", -amount, datetime.now().strftime("Today • %I:%M %p")))
        self.show_dashboard(); self.toast(f"₹{amount:,.2f} withdrawn successfully")
        return True

    def show_balance(self):
        self.toast(f"Available balance: {self.money(self.account['balance'])}")

    def show_info(self):
        info = f"Name: {self.account['name']}\nPhone: +91 {self.account['phone']}\nEmail: {self.account['email']}\n\nAvailable balance: {self.money(self.account['balance'])}"
        messagebox.showinfo("Your MKB account", info, parent=self)

    def change_pin(self):
        window = tk.Toplevel(self); window.title("Change PIN"); window.configure(bg=self.WHITE); window.transient(self); window.grab_set()
        frame = tk.Frame(window, bg=self.WHITE, padx=36, pady=30); frame.pack()
        self.label(frame, "Update your PIN", 19, self.BG, True, bg=self.WHITE).pack(anchor="w")
        self.label(frame, "Use a secure four-digit PIN.", 10, "#62798E", bg=self.WHITE).pack(anchor="w", pady=(3, 16))
        current = self.input(frame, "CURRENT PIN", show="●")
        new = self.input(frame, "NEW 4-DIGIT PIN", show="●")
        def save():
            if current.get() != self.account["pin"]: return self.alert("Your current PIN is incorrect.", window)
            if not (new.get().isdigit() and len(new.get()) == 4): return self.alert("New PIN must contain exactly four digits.", window)
            self.account["pin"] = new.get(); window.destroy(); self.toast("Your PIN has been updated")
        self.action_button(frame, "Update PIN  →", save).pack(fill="x", pady=(20, 0))

    def show_history(self):
        history = "\n\n".join(f"{kind}\n{timestamp}    {('+' if amount >= 0 else '')}{self.money(amount)}" for kind, amount, timestamp in reversed(self.transactions))
        messagebox.showinfo("Transaction activity", history or "No transactions yet.", parent=self)

    def toast(self, text):
        toast = tk.Label(self, text="✓  " + text, bg=self.GREEN, fg="#052315", font=("Segoe UI", 10, "bold"), padx=18, pady=10)
        toast.place(relx=.99, rely=.04, anchor="ne")
        self.after(2600, toast.destroy)

    def alert(self, text, parent=None):
        messagebox.showerror("MKB ATM", text, parent=parent or self)

    @staticmethod
    def money(value):
        return f"₹{value:,.2f}"


if __name__ == "__main__":
    MKBATM().mainloop()
