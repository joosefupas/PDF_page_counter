import os
from PyPDF2 import PdfReader
import tkinter as tk
from tkinter import filedialog


class PDFCounter(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("PDF Page Counter")
        self.master.geometry("400x150")
        self.create_widgets()

    def create_widgets(self):
    # Create label and entry for price per page
        self.price_label = tk.Label(self.master, text="Price per page:")
        self.price_label.grid(row=0, column=0)
        self.price_entry = tk.Entry(self.master)
        self.price_entry.grid(row=0, column=1)

        # Create button to select folder
        self.folder_button = tk.Button(self.master, text="Select folder", command=self.select_folder)
        self.folder_button.grid(row=1, column=0)

        # Create label to display selected folder
        self.folder_label = tk.Label(self.master, text="No folder selected.")
        self.folder_label.grid(row=1, column=1)

        # Create button to count pages
        self.count_button = tk.Button(self.master, text="Count", command=self.count_pages)
        self.count_button.grid(row=2, column=0)

        # Create label to display total number of pages
        self.page_count_label = tk.Label(self.master, text="")
        self.page_count_label.grid(row=2, column=1)

        # Create label to display total price
        self.total_price_label = tk.Label(self.master, text="")
        self.total_price_label.grid(row=3, column=1)

        # Create signature label
        self.signature_label = tk.Label(self.master, text="@joosefupas")
        self.signature_label.grid(row=4, column=1)

    def select_folder(self):
        # Open dialog to select folder
        folder_path = filedialog.askdirectory()
        self.folder_label.config(text=folder_path)

    def count_pages(self):
    # Get the selected folder path and price per page
        folder_path = self.folder_label.cget("text")
        price_entry_value = self.price_entry.get()

        if price_entry_value == "":
            price_page = 0
        else:
            price_page = float(price_entry_value)

    # Get a list of PDF file names in the folder
        pdf_files = [f for f in os.listdir(folder_path) if f.endswith(".pdf")]

    # Loop through each PDF file and count the pages
        tot_page = 0
        for pdf_file in pdf_files:
            with open(os.path.join(folder_path, pdf_file), "rb") as file:
                pdf_reader = PdfReader(file)
                page_count = len(pdf_reader.pages)
                tot_page += page_count

     # Calculate the total price based on the total number of pages and the price per page
        total_price = tot_page * price_page

        # Update the page count label with the total number of pages
        self.page_count_label.config(text=f"Total page count: {tot_page}")

        # Update the total price label with the total price
        self.total_price_label.config(text=f"Total price: {total_price}")

        # Output the total number of pages and the total price
        print(f"Total page count: {tot_page}")
        print(f"The total price for your prints should be {total_price}")
       


root = tk.Tk()
app = PDFCounter(master=root)
app.mainloop()
