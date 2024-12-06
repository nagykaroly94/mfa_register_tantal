import cv2

# Kép betöltése
img = cv2.imread('qr1.png')

if img is None:
    print("Nem sikerült betölteni a képet!")
else:
    # QR kód olvasása
    detector = cv2.QRCodeDetector()
    
    # A detectAndDecode() metódus használata a QR kód dekódolásához
    value, pts, qr_code = detector.detectAndDecode(img)

    if value:
        print("QR kód szövege:", value)
    else:
        print("Nem találtunk QR kódot.")
