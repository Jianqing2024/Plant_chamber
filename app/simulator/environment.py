import numpy as np
from datetime import datetime
from app.models.state import EnvironmentState, ControlCommand

class EnvironmentModel:

    def __init__(self):
        self.temperature = 25.0
        self.humidity = 50.0
        self.room_temp = 22.0

    def update(self, control: ControlCommand) -> EnvironmentState:

        # 温度动力学模型
        heater_effect = 2.0 * control.heater_power
        cooling = 0.1 * (self.temperature - self.room_temp)

        self.temperature += heater_effect - cooling

        # 湿度模型
        humidifier_effect = 3.0 * control.humidifier_power
        natural_decay = 0.05 * (self.humidity - 40)

        self.humidity += humidifier_effect - natural_decay

        return EnvironmentState(
            temperature=self.temperature,
            humidity=self.humidity,
            timestamp=datetime.now()
        )
