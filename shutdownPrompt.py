import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

def perform_action(action):
    if action == "Sleep":
        os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
    elif action == "Hibernate":
        os.system('rundll32.exe powrprof.dll,SetSuspendState 1,1,0')
    elif action == "Shutdown":
        os.system('shutdown /s /t 1')
    elif action == "Do Nothing":
        messagebox.showinfo("No action selected", "No action was selected.")
    root.destroy()  # Close the window after performing the action

def on_dropdown_change(event):
    selected_action = dropdown.get()
    perform_action(selected_action)

# Create the main window
root = tk.Tk()
root.title("System Control")

# Create a label
label = tk.Label(root, text="Select an action:")
label.pack(pady=10)

# Create a dropdown list
actions = ["Sleep", "Hibernate", "Shutdown", "Do Nothing"]
dropdown = ttk.Combobox(root, values=actions)
dropdown.set("Select an action")
dropdown.pack(pady=10)

# Bind the dropdown change event to the function
dropdown.bind("<<ComboboxSelected>>", on_dropdown_change)

# Run the GUI
root.mainloop()
