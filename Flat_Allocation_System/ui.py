import tkinter as tk
from tkinter import messagebox
from backend import (
    get_flats,
    get_tenants,
    get_payments,
    add_tenant,
    allocate_flat,
    add_payment
)



# ---------- MAIN WINDOW ----------
root = tk.Tk()
root.title("Flat Allocation Management System")
root.geometry("850x600")

tk.Label(
    root,
    text="Flat Allocation Management System",
    font=("Arial", 18, "bold")
).pack(pady=10)

# ---------- OUTPUT ----------
output = tk.Text(root, height=22, width=95, font=("Courier New", 10))
output.pack(pady=10)

# ---------- VIEW FLATS ----------
def show_flats():
    output.delete(1.0, tk.END)
    flats = get_flats()

    for f in flats:
        output.insert(tk.END, f"""
Flat ID     : {f[0]}
Flat Number : {f[1]}
Floor       : {f[2]}
Type        : {f[3]}
Rent (₹)    : {f[4]}
Status      : {f[5]}
-------------------------------
""")

# ---------- VIEW TENANTS ----------
def show_tenants():
    output.delete(1.0, tk.END)
    tenants = get_tenants()

    for t in tenants:
        output.insert(tk.END, f"""
Tenant ID  : {t[0]}
Name       : {t[1]}
Phone      : {t[2]}
ID Proof   : {t[3]}
Join Date  : {t[4]}
-------------------------------
""")
        
# ---------- VIEW PAYMENTS ----------
def show_payments():
    output.delete(1.0, tk.END)
    payments = get_payments()

    for p in payments:
        output.insert(tk.END, f"""
Payment ID : {p[0]}
Tenant     : {p[1]}
Month      : {p[2]}
Amount (₹) : {p[3]}
Status     : {p[4]}
-------------------------------
""")


# ---------- ADD TENANT ----------
def add_tenant_ui():
    win = tk.Toplevel(root)
    win.title("Add Tenant")
    win.geometry("320x260")

    labels = ["Name", "Phone", "ID Proof", "Join Date (YYYY-MM-DD)"]
    entries = []

    for i, l in enumerate(labels):
        tk.Label(win, text=l).grid(row=i, column=0, pady=5)
        e = tk.Entry(win)
        e.grid(row=i, column=1)
        entries.append(e)

    def submit():
        add_tenant(
            entries[0].get(),
            entries[1].get(),
            entries[2].get(),
            entries[3].get()
        )
        messagebox.showinfo("Success", "Tenant added successfully")
        win.destroy()

    tk.Button(win, text="Add Tenant", command=submit)\
        .grid(row=4, columnspan=2, pady=10)

# ---------- ALLOCATE FLAT ----------
def allocate_flat_ui():
    win = tk.Toplevel(root)
    win.title("Allocate Flat")
    win.geometry("320x220")

    labels = ["Tenant ID", "Flat ID", "Start Date (YYYY-MM-DD)"]
    entries = []

    for i, l in enumerate(labels):
        tk.Label(win, text=l).grid(row=i, column=0, pady=5)
        e = tk.Entry(win)
        e.grid(row=i, column=1)
        entries.append(e)

    def submit():
        allocate_flat(
            entries[0].get(),
            entries[1].get(),
            entries[2].get()
        )
        messagebox.showinfo("Success", "Flat allocated successfully")
        win.destroy()
        show_flats()

    tk.Button(win, text="Allocate", command=submit)\
        .grid(row=3, columnspan=2, pady=10)

# ---------- ADD PAYMENT ----------
def add_payment_ui():
    win = tk.Toplevel(root)
    win.title("Add Payment")
    win.geometry("350x260")

    labels = [
        "Tenant ID (who is paying)",
        "Rent Month (YYYY-MM)",
        "Amount Paid (₹)",
        "Payment Status (Paid / Pending)"
    ]
    entries = []

    for i, l in enumerate(labels):
        tk.Label(win, text=l).grid(row=i, column=0, pady=5)
        e = tk.Entry(win)
        e.grid(row=i, column=1)
        entries.append(e)

    def submit():
        add_payment(
            entries[0].get(),
            entries[1].get(),
            entries[2].get(),
            entries[3].get()
        )
        messagebox.showinfo("Success", "Payment recorded successfully")
        win.destroy()

    tk.Button(win, text="Add Payment", command=submit)\
        .grid(row=4, columnspan=2, pady=10)

# ---------- BUTTONS ----------
btns = tk.Frame(root)
btns.pack(pady=10)

tk.Button(btns, text="View Flats", width=20, command=show_flats)\
    .grid(row=0, column=0, padx=5)

tk.Button(btns, text="View Tenants", width=20, command=show_tenants)\
    .grid(row=0, column=1, padx=5)

tk.Button(btns, text="Add Tenant", width=20, command=add_tenant_ui)\
    .grid(row=0, column=2, padx=5)

tk.Button(btns, text="Allocate Flat", width=20, command=allocate_flat_ui)\
    .grid(row=1, column=0, padx=5)

tk.Button(btns, text="Add Payment", width=20, command=add_payment_ui)\
    .grid(row=1, column=1, padx=5)

tk.Button(root, text="Exit", width=20, command=root.destroy)\
    .pack(pady=10)
tk.Button(btns, text="View Payments", width=20, command=show_payments)\
    .grid(row=1, column=2, padx=5)

root.mainloop()
