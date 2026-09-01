from src.simulator import DeviceSimulator


def test_reset_returns_device_to_safe_state():
    device = DeviceSimulator()

    device.set_motor_speed(80)
    device.sensor_failed = True

    response = device.reset()

    assert response["status"] == "RESET_COMPLETE"
    assert device.motor_speed == 0
    assert device.sensor_failed is False
