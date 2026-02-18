from app.models.state import ControlCommand, EnvironmentState, TargetSetting

class BasicController:

    def compute(self, state: EnvironmentState, target: TargetSetting) -> ControlCommand:

        heater = 0.0
        humidifier = 0.0

        # 滞回控制
        if state.temperature < target.target_temp - 0.5:
            heater = 1.0
        elif state.temperature > target.target_temp + 0.5:
            heater = 0.0

        if state.humidity < target.target_humidity - 2:
            humidifier = 1.0
        elif state.humidity > target.target_humidity + 2:
            humidifier = 0.0

        return ControlCommand(
            heater_power=heater,
            humidifier_power=humidifier
        )
