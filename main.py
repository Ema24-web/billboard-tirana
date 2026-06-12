import ui
import data_manager
import api_service

def run():
    ui.show_header()

    while True:
        ui.show_menu()
        choice = input("Zgjedhja jote: ")

        if choice == "1":
            events = data_manager.get_events()
            ui.show_events(events)

        elif choice == "2":
            places = data_manager.get_tourism()
            ui.show_tourism(places)

        elif choice == "3":
            restaurants = data_manager.get_restaurants()
            ui.show_restaurants(restaurants)

        elif choice == "4":
            emergency = data_manager.get_emergency()
            ui.show_emergency(emergency)

        elif choice == "5":
            embassies = data_manager.get_embassies()
            ui.show_embassies(embassies)

        elif choice == "6":
            weather = api_service.get_weather()
            print(f"\n--- MOTI I TIRANES ---")
            print(weather)

        elif choice == "0":
            print("\nMirupafshim! Gezuar viziten ne Tirane!")
            break

        else:
            print("\nZgjedhje e gabuar! Provo perseri.")

run()