import os
from PyPDF2 import PdfReader


# Get the directory path of the current script file
folder_path = os.path.dirname(os.path.abspath(__file__))

# Get a list of PDF file names in the folder
pdf_files = [f for f in os.listdir(folder_path) if f.endswith(".pdf")]

# Ask the user for the price per print/page
price_page = float(input("What is the price per print/page? "))

# Loop through each PDF file and count the pages
tot_page = 0
for pdf_file in pdf_files:
    with open(os.path.join(folder_path, pdf_file), "rb") as file:
        pdf_reader = PdfReader(file)
        page_count = len(pdf_reader.pages)
        tot_page += page_count

# Calculate the total price based on the total number of pages and the price per page
total_price = tot_page * price_page

# Output the total number of pages and the total price
print(f"Total page count: {tot_page}")
print(f"The total price for your prints should be {total_price}")
