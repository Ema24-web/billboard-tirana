import tkinter as tk
from tkinter import messagebox
import data_manager
import api_service

def create_window():
    window = tk.Tk()
    window.title("Billboard Interaktiv i Tiranës")
    window.geometry("600x500")
    window.configure(bg="#1a1a2e")

    # TITULLI
    title = tk.Label(
        window,
        text="🏙️ BILLBOARD INTERAKTIV I TIRANËS",
        font=("Arial", 16, "bold"),
        bg="#1a1a2e",
        fg="#e94560"
    )
    title.pack(pady=20)

    # REZULTATI
    result_text = tk.Text(
        window,
        height=15,
        width=65,
        bg="#16213e",
        fg="#ffffff",
        font=("Arial", 10)
    )
    result_text.pack(pady=10)

    def show_result(content):
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, content)

    def btn_events():
        events = data_manager.get_events()
        text = "--- EVENTE KULTURORE ---\n\n"
        for e in events:
            text += f"Titulli : {e['title']}\n"
            text += f"Data    : {e['date']}\n"
            text += f"Vendi   : {e['location']}\n"
            text += "-" * 30 + "\n"
        show_result(text)

    def btn_tourism():
        places = data_manager.get_tourism()
        text = "--- DESTINACIONE TURISTIKE ---\n\n"
        for p in places:
            text += f"Vendi       : {p['name']}\n"
            text += f"Pershkrimi  : {p['description']}\n"
            text += "-" * 30 + "\n"
        show_result(text)

    def btn_restaurants():
        restaurants = data_manager.get_restaurants()
        text = "--- RESTORANTE DHE BARE ---\n\n"
        for r in restaurants:
            text += f"Emri    : {r['name']}\n"
            text += f"Lloji   : {r['type']}\n"
            text += f"Vendi   : {r['location']}\n"
            text += "-" * 30 + "\n"
        show_result(text)

    def btn_emergency():
        emergency = data_manager.get_emergency()
        text = "--- SHERBIMET E URGJENCES ---\n\n"
        for s in emergency:
            text += f"{s['service']} : {s['number']}\n"
        show_result(text)

    def btn_embassies():
        embassies = data_manager.get_embassies()
        text = "--- AMBASADAT ---\n\n"
        for e in embassies:
            text += f"Shteti  : {e['country']}\n"
            text += f"Adresa  : {e['address']}\n"
            text += f"Telefon : {e['phone']}\n"
            text += "-" * 30 + "\n"
        show_result(text)

    def btn_weather():
        weather = api_service.get_weather()
        show_result(f"--- MOTI I TIRANES ---\n\n{weather}")

    # BUTONAT
    buttons = [
        ("🎭 Evente Kulturore", btn_events),
        ("🏛️ Destinacione Turistike", btn_tourism),
        ("🍕 Restorante dhe Bare", btn_restaurants),
        ("🚨 Sherbime Urgjence", btn_emergency),
        ("🏳️ Ambasadat", btn_embassies),
        ("🌤️ Moti i Tiranes", btn_weather),
    ]

    frame = tk.Frame(window, bg="#1a1a2e")
    frame.pack()

    for text, command in buttons:
        btn = tk.Button(
            frame,
            text=text,
            command=command,
            bg="#e94560",
            fg="white",
            font=("Arial", 10, "bold"),
            width=25,
            pady=5
        )
        btn.pack(pady=3)

    window.mainloop()

create_window()
