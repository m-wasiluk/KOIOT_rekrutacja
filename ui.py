from light_bulb import Light_bulb
from datetime import datetime, timedelta
from random import randint


def display_state(light_bulbs: list[Light_bulb]):
    """
    Funckja wyswietla stany wszystkich utworzonych zarowek.
    Format wyswietlenia stanu zarowki:
    Zarowka nr {number} stan: {switch_state}    natezenie swiatla: {intensity}
    kolor: {colour} zainstalowania: {creation_time}
    oczekiwane zakoczenie pracy w: {end_life_time}

    Wyswietlenie stanu pomiedzy poszczegolnymi zarowkami jest oddzielone
    znakiem konca linii.
    Dodatkowo funkcja oblicza i wyswietla date prawdopodobnego zakonczenia
    pracy zarowki, korzystajac z parametru 'creation_time' oraz
    'approx_life_duration'.
    """
    if len(light_bulbs) == 0:
        print("Nie masz zadnych zarowek. Stworz najpierw "
              "jakies, abys potem mogl wyswietlic ich stan.")
        return
    else:
        for light_bulb in light_bulbs:
            end_life_time = light_bulb.get_creation_time() + timedelta(
                light_bulb.get_approx_life_duration()*365)
            print(f"Zarówka nr {light_bulb.get_number()}\t"
                  f"stan: {light_bulb.get_switch_state()}\t"
                  f"natezenie swiatla: {light_bulb.get_intensity()}\n"
                  f"kolor: {light_bulb.get_colour()}\t"
                  f"zainstalowana: {light_bulb.get_creation_time()}\n"
                  "oczekiwane zakonczenie pracy w: "
                  f"{end_life_time}\n")


def create_new_light_bulb(number_of_light_bulbs: int):
    """
    Funkcja tworzy nowa zarowke. Jedynym parametrem ustawianym w tej funkcji
    przez uzytkownika jest kolor zarowki, pozostale parametry sa ustawiane
    jako domyslne.
    """
    print("Podaj kolor zarowki. Do wyboru masz: biała, zolta, niebieska "
          "lub czerwona:")

    colour = input()
    while (colour not in ["biala", "zolta", "niebieska", "czerwona"]):
        print("Podales kolor, ktory nie jest dostepny. Dostepne kolory:"
              "\n-biala\n-zolta\n-niebieska\n-czerwona")
        colour = input()

    light_bulb = Light_bulb(number=number_of_light_bulbs + 1,
                            colour=colour, creation_time=datetime.now(),
                            approx_life_duration=randint(1, 10))

    print("Utworzono nowa zarowke!")

    return light_bulb


def remove_light_bulb(light_bulbs: list[Light_bulb]):
    """
    Funkcja wpierw wyswietla wszystkie isniejace zarowki korzystajac z innej
    funkcji: 'display_state()'. Nastepnie prosi uzytkonika o podanie numeru
    zarowki, ktora ma byc usunieta. Po usunieciu nastepuje aktualizacja
    numerow pozostalych zarowek tak, by kazda zarowka w liscie zarowek miala
    numer odpowiadajacy jej pozycji w liscie, zaczynajac od numeru '1'.
    """
    if len(light_bulbs) == 0:
        print("Nie masz zadnych zarowek. Stworz najpierw "
              "jakies, abys potem mogl je usunac.")
        return
    else:
        print("Oto zarowki dostepne do usuniecia:\n")
    display_state(light_bulbs)
    print("Podaj numer zarowki ktora chcesz usunac: ")

    number = input()
    while ((not number.isdecimal()) or
           (int(number) <= 0)):
        print("Podaj numer jednej z instniejacych zarowek:")
        number = input()

    number = int(number)
    light_bulbs.pop(number-1)
    print(f"Usunięto żarówkę nr {number}.")
    set_bulbs_numbers(light_bulbs)


def set_bulbs_numbers(light_bulbs: list[Light_bulb]):
    """
    Funkcja aktualizuje numery w liscie zarowek tak, aby kazda zarowka miala
    numer odpowiadajacy jej pozycji w liscie, zaczynajac od '1'.
    """
    for i in range(len(light_bulbs)):
        light_bulbs[i].set_number(i+1)


def edit_light_bulb(light_bulbs: list[Light_bulb]):
    """
    Funkcja wpierw wyswietla wszystkie isniejace zarowki korzystajac z innej
    funkcji: 'display_state()'. Nastepnie prosi uzytkonika o podanie numeru
    zarowki, ktora ma byc poddana edycji. Nastepnie uzytkownik musi podac
    parametr, jaki chce poddac edycji, a nastepnie moze podac nowa wartosc
    tego parametru. Parametry mozliwe do edycji przez uzytkownika:
    - switch_state
    - intensity
    - colour
    """
    if len(light_bulbs) == 0:
        print("Nie masz zadnych zarowek. Stwórz najpierw "
              "jakies, abys potem mogl je edytowac.")
        return
    else:
        print("Oto zarówki dostepne do edycji:\n")
    display_state(light_bulbs)
    print("Podaj numer zarówki która chcesz edytowac: ")

    number = input()
    while ((not number.isdecimal()) or
           (int(number) <= 0) or
           (int(number) > len(light_bulbs))):
        print("Podaj numer jednej z instniejacych zarowek:")
        number = input()

    number = int(number)
    print("Podaj jaki parametr chcesz edytowac.")
    print("Parametry dostepne do edycji:\n-stan\n-natezenie swiatla\n-kolor")

    param = input()
    while (param not in ["stan", "natezenie swiatla", "kolor"]):
        print("Podaleś niewlasciwy parametr.")
        print("Parametry dostępne do edycji:\n-stan\n-natezenie swiatla"
              "\n-kolor")
        param = input()

    if (param == "stan"):
        print("Podaj nowy stan zarówki. Do wyboru:\n-wlaczona\n-wylaczona")
        state = input()
        while (state not in ["wlaczona", "wylaczona"]):
            print("Podales niewlasciwy stan zarowki.")
            print("Mozliwe stany zarówki:\n-wlaczona\n-wylaczona")
            state = input()
        light_bulbs[number-1].set_switch_state(state)
        print("Zmieniono stan zarowki")

    elif (param == "natezenie swiatla"):
        print("Podaj nowe natezenie swiecenia zarowki. Wartosc musi byc "
              "liczba calkowita i zawierac sie w przedziale od 0 do 100")
        intensity = input()
        while ((not intensity.isdecimal()) or
               (int(intensity) < 0) or
               (int(intensity) > 100)):
            print("Podales niewlasciwa wartosc natezenia swiatla zarowki.")
            print("Podaj liczbe calkowita zawierajaca sie w przedziale od 0 "
                  "do 100")
            intensity = input()
        light_bulbs[number-1].set_intensity(int(intensity))
        print("Zmieniono natezenie swiatla zarowki")

    elif (param == "kolor"):
        print("Podaj nowy kolor zarowki. Do wyboru:\n-biala\n-zolta"
              "\n-niebieska\n-czerwona")
        colour = input()
        while (colour not in ["biala", "zolta", "niebieska", "czerwona"]):
            print("Podales niewlasciwy kolor zarowki.")
            print("Mozliwe kolory zarowki:\n-biala\n-zolta"
                  "\n-niebieska\n-czerwona")
            colour = input()
        light_bulbs[number-1].set_colour(colour)
        print("Zmieniono kolor zarowki")


def turn_on_all(light_bulbs):
    """
    Funckja ustawia stan 'wlaczona' w parametrze 'switch_state'
    we wszystkich zarowkach.
    """
    if len(light_bulbs) == 0:
        print("Nie masz zadnych zarowek. Stworz najpierw "
              "jakies, abys potem mogl je edytowac.")
    else:
        for light_bulb in light_bulbs:
            light_bulb.set_switch_state("wlaczona")
        print("Wlaczona wszytkie zarowki.")


def turn_off_all(light_bulbs):
    """
    Funckja ustawia stan 'wylaczona' w parametrze 'switch_state'
    we wszystkich zarowkach.
    """
    if len(light_bulbs) == 0:
        print("Nie masz zadnych zarowek. Stworz najpierw "
              "jakies, abys potem mogl je edytowac.")
    else:
        for light_bulb in light_bulbs:
            light_bulb.set_switch_state("wylaczona")
        print("Wylaczona wszytkie zarowki.")
