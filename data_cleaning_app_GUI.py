import pandas as pd
import os
from pandas.api.types import is_numeric_dtype
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog, messagebox

# Function to clean dataset
def data_cleaning_master(data_path, data_name):
    """Cleans dataset, removes duplicates, handles missing values, and saves the cleaned file."""

    if not os.path.exists(data_path):
        messagebox.showerror("Error", "❌ Incorrect file path! Please select a valid file.")
        return
    
    # Read file based on type
    if data_path.endswith('.csv'):
        df = pd.read_csv(data_path, encoding_errors='ignore')
    elif data_path.endswith('.xlsx'):
        df = pd.read_excel(data_path)
    else:
        messagebox.showerror("Error", "⚠️ Unknown file type! Please select a CSV or Excel file.")
        return

    # Check for duplicates
    total_duplicates = df.duplicated().sum()
    
    # Save duplicate records (if any)
    if total_duplicates > 0:
        duplicate_records = df[df.duplicated()]
        duplicate_records.to_csv(f'{data_name}_duplicates.csv', index=False)

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    for col in df.columns:
        if is_numeric_dtype(df[col]):
            df[col].fillna(df[col].mean(), inplace=True)
        else:
            df.dropna(subset=[col], inplace=True)

    # Save cleaned dataset
    cleaned_file = f'{data_name}_Cleaned_data.csv'
    df.to_csv(cleaned_file, index=False)

    # Show success message
    messagebox.showinfo("Success", f"✅ Data cleaned and saved as {cleaned_file}")

# Function to browse file
def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV & Excel Files", "*.csv;*.xlsx"), ("CSV Files", "*.csv"), ("Excel Files", "*.xlsx")])
    entry_path.delete(0, ttk.END)
    entry_path.insert(0, file_path)

# Function to clean data
def clean_data():
    data_path = entry_path.get()
    data_name = entry_name.get()
    
    if not data_path or not data_name:
        messagebox.showwarning("Warning", "⚠️ Please provide both file path and dataset name.")
        return
    
    progress_bar.start(10)
    data_cleaning_master(data_path, data_name)
    progress_bar.stop()

# Initialize Tkinter app with ttkbootstrap theme
root = ttk.Window(themename="darkly")
root.title("🧼 Data Cleaning App")
root.geometry("420x300")
root.resizable(False, False)

# Title Label
title_label = ttk.Label(root, text="Data Cleaning Tool", font=("Arial", 16, "bold"), bootstyle="info")
title_label.pack(pady=10)

# File Selection
frame = ttk.Frame(root)
frame.pack(pady=5)

entry_path = ttk.Entry(frame, width=35)
entry_path.pack(side=LEFT, padx=5)
browse_button = ttk.Button(frame, text="📂 Browse", bootstyle="primary", command=browse_file)
browse_button.pack(side=RIGHT)

# Dataset Name Input
ttk.Label(root, text="Dataset Name:", font=("Arial", 11), bootstyle="light").pack(pady=5)
entry_name = ttk.Entry(root, width=30)
entry_name.pack()

# Clean Data Button
clean_button = ttk.Button(root, text="🧹 Clean Data", bootstyle="success-outline", command=clean_data)
clean_button.pack(pady=15)

# Progress Bar
progress_bar = ttk.Progressbar(root, mode='indeterminate', bootstyle="success-striped")
progress_bar.pack(fill=X, padx=20)

# Run the GUI
root.mainloop()
