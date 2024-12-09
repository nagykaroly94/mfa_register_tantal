
# Tantál - Ügyfélkezelő alkalmazás

A Tantál egy GUI alapú Python-alkalmazás, amely ügyfélkezelési funkciókat valósít meg. Az alkalmazás adatbázis-kezeléssel, QR-kód generálással és dokumentumok exportálásával segíti az ügyfelek kezelését.

---

## Függőségek

Az alkalmazás a következő Python-könyvtárakat használja:
- **`mysql.connector`**: Az adatbázis kapcsolatért.
- **`tkinter`**: Grafikus felület létrehozására.
- **`qrcode`**: QR-kód generálására.
- **`Pillow` (`PIL`)**: Képek feldolgozására.
- **`opencv-python` (`cv2`)**: QR-kódok olvasására.
- **`python-docx`**: Dokumentumok (Word fájlok) generálására.

---

## Fő funkciók

### 1. Adatbázis kapcsolat létrehozása
A `db_kapcsolodas()` függvény inicializálja az adatbázis kapcsolatot egy konfigurációs fájl segítségével, amely tartalmazza az adatbázis elérhetőségi információit.

### 2. Ügyfelek kezelése
- **Új ügyfél hozzáadása**: 
  A `ugyfel_megad()` függvény begyűjti az adatokat a GUI `Entry` mezőiből, majd azokat menti az adatbázisba.
  
- **Ügyfél törlése**:
  A `kijelolt_adat_torles()` funkció egy kiválasztott ügyfelet töröl az adatbázisból, és frissíti a GUI elemeket.

- **Adatok frissítése**:
  A `ugyfel_frissites()` lehetőséget biztosít az ügyfél adatainak módosítására, majd az adatbázisban történő frissítésére.

### 3. QR-kódok kezelése
- **QR-kód generálása**:
  A `generate_qr(data)` függvény létrehoz egy QR-kódot a megadott adatok alapján.
  
- **QR-kód olvasása**:
  A `qr_read()` funkció egy megadott képfájlból dekódolja a QR-kód tartalmát.

### 4. Adatok keresése
A `search_ceg()` funkció segítségével az adatbázisban található cégnév alapján kereshetünk.

### 5. Dokumentum exportálása
A `export_document(treeview, qr_canvas)` funkció létrehoz egy `.docx` formátumú dokumentumot az aktuálisan kiválasztott ügyfél adataival, beleértve a QR-kód képét.

### 6. GUI funkciók
- **Treeview és oszlopok**:
  Az ügyfelek adatait egy `Treeview` widget mutatja be.
- **Gombok és keresőmezők**:
  Különböző `Button` widgetek kezelik az adatbázis-műveleteket és egyéb funkciókat.
- **QR-kód megjelenítés**:
  Egy `Canvas` widget jeleníti meg az aktuálisan kiválasztott QR-kódot.

---

## Főbb widgetek és elrendezés
- **Treeview**:
  Az ügyfelek adatainak megjelenítésére szolgál.
  
- **QR-kód frame**:
  Középen jeleníti meg az aktuális QR-kódot.
  
- **Adatbevitel**:
  Egy `data_frame` nevű frame tartalmazza az adatbevitelhez szükséges mezőket és gombokat.

- **Keresés**:
  Egy keresőmező segítségével gyorsan lekérdezhetők az ügyfelek adatai.

---

## Hibakezelés
- Az adatbázis kapcsolat hibáit a `messagebox` jeleníti meg.
- Hiányzó adatokat a program hibaüzenettel jelzi.

---

## Használati lépések
1. **Adatok hozzáadása**:
   - Töltsd ki az adatmezőket.
   - Kattints az "Új ügyfél hozzáadása" gombra.
2. **QR-kód kiválasztása vagy generálása**:
   - A QR-kódot megjelenítheted az ügyfél adataira kattintva.
3. **Adatok törlése/frissítése**:
   - Válassz ki egy ügyfelet a `Treeview`-ben.
   - Használd a törlés vagy frissítés gombokat.
4. **Dokumentum exportálása**:
   - Válaszd ki az ügyfelet, majd kattints a "Dokumentum létrehozása" gombra.

---

## Futtatás
1. Telepítsd a függőségeket:
   ```bash
   pip install mysql-connector-python qrcode pillow opencv-python python-docx
   ```
2. Biztosítsd, hogy az `config.ini` fájl tartalmazza az adatbázis elérhetőségi adatait.
3. Futtasd a programot:
   ```bash
   python tantal.py
   ```

---

## Jövőbeni fejlesztési lehetőségek
- Adatbázis biztonságának növelése (pl. titkosítás).
- További vizuális testreszabás (pl. téma kiválasztása).
- Többnyelvűség támogatása.
