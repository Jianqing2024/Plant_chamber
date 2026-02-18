from pydantic import BaseModel
from datetime import datetime

class EnvironmentState(BaseModel):
    temperature: float
    humidity: float
    timestamp: datetime

class ControlCommand(BaseModel):
    heater_power: float  # 0~1
    humidifier_power: float  # 0~1

class TargetSetting(BaseModel):
    target_temp: float
    target_humidity: float
