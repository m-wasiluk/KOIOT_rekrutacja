from random import randint
from datetime import datetime


class Light_bulb:
    """
    Klasa Lught_bulb reprezentuje pojedyncza zarowke. Zawiera nastepujace pola:

    :param number: Kazda zarowka ma swoj oddzielny numer, swiadczacy o jej
    pozycji w liscie zarowek. Pozwala to na jednoznaczne odniesienie sie
    do konkretnej zarowki, np w przypadku decyzji o usunieciu
    konkretnej zarowki.
    :param type: int, musi byc liczba calkowita wieksza od zera

    :param switch_state: Reprezentuje stan zapalenia zarowki.
    :type switch_state: str, dostępne tylko dwa stany: "wlaczona", "wylaczona"

    :param intensity: Reprezentuje intensywnosc swiecenia zarowki.
    :type intensity: int, musi zawierac sie w przedziale <0;100>

    :param colour: Reprezentuje barwe swiecenia zarowki.
    :type colour: str, dostepne tylko 4 kolory:
    "biala", "zolta", "niebieksa", "czerwona"

    :param creation_time: Reprezentuje moment pierwszej instalacji
    zarowki (rownoznaczne z momentem utworzenia obiektu klasy 'Light_bulb')
    :type creation_time: datetime

    :param approx_life_duration: Liczba losowa z przedziału <1; 10>
    reprezentująca lata, po jakich w przyblizeniu zarowka przestanie dzialac.
    :type approx_life_duration: int
    """
    def __init__(self, number: int = 1, switch_state: str = "wylaczona",
                 intensity: int = 0, colour: str = "biala",
                 creation_time: datetime = None,
                 approx_life_duration: int = None):
        self.set_number(number)
        self.set_switch_state(switch_state)
        self.set_intensity(intensity)
        self.set_colour(colour)
        if not creation_time:
            self._creation_time = datetime.now()
        else:
            self.set_creation_time(creation_time)
        if not approx_life_duration:
            self._approx_life_duration = randint(1, 10)
        else:
            self.set_approx_life_duration(approx_life_duration)

    def set_number(self, new_number: int):
        if ((type(new_number) is not int) or
           (new_number <= 0)):
            raise Exception
        else:
            self._number = new_number

    def get_number(self):
        return self._number

    def set_switch_state(self, new_switch_state: str):
        if (new_switch_state not in ("wlaczona", "wylaczona")):
            raise Exception
        else:
            self._switch_state = new_switch_state

    def get_switch_state(self):
        return self._switch_state

    def set_intensity(self, new_intensity: int):
        if ((type(new_intensity) is not int) or
           (new_intensity < 0) or
           (new_intensity > 100)):
            raise Exception
        else:
            self._intensity = new_intensity

    def get_intensity(self):
        return self._intensity

    def set_colour(self, new_colour: str):
        if ((type(new_colour) is not str) or
           (new_colour not in ("biala", "zolta", "niebieska", "czerwona"))):
            raise Exception
        else:
            self._colour = new_colour

    def get_colour(self):
        return self._colour

    def set_creation_time(self, new_creation_time):
        if (type(new_creation_time) is not datetime):
            raise Exception
        self._creation_time = datetime.now()

    def get_creation_time(self):
        return self._creation_time

    def set_approx_life_duration(self, new_life_duration):
        if ((type(new_life_duration) is not int) or
           (new_life_duration < 0) or
           (new_life_duration > 10)):
            raise Exception
        self._approx_life_duration = new_life_duration

    def get_approx_life_duration(self):
        return self._approx_life_duration
