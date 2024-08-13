# Name: Georgia Vrana
# Date Submitted: Tuesday, April 23rd, 2024
# Assignment-12: GUI Contact Form
# Description: This Python program creates a GUI contact form where users can enter their first name,
#              last name, address, city, postal code, and select a province from a dropdown menu;
#              upon submission, it displays the entered information in a message box.

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def submit():
    # Retrieve values from GUI elements
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    address = address_entry.get()
    city = city_entry.get()
    postal_code = postal_code_entry.get()
    province = province_combo.get()

    # Format output string
    output_message = f"{first_name} {last_name}\n{address}\n{city}, {province}\n{postal_code}"

    # Display a message box with the contact information
    messagebox.showinfo("Contact Information", output_message)

# Initialize the root window
root = tk.Tk()
root.title("Contact Form")
root.geometry('400x300')

# Create labels
first_name_label = tk.Label(root, text="First Name:")
last_name_label = tk.Label(root, text="Last Name:")
address_label = tk.Label(root, text="Address:")
city_label = tk.Label(root, text="City:")
postal_code_label = tk.Label(root, text="Postal Code:")
province_label = tk.Label(root, text="Province:")

# Create entry widgets
first_name_entry = tk.Entry(root)
first_name_entry.insert(0, "John")  # Default value
last_name_entry = tk.Entry(root)
last_name_entry.insert(0, "Doe")   # Default value
address_entry = tk.Entry(root)
address_entry.insert(0, "148 Python Ave")
city_entry = tk.Entry(root)
city_entry.insert(0, "Peterborough")
postal_code_entry = tk.Entry(root)
postal_code_entry.insert(0, "K9J 8M4")

# Create a combobox for province selection with full province names
province_combo = ttk.Combobox(root, values=[
    "British Columbia", "Alberta", "Saskatchewan", "Manitoba", "Ontario", 
    "Quebec", "Prince Edward Island", "New Brunswick", "Nova Scotia", 
    "Newfoundland and Labrador", "Yukon", "Northwest Territories", "Nunavut"
])
province_combo.set("Ontario")  # Default value

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=submit)

# Layout the GUI elements using grid
first_name_label.grid(row=0, column=0, padx=10, pady=3, sticky='w')
first_name_entry.grid(row=0, column=1, padx=10, pady=3, sticky='e')
last_name_label.grid(row=1, column=0, padx=10, pady=3, sticky='w')
last_name_entry.grid(row=1, column=1, padx=10, pady=3, sticky='e')
address_label.grid(row=2, column=0, padx=10, pady=3, sticky='w')
address_entry.grid(row=2, column=1, padx=10, pady=3, sticky='e')
city_label.grid(row=3, column=0, padx=10, pady=3, sticky='w')
city_entry.grid(row=3, column=1, padx=10, pady=3, sticky='e')
postal_code_label.grid(row=4, column=0, padx=10, pady=3, sticky='w')
postal_code_entry.grid(row=4, column=1, padx=10, pady=3, sticky='e')
province_label.grid(row=5, column=0, padx=10, pady=3, sticky='w')
province_combo.grid(row=5, column=1, columnspan=4, padx=10, pady=3, sticky='e')
submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()