from time import sleep
from file_functions import load_light_bulbs, save_light_bulbs
import ui

# zaladowanie zapisanych zarowek
light_bulbs = load_light_bulbs()

choice = None

while (choice != "zakończ"):
    print("\nWitaj w programie zarzadzajacym Twoimi zarowkami!")
    print(f'Aktualnie masz {len(light_bulbs)} zarowek.')
    print("Co chcesz zrobic?")
    print("Wpisz 'stan' aby wyswietlic stan zarowek.")
    print("Wpisz 'nowa', aby stworzyc nowa zarowke.")
    print("Wpisz 'usun' aby usunac istniejaca zarowke.")
    print("Wpisz 'edytuj' aby edytowac istniejaca zarowke")
    print("Wpisz 'wlacz' aby wlaczyc wszystkie zarowki na raz.")
    print("Wpisz 'wylacz' aby wylaczyc wszystkie zarowki na raz")
    print("Wpisz 'zapisz' aby zapisac zmiany dokonane w "
          "trakcie dzialania tego programu.")
    print("Wpisz 'zakoncz' aby zakonczyc dzialanie programu.")
    print("Pamietaj, ze po zapisaniu i wylaczeniu programu możesz sprawdzić "
          "stan swoich zarówek w plikach 'light_bulbs.txt'.")

    choice = input()
    print("\033c", end='')

    if choice == "stan":
        ui.display_state(light_bulbs)
    elif choice == "nowa":
        light_bulbs.append(ui.create_new_light_bulb(len(light_bulbs)))
    elif choice == "usun":
        ui.remove_light_bulb(light_bulbs)
    elif choice == "edytuj":
        ui.edit_light_bulb(light_bulbs)
    elif choice == "wlacz":
        ui.turn_on_all(light_bulbs)
    elif choice == "wylacz":
        ui.turn_off_all(light_bulbs)
    elif choice == "zapisz":
        save_light_bulbs(light_bulbs)
    elif choice == "zakoncz":
        print("Do widzenia")
        sleep(1)
        break
    else:
        print("Podano inna opcje, niz mozliwa do wybrania.")
