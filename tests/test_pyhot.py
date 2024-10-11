import pytest
from unittest.mock import patch, MagicMock
from pyhot.pyhot import Heater
from typing import Any

# Mocking the minimalmodbus.Instrument class
@pytest.fixture
def mock_instrument() -> Any:
    with patch('minimalmodbus.Instrument', autospec=True) as mock_instrument:
        yield mock_instrument

def test_heater_init(mock_instrument: Any) -> None:
    # Test initializing the Heater class
    heater = Heater(port="/dev/ttyACM0", addr=1)
    
    mock_instrument.assert_called_once_with("/dev/ttyACM0", 1, mode="rtu")
    assert heater.port == "/dev/ttyACM0"
    assert heater.addr == 1

def test_set_PID(mock_instrument: Any) -> None:
    heater = Heater(port="/dev/ttyACM0", addr=1)
    heater.ser = MagicMock()

    # Test setting PID parameters
    heater.set_PID(1.0, 2.0, 3.0, 4.0, 70.0)

    heater.ser.write_float.assert_any_call(686, 1.0, 2)
    heater.ser.write_float.assert_any_call(680, 2.0, 2)
    heater.ser.write_float.assert_any_call(676, 3.0, 2)
    heater.ser.write_float.assert_any_call(678, 4.0, 2)
    heater.ser.write_float.assert_any_call(544, 70.0, 2)

def test_set_thermocouple(mock_instrument: Any) -> None:
    heater = Heater(port="/dev/ttyACM0", addr=1)
    heater.ser = MagicMock()

    # Test setting thermocouple type
    heater.set_thermocouple(couple_type=2)

    heater.ser.write_register.assert_called_once_with(643, 2, 0, 16, False)

def test_get_temp(mock_instrument: Any) -> None:
    heater = Heater(port="/dev/ttyACM0", addr=1)
    heater.ser = MagicMock()

    # Mock the return value of read_float
    heater.ser.read_float.return_value = 123.45

    # Test getting temperature
    temperature = heater.get_temp()

    heater.ser.read_float.assert_called_once_with(528, 3, 2)
    assert temperature == 123.45

def test_run(mock_instrument: Any) -> None:
    heater = Heater(port="/dev/ttyACM0", addr=1)
    heater.ser = MagicMock()

    # Test running the heater
    heater.run()

    heater.ser.write_register.assert_any_call(576, 5, 0, 16, False)
    heater.ser.write_register.assert_any_call(576, 6, 0, 16, False)

def test_stop(mock_instrument: Any) -> None:
    heater = Heater(port="/dev/ttyACM0", addr=1)
    heater.ser = MagicMock()

    # Test stopping the heater
    heater.stop()

    heater.ser.write_register.assert_called_once_with(576, 8, 0, 16, False)

def test_set_action_direct(mock_instrument: Any) -> None:
    heater = Heater(port="/dev/ttyACM0", addr=1)
    heater.ser = MagicMock()

    # Test setting action to direct
    heater.set_action("direct")

    heater.ser.write_register.assert_called_once_with(673, 1, 0, 16, False)

def test_set_action_reverse(mock_instrument: Any) -> None:
    heater = Heater(port="/dev/ttyACM0", addr=1)
    heater.ser = MagicMock()

    # Test setting action to reverse
    heater.set_action("reverse")

    heater.ser.write_register.assert_called_once_with(673, 0, 0, 16, False)

def test_action_off(mock_instrument: Any) -> None:
    heater = Heater(port="/dev/ttyACM0", addr=1)
    heater.ser = MagicMock()

    # Test setting output action to off
    heater.action("off")

    heater.ser.write_register.assert_called_once_with(1025, 0, 0, 16, False)

def test_action_pid(mock_instrument: Any) -> None:
    heater = Heater(port="/dev/ttyACM0", addr=1)
    heater.ser = MagicMock()

    # Test setting output action to PID
    heater.action("pid")

    heater.ser.write_register.assert_called_once_with(1025, 1, 0, 16, False)

def test_autotune_adaptive_enable(mock_instrument: Any) -> None:
    heater = Heater(port="/dev/ttyACM0", addr=1)
    heater.ser = MagicMock()

    # Test enabling adaptive autotuning
    heater.autotune_adaptive(enable=True)

    heater.ser.write_register.assert_called_once_with(672, 1, 0, 16, False)

def test_filter_hold(mock_instrument: Any) -> None:
    heater = Heater(port="/dev/ttyACM0", addr=1)
    heater.ser = MagicMock()

    # Test setting filter value
    heater.filter_hold(5)

    heater.ser.write_register.assert_called_once_with(655, 5, 0, 16, False)
