import math
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate_installments(payment_value,payment_method):
    # Calculate 7% of the payment value
    installment_amount = payment_value + calculate_servicecharge(payment_value,payment_method)
    # Divide the payment into 4 installments
    installment_amount = installment_amount / 4
    return installment_amount


def calculate_servicecharge(payment_value, payment_method):
    # Calculate 7% of the payment value
    if payment_method == 'Tabby':
        percent = 6.9 / 100
        service_charge = payment_value * percent
    elif payment_method == 'payment link':
        percent = 3 / 100
        service_charge = payment_value * percent
    elif payment_method == 'Card':
        percent = 2.5 / 100
        service_charge = payment_value * percent
    else:
        service_charge = 0

    return service_charge


def calculate_button_clicked():
    try:
        payment_value = float(payment_entry.get())
        payment_method = payment_methods_combobox.get()

        # Calculate the installments
        installment_amount = calculate_installments(payment_value,payment_method)
        servicecharge = calculate_servicecharge(payment_value,payment_method)

        # Display the results
        result_text = f"Payment Method: {payment_method}\n"
        result_text += f"Payment Value: ${payment_value:.2f}\n"
        result_text += f"Service Charge: ${servicecharge:.2f}\n"
        if payment_method == 'Tabby':
            result_text += f"Installment 1: ${installment_amount:.2f}\n"
            result_text += f"Installment 2: ${installment_amount:.2f}\n"
            result_text += f"Installment 3: ${installment_amount:.2f}\n"
            result_text += f"Installment 4: ${installment_amount:.2f}"
    

        result_label.config(text=result_text)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for Payment Value.")


# Create main window
root = tk.Tk()
root.title("Installment Calculator")

# Payment methods
payment_methods = ['Cash', 'Card', 'payment link','Tabby']

# Payment Value
payment_label = ttk.Label(root, text="Enter Payment Value:")
payment_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

payment_entry = ttk.Entry(root)
payment_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

# Payment Method
payment_method_label = ttk.Label(root, text="Select Payment Method:")
payment_method_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

payment_methods_combobox = ttk.Combobox(root, values=payment_methods, state="readonly")
payment_methods_combobox.current(0)
payment_methods_combobox.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

# Calculate button
calculate_button = ttk.Button(root, text="Calculate", command=calculate_button_clicked)
calculate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

# Result
result_label = ttk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

root.mainloop()
