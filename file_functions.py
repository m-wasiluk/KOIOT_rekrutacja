import os
from datetime import datetime
from light_bulb import Light_bulb


def check_memory():
    """
    Funkcja odczytuje informacje z pliku 'memory.txt',
    ktory przechowuje nazwy plikow przedstawiajacych stan zapisanych zarowek.
    """
    light_bulbs_files = []
    try:
        with open("memory.txt", "r") as file_handle:
            for line in file_handle.readlines():
                light_bulbs_files.append(line.rstrip('\n'))
        return light_bulbs_files
    except Exception:
        with open("memory.txt", "w") as file_handle:
            pass
        return light_bulbs_files


def load_light_bulbs():
    """
    Funkcja odczytuje zarowki z kazdego zapisanego pliku oraz
    zapisuje je w liscie zarowek, ktora na koniec zwraca.
    """
    light_bulbs_files = check_memory()
    light_bulbs = []
    for path in light_bulbs_files:
        if path == "":
            continue
        with open(path, "r") as file_handle:
            data = file_handle.readlines()
            light_bulbs.append(Light_bulb(
                int(data[1].rstrip("\n")), data[3].rstrip("\n"),
                int(data[5].rstrip("\n")), data[7].rstrip("\n"),
                datetime.fromisoformat(data[9].rstrip('\n')),
                int(data[11].rstrip("\n"))
            ))
    return light_bulbs


def save_light_bulbs(light_bulbs: list[Light_bulb]):
    """
    Funkcja zapisuje zarowki, ktore sa przekazane jako argument funkcji
    w formie listy obiektow typu 'Light_bulb'.
    Kazda zarowka ma swoj oddzielny plik, a informacje o nazwach
    zapisanych plikow przechowywane sa w pliku 'memory.txt'.

    Format zapisywania zarowek do plikow:
    Zarowka numer:
    {number}
    Natezenie swiatla:
    {intensity}
    Kolor zarowki:
    {colour}
    Data zainstalowania:
    {creation_time}
    Oczekiwane zakonczenie pracy:
    {approx_life_duration}
    """
    for path in check_memory():
        if path == "":
            continue
        os.remove(path)
    with open("memory.txt", "w") as file_handle:
        file_handle.write("")
    for light_bulb in light_bulbs:
        with open(f"light_bulb{light_bulb.get_number()}.txt",
                  "w") as file_handle:
            file_handle.write("Zarowka numer:\n")
            file_handle.write(f"{str(light_bulb.get_number())}\n")
            file_handle.write("Stan zarowki:\n")
            file_handle.write(f"{light_bulb.get_switch_state()}\n")
            file_handle.write("Natezenie swiatla:\n")
            file_handle.write(f"{str(light_bulb.get_intensity())}\n")
            file_handle.write("Kolor zarowki:\n")
            file_handle.write(f"{light_bulb.get_colour()}\n")
            file_handle.write("Data zainstalowania:\n")
            file_handle.write(
                f"{light_bulb.get_creation_time().isoformat()}\n")
            file_handle.write("Spodziewany czas pracy w latach:\n")
            file_handle.write(
                f"{str(light_bulb.get_approx_life_duration())}\n")
        with open("memory.txt", "a") as file_handle:
            file_handle.write(f"\nlight_bulb{light_bulb.get_number()}.txt")
    print("Pomyslnie wykonano zapis.")
