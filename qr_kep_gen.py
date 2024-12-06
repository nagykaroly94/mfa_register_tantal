import qrcode
from PIL import Image

# QR-kód generálása
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=1)
qr.add_data("Random QR Code Data")
qr.make(fit=True)

# Kép létrehozása és kicsinyítése
img = qr.make_image(fill="black", back_color="white")
small_img = img.resize((64, 64))  # 64x64 pixel ikon méret

# Mentés .ico formátumban
small_img.save("ikon.ico", format="ICO")
