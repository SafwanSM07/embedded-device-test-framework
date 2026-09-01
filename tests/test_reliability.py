from src.simulator import DeviceSimulator


def test_device_handles_repeated_motor_commands():
    device = DeviceSimulator()

    for cycle in range(1000):
        speed = cycle % 101
        response = device.set_motor_speed(speed)

        assert response["motor_speed"] == speed
