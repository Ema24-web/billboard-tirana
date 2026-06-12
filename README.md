# Billboard Interaktiv i Qytetit të Tiranës

## Përshkrimi
Ky program simulon një tabelë informacioni interaktive për qytetin e Tiranës.
Ofron informacione për turistët dhe qytetarët për evente, turizëm, restorante,
shërbime urgjence dhe ambasada.

## Teknologjitë e Përdorura
- Python 3.x
- Libraria: requests, json, datetime
- IDE: PyCharm

## Struktura e Projektit
billboard_tirana/
├── main.py           # Fajlli kryesor
├── ui.py             # Ndërfaqja me përdoruesin
├── data_manager.py   # Menaxhimi i të dhënave
├── api_service.py    # Shërbimi i motit (API)
├── data/
│   └── data.json     # Databaza e të dhënave
└── README.md         # Dokumentacioni

## Si Instalohet
1. Instalo Python 3.x
2. Instalo librarine requests:
   pip install requests
3. Hap projektin në PyCharm
4. Ekzekuto main.py

## Si Përdoret
Pas ekzekutimit të main.py, zgjedh një kategori:
- 1: Evente Kulturore
- 2: Destinacione Turistike
- 3: Restorante dhe Bare
- 4: Shërbimet e Urgjencës
- 5: Ambasadat
- 6: Moti i Tiranës (live)
- 0: Dil nga programi



## Universiteti
Informatikë Biznesi - Viti i Parë