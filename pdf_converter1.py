from docx2pdf import convert
from tkinter import messagebox
import os

def convert_single_docx_to_pdf():

    file = "C:/Users/ugyfel/Desktop/Landa/Ketlepcsos_Hitelesites_Sablon_Letoltesekkel.docx"
    input_file = file
    if not input_file.endswith('.docx'):
        messagebox.showerror("Hiba", "A megadott fájl nem .docx formátumú!")
        return

    # A kimeneti PDF fájl neve
    output_file = input_file.replace('.docx', '.pdf')

    try:
        # Konvertálás PDF-be
        convert(input_file, output_file)
        messagebox.showinfo("Siker", f"A PDF generálása sikeres: {output_file}")
    except Exception as e:
        messagebox.showerror("Hiba", f"Nem sikerült a PDF fájl generálása: {e}")

convert_single_docx_to_pdf()