class DeviceSimulator:
    """Simulates a small sensor and motor-control device."""

    def __init__(self):
        self.motor_speed = 0
        self.temperature = 25.0
        self.humidity = 55.0
        self.sensor_failed = False

    def set_motor_speed(self, speed):
        if not isinstance(speed, int):
            raise TypeError("Motor speed must be an integer")

        if not 0 <= speed <= 100:
            raise ValueError("Motor speed must be between 0 and 100")

        self.motor_speed = speed

        return {
            "status": "OK",
            "motor_speed": self.motor_speed,
        }

    def read_environment(self):
        if self.sensor_failed:
            raise RuntimeError("Sensor communication failed")

        return {
            "temperature": self.temperature,
            "humidity": self.humidity,
        }

    def reset(self):
        self.motor_speed = 0
        self.sensor_failed = False

        return {"status": "RESET_COMPLETE"}
