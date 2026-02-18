import time
from app.simulator.environment import EnvironmentModel
from app.controller.basic import BasicController
from app.models.state import TargetSetting

def main():

    simulator = EnvironmentModel()
    controller = BasicController()

    target = TargetSetting(
        target_temp=28.0,
        target_humidity=65.0
    )

    control = None

    for _ in range(200):

        if control is None:
            from app.models.state import ControlCommand
            control = ControlCommand(heater_power=0, humidifier_power=0)

        state = simulator.update(control)
        control = controller.compute(state, target)

        print(
            f"T={state.temperature:.2f}C "
            f"H={state.humidity:.2f}% "
            f"Heater={control.heater_power}"
        )

        time.sleep(0.1)

if __name__ == "__main__":
    main()
