def show_header():
    print("=" * 50)
    print("   TABELA INTERAKTIVE E QYTETIT TE TIRANES")
    print("=" * 50)

def show_menu():
    print("\nZgjedh nje kategori:")
    print("1. Evente Kulturore")
    print("2. Destinacione Turistike")
    print("3. Restorante dhe Bare")
    print("4. Sherbimet e Urgjences")
    print("5. Ambasadat")
    print("6. Moti i Tiranes")
    print("0. Dil nga programi")
    print("-" * 50)

def show_events(events):
    print("\n--- EVENTE KULTURORE ---")
    for event in events:
        print(f"Titulli : {event['title']}")
        print(f"Data    : {event['date']}")
        print(f"Vendi   : {event['location']}")
        print("-" * 30)

def show_tourism(places):
    print("\n--- DESTINACIONE TURISTIKE ---")
    for place in places:
        print(f"Vendi       : {place['name']}")
        print(f"Pershkrimi  : {place['description']}")
        print("-" * 30)

def show_restaurants(restaurants):
    print("\n--- RESTORANTE DHE BARE ---")
    for r in restaurants:
        print(f"Emri    : {r['name']}")
        print(f"Lloji   : {r['type']}")
        print(f"Vendndodhja : {r['location']}")
        print("-" * 30)

def show_emergency(services):
    print("\n--- SHERBIMET E URGJENCES ---")
    for s in services:
        print(f"{s['service']} : {s['number']}")
    print("-" * 30)

def show_embassies(embassies):
    print("\n--- AMBASADAT ---")
    for e in embassies:
        print(f"Shteti  : {e['country']}")
        print(f"Adresa  : {e['address']}")
        print(f"Telefon : {e['phone']}")
        print("-" * 30)