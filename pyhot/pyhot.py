from typing import Union
import minimalmodbus  # type: ignore[import]

class Heater:
    def __init__(self, port: str = "", addr: Union[int, None] = None):
        """
        Constructor for the Heater class.

        Parameters:
        - port: Serial port where the heater is connected.
        - addr: Modbus address of the heater.
        """
        self.port = port
        self.addr = addr
        self.ser = minimalmodbus.Instrument(port, addr, mode="rtu")

    def set_PID(self, max_rate: float, dev_gain: float, pro_gain: float, int_gain: float, PID_setpoint: float) -> None:
        """
        Set PID parameters for the heater.

        Parameters:
        - max_rate: Maximum rate of change for the process variable.
        - dev_gain: Derivative gain of the PID controller.
        - pro_gain: Proportional gain of the PID controller.
        - int_gain: Integral gain of the PID controller.
        - PID_setpoint: Setpoint for the PID controller.
        """
        self.ser.write_float(686, max_rate, 2)
        self.ser.write_float(676, pro_gain, 2)  # P gain
        self.ser.write_float(678, int_gain, 2)  # I gain
        self.ser.write_float(680, dev_gain, 2)  # D Gain
        self.ser.write_float(544, PID_setpoint, 2)  # Current Setpoint 1
        return

    def set_thermocouple(self, couple_type: int = 1) -> None:
        """
        Set the type of thermocouple for the heater.

        Parameters:
        - couple_type: Type of thermocouple.
        """
        self.ser.write_register(643, couple_type, 0, 16, False)  # Thermocouple Type

    def get_temp(self) -> float:
        """
        Get the current temperature from the heater.

        Returns:
        - Current temperature.
        """
        temperature = self.ser.read_float(528, 3, 2)  # Current Input Value
        temperature = "%.4f" % temperature
        temperature = f"{temperature:{6}.{6}}"
        return float(temperature)

    def run(self) -> None:
        """
        Start the heater in run mode.
        """
        self.ser.write_register(576, 5, 0, 16, False)  # The running mode
        self.ser.write_register(576, 6, 0, 16, False)  # Run Mode

    def stop(self) -> None:
        """
        Stop the heater.
        """
        self.ser.write_register(576, 8, 0, 16, False)  # The running mode

    def set_action(self, action_value: str) -> None:
        """
        Set the action (direct or reverse) for the PID controller.

        Parameters:
        - action_value: Action value ("direct" or "reverse").
        """
        if action_value == "direct":
            self.ser.write_register(673, 1, 0, 16, False)  # PID Action
        elif action_value == "reverse":
            self.ser.write_register(673, 0, 0, 16, False)  # PID Action
        return

    def action(self, output_value: str) -> None:
        """
        Set the action for the heater output.

        Parameters:
        - output_value: Output action ("off" or "pid").
        """
        if output_value == "off":
            self.ser.write_register(1025, 0, 0, 16, False)  # Output 1 Mode
        elif output_value == "pid":
            self.ser.write_register(1025, 1, 0, 16, False)  # Output 1 Mode
        return

    def autotune_adaptive(self, enable: bool = False) -> None:
        """
        Enable or disable adaptive PID tuning.

        Parameters:
        - enable: Enable or disable adaptive tuning.
        """
        if enable is True:
            self.ser.write_register(672, 1, 0, 16, False)  # PID Adaptive Control
        return
        self.ser.write_register(672, 0, 0, 16, False)  # PID Adaptive Control
        return

    def set_PID_auto(self, max_rate: float, autotune_timeout: int, PID_setpoint: float) -> None:
        """
        Set PID parameters for auto-tuning.

        Parameters:
        - max_rate: Maximum rate of change for the process variable.
        - autotune_timeout: Timeout for auto-tuning in milliseconds.
        - PID_setpoint: Setpoint for the PID controller.
        """
        autotune_timeout = autotune_timeout * 1000
        self.ser.write_float(686, max_rate, 2)
        self.ser.write_float(544, PID_setpoint, 2)  # Current Setpoint 1
        self.ser.write_long(674, autotune_timeout, False)
        self.ser.write_register(579, 1, 0, 16, False)  # Autotune Start
        return

    def filter_hold(self, filter_knob: int = 0) -> None:
        """
        Set the filter value for the heater.

        Parameters:
        - filter_knob: Filter knob value.
        """
        filter_knob = int(filter_knob)
        self.ser.write_register(655, filter_knob, 0, 16, False)  # Filter
        return

# Example usage:
# c1 = Heater(port="/dev/ttyACM4", addr=1)
# c1.set_thermocouple()
# c1.set_action()
# c1.filter_hold()
# c1.set_PID(max_rate=1, dev_gain=1, pro_gain=8, int_gain=0, PID_setpoint=70)
# c1.run()
#
# c2 = Heater(port="/dev/ttyACM2", addr=2)
# c2.set_thermocouple()
# c2.set_action()
# c2.filter_hold()
# c2.set_PID(max_rate=1, dev_gain=1, pro_gain=8, int_gain=0, PID_setpoint=70)
# c2.run()
#
# while(1):
#     print("{},{}".format(c1.get_temp(), c2.get_temp()))
#     time.sleep(1)
