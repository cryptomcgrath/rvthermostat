from enum import Enum
from mode import Mode
from action import Action
import control
import sensor

class Program:
    name = ""
    sensor_id = 0 
    control_id = 0
    set_point = 0
    mode = Mode['NONE']

    def __init__(self, name, sensor_id, control_id, set_point, mode):
        self.name = name
        self.sensor_id = sensor_id
        self.control_id = control_id
        self.set_point = set_point
        self.mode = mode

    def from_dict(dict):
        name = dict["name"]
        return Program(dict["name"], dict["sensor_id"], dict["control_id"], dict["set_point"], Mode.from_string(dict["mode"]))

