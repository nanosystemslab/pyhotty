"""Unit tests for Pyhotty Lbrary."""

from typing import Any
from unittest.mock import MagicMock
from unittest.mock import patch

import pytest

from pyhotty.pyhotty import Heater


@pytest.fixture
def mock_instrument() -> Any:
    """Creates a mock of the minimalmodbus.Instrument class."""
    with patch("minimalmodbus.Instrument", autospec=True) as mock_instrument:
        yield mock_instrument


def test_heater_init(mock_instrument: Any) -> None:
    """Test initializing the Heater class."""
    heater = Heater(port="/dev/ttyACM0", addr=1)

    mock_instrument.assert_called_once_with("/dev/ttyACM0", 1, mode="rtu")
    assert heater.port == "/dev/ttyACM0"
    assert heater.addr == 1


def test_set_pid(mock_instrument: Any) -> None:
    """Test setting PID parameters."""
    heater = Heater(port="/dev/ttyACM0", addr=1)
    heater.ser = MagicMock()

    heater.set_pid(1.0, 2.0, 3.0, 4.0, 70.0)

    heater.ser.write_float.assert_any_call(686, 1.0, 2)
    heater.ser.write_float.assert_any_call(680, 2.0, 2)
    heater.ser.write_float.assert_any_call(676, 3.0, 2)
    heater.ser.write_float.assert_any_call(678, 4.0, 2)
    heater.ser.write_float.assert_any_call(544, 70.0, 2)


def test_set_thermocouple(mock_instrument: Any) -> None:
    """Test setting thermocouple type."""
    heater = Heater(port="/dev/ttyACM0", addr=1)
    heater.ser = MagicMock()

    heater.set_thermocouple(couple_type=2)

    heater.ser.write_register.assert_called_once_with(643, 2, 0, 16, False)


def test_get_temp(mock_instrument: Any) -> None:
    """Test getting temperature."""
    heater = Heater(port="/dev/ttyACM0", addr=1)
    heater.ser = MagicMock()

    # Mock the return value of read_float
    heater.ser.read_float.return_value = 123.45

    temperature = heater.get_temp()

    heater.ser.read_float.assert_called_once_with(528, 3, 2)
    assert temperature == 123.45


def test_run(mock_instrument: Any) -> None:
    """Test running the heater."""
    heater = Heater(port="/dev/ttyACM0", addr=1)
    heater.ser = MagicMock()

    heater.run()

    heater.ser.write_register.assert_any_call(576, 5, 0, 16, False)
    heater.ser.write_register.assert_any_call(576, 6, 0, 16, False)


def test_stop(mock_instrument: Any) -> None:
    """Test stopping the heater."""
    heater = Heater(port="/dev/ttyACM0", addr=1)
    heater.ser = MagicMock()

    heater.stop()

    heater.ser.write_register.assert_called_once_with(576, 8, 0, 16, False)


def test_set_action_direct(mock_instrument: Any) -> None:
    """Test setting action to direct."""
    heater = Heater(port="/dev/ttyACM0", addr=1)
    heater.ser = MagicMock()

    heater.set_action("direct")

    heater.ser.write_register.assert_called_once_with(673, 1, 0, 16, False)


def test_set_action_reverse(mock_instrument: Any) -> None:
    """Test setting action to reverse."""
    heater = Heater(port="/dev/ttyACM0", addr=1)
    heater.ser = MagicMock()

    heater.set_action("reverse")

    heater.ser.write_register.assert_called_once_with(673, 0, 0, 16, False)


def test_action_off(mock_instrument: Any) -> None:
    """Test setting output action to off."""
    heater = Heater(port="/dev/ttyACM0", addr=1)
    heater.ser = MagicMock()

    heater.action("off")

    heater.ser.write_register.assert_called_once_with(1025, 0, 0, 16, False)


def test_action_pid(mock_instrument: Any) -> None:
    """Test setting output action to PID."""
    heater = Heater(port="/dev/ttyACM0", addr=1)
    heater.ser = MagicMock()

    heater.action("pid")

    heater.ser.write_register.assert_called_once_with(1025, 1, 0, 16, False)


def test_autotune_adaptive_enable(mock_instrument: Any) -> None:
    """Test enabling adaptive autotuning."""
    heater = Heater(port="/dev/ttyACM0", addr=1)
    heater.ser = MagicMock()

    heater.autotune_adaptive(enable=True)

    heater.ser.write_register.assert_called_once_with(672, 1, 0, 16, False)


def test_filter_hold(mock_instrument: Any) -> None:
    """Test setting filter value."""
    heater = Heater(port="/dev/ttyACM0", addr=1)
    heater.ser = MagicMock()

    heater.filter_hold(5)

    heater.ser.write_register.assert_called_once_with(655, 5, 0, 16, False)
