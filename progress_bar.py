import tkinter as tk
from tkinter import ttk, messagebox
from docx2pdf import convert
import threading  # A konvertálás külön szálon történik, hogy ne fagyjon le a GUI

def convert_single_docx_to_pdf(input_file):

    # Új ablak a progress bar számára
    progress_window = tk.Toplevel()
    progress_window.title("Folyamat")

    # Progress bar widget
    progress_bar = ttk.Progressbar(progress_window, orient="horizontal", length=300, mode="determinate")
    progress_bar.grid(row=0, column=0, padx=20, pady=20)
    progress_bar["maximum"] = 100
    progress_bar["value"] = 0  # Kezdeti érték

    # Üzenet a folyamat állapotáról
    status_label = tk.Label(progress_window, text="Fájl konvertálása folyamatban...")
    status_label.grid(row=1, column=0, padx=20, pady=5)

    def update_progress():
        # Ha a fájl nem .docx, akkor hibaüzenet
        if not input_file.endswith('.docx'):
            messagebox.showerror("Hiba", "A megadott fájl nem .docx formátumú!")
            progress_window.destroy()
            return

        # A kimeneti PDF fájl neve
        output_file = input_file.replace('.docx', '.pdf')

        try:
            # Itt a fájl konvertálása, ezt indítjuk el külön szálon
            convert(input_file, output_file)
            progress_bar["value"] = 100
            # A progress bar beállítása 100%-ra, ha a konvertálás befejeződik
            status_label.config(text="A PDF generálása sikeres!")

            # Visszajelzés a felhasználónak
            messagebox.showinfo("Siker", f"A PDF generálása sikeres: {output_file}")

        except Exception as e:
            # Ha hiba történik, progress bar 0-ra állítása és hibaüzenet
            progress_bar["value"] = 0
            messagebox.showerror("Hiba", f"Nem sikerült a konvertálás: {e}")

        finally:
            # A progress bar után bezárjuk az ablakot
            progress_window.after(1000, progress_window.destroy)

    # Futtatás külön szálon, hogy a GUI ne fagyjon le
    threading.Thread(target=update_progress).start()

# Példa gomb a fájl konvertálására
root = tk.Tk()
root.title("PDF Konvertálás")

convert_button = tk.Button(root, text="Dokumentum konvertálása", command=lambda: convert_single_docx_to_pdf("Ketlepcsos_Hitelesites_Sablon_Letoltesekkel.docx"))
convert_button.pack(padx=20, pady=20)

root.mainloop()
