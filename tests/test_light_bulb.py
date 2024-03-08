from light_bulb import Light_bulb
from datetime import datetime
import pytest
from time import sleep


def test_create_valid_light_bulb():
    date = datetime.now()
    new_light_bulb = Light_bulb(1, "wlaczona", 0, "biala", date, 1)
    assert new_light_bulb.get_number() == 1
    assert new_light_bulb.get_switch_state() == "wlaczona"
    assert new_light_bulb.get_intensity() == 0
    assert new_light_bulb.get_colour() == "biala"
    assert new_light_bulb.get_creation_time() == date
    assert new_light_bulb.get_approx_life_duration() == 1


def test_create_defaul_light_bulb():
    new_light_bulb = Light_bulb()
    assert new_light_bulb.get_number() == 1
    assert new_light_bulb.get_switch_state() == "wylaczona"
    assert new_light_bulb.get_intensity() == 0
    assert new_light_bulb.get_colour() == "biala"

# Test set_number() method


def test_set_number_with_valid_input():
    new_light_bulb = Light_bulb()
    new_light_bulb.set_number(1)
    assert new_light_bulb.get_number() == 1


def test_set_number_to_float():
    new_light_bulb = Light_bulb()
    with pytest.raises(Exception):
        new_light_bulb.set_number(1.1)


def test_set_number_to_zero():
    new_light_bulb = Light_bulb()
    with pytest.raises(Exception):
        new_light_bulb.set_number(0)


def test_set_number_to_negative_integral():
    new_light_bulb = Light_bulb()
    with pytest.raises(Exception):
        new_light_bulb.set_number(-1)


def test_set_number_to_single_character():
    new_light_bulb = Light_bulb()
    with pytest.raises(Exception):
        new_light_bulb.set_number('a')

# Test set_switch_state() method


def test_set_switch_state_with_valid_input():
    new_light_bulb = Light_bulb()
    new_light_bulb.set_switch_state("wlaczona")
    assert new_light_bulb.get_switch_state() == "wlaczona"


def test_set_switch_state_to_float():
    new_light_bulb = Light_bulb()
    with pytest.raises(Exception):
        new_light_bulb.set_switch_state(1.1)


def test_set_switch_state_to_int():
    new_light_bulb = Light_bulb()
    with pytest.raises(Exception):
        new_light_bulb.set_switch_state(1)


def test_set_switch_state_to_single_character():
    new_light_bulb = Light_bulb()
    with pytest.raises(Exception):
        new_light_bulb.set_switch_state('a')


def test_set_switch_state_to_invalid_word():
    new_light_bulb = Light_bulb()
    with pytest.raises(Exception):
        new_light_bulb.set_switch_state("Wlaczona")

# Test set_intensity() method


def test_set_intensity_with_valid_input():
    new_light_bulb = Light_bulb()
    new_light_bulb.set_intensity(1)
    assert new_light_bulb.get_intensity() == 1


def test_set_intensity_to_float():
    new_light_bulb = Light_bulb()
    with pytest.raises(Exception):
        new_light_bulb.set_intensity(1.1)


def test_set_intensity_to_negative_integer():
    new_light_bulb = Light_bulb()
    with pytest.raises(Exception):
        new_light_bulb.set_intensity(-1)


def test_set_intensity_to_zero():
    new_light_bulb = Light_bulb()
    new_light_bulb.set_intensity(0)
    assert new_light_bulb.get_intensity() == 0


def test_set_intensity_to_100():
    new_light_bulb = Light_bulb()
    new_light_bulb.set_intensity(100)
    assert new_light_bulb.get_intensity() == 100


def test_set_intensity_above_100():
    new_light_bulb = Light_bulb()
    with pytest.raises(Exception):
        new_light_bulb.set_intensity(101)

# Test set_colour() method


def test_set_colour_with_valid_input():
    new_light_bulb = Light_bulb()
    new_light_bulb.set_colour("czerwona")
    assert new_light_bulb.get_colour() == "czerwona"


def test_set_colour_to_float():
    new_light_bulb = Light_bulb()
    with pytest.raises(Exception):
        new_light_bulb.set_colour(1.1)


def test_set_colour_to_int():
    new_light_bulb = Light_bulb()
    with pytest.raises(Exception):
        new_light_bulb.set_colour(1)


def test_set_colour_to_single_character():
    new_light_bulb = Light_bulb()
    with pytest.raises(Exception):
        new_light_bulb.set_colour('a')


def test_set_colour_to_invalid_word():
    new_light_bulb = Light_bulb()
    with pytest.raises(Exception):
        new_light_bulb.set_colour("bialy")

# Test set_creation_time()


def test_set_creation_time_with_valid_input():
    new_light_bulb = Light_bulb()
    sleep(0.01)
    date = datetime.now()
    assert new_light_bulb.get_creation_time() != date
    new_light_bulb.set_creation_time(date)
    assert new_light_bulb.get_creation_time() == date


def test_set_creation_time_to_float():
    new_light_bulb = Light_bulb()
    with pytest.raises(Exception):
        new_light_bulb.set_creation_time(1.1)


def test_set_creation_time_to_int():
    new_light_bulb = Light_bulb()
    with pytest.raises(Exception):
        new_light_bulb.set_creation_time(1)


def test_set_creation_time_to_str():
    new_light_bulb = Light_bulb()
    with pytest.raises(Exception):
        new_light_bulb.set_creation_time("abc")

# Test set_approx_life_duration()


def test_set_approx_life_duration_with_valid_input():
    new_light_bulb = Light_bulb(approx_life_duration=1)
    assert new_light_bulb.get_approx_life_duration() == 1
    new_light_bulb.set_approx_life_duration(2)
    assert new_light_bulb.get_approx_life_duration() == 2


def test_set_approx_life_duration_to_float():
    new_light_bulb = Light_bulb()
    with pytest.raises(Exception):
        new_light_bulb.set_approx_life_duration(1.1)


def test_set_approx_life_duration_to_negtive_integer():
    new_light_bulb = Light_bulb()
    with pytest.raises(Exception):
        new_light_bulb.set_approx_life_duration(-1)


def test_set_approx_life_duration_to_str():
    new_light_bulb = Light_bulb()
    with pytest.raises(Exception):
        new_light_bulb.set_approx_life_duration("abc")


def test_set_approx_life_duration_to_out_of_range():
    new_light_bulb = Light_bulb()
    with pytest.raises(Exception):
        new_light_bulb.set_approx_life_duration(11)
