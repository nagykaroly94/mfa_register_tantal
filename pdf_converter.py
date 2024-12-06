import docx2pdf
import os
from tkinter import messagebox

input_folder = '.'  # specify the folder containing the input files
output_folder = '.'  # specify the folder where the PDF files will be saved

# get a list of all the docx files in the input folder
input_files = [f for f in os.listdir(input_folder) if f.endswith('.docx')]

# loop over each input file and convert it to PDF
for input_file in input_files:
    # construct the input and output file paths
    input_path = os.path.join(input_folder, input_file)
    output_file = input_file.replace('.docx', '.pdf')
    output_path = os.path.join(output_folder, output_file)

    # convert the input file to PDF using docx2pdf
    docx2pdf.convert(input_path, output_path)

    messagebox.showinfo("Siker", f"A következő fájl PDF-be való konvertálása sikeresen befejeződött: {input_file}")
    print("Kész")