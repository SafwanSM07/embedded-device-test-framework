import pytest

from src.simulator import DeviceSimulator


@pytest.fixture
def device():
    return DeviceSimulator()


@pytest.mark.parametrize("speed", [0, 1, 25, 50, 99, 100])
def test_accepts_valid_motor_speeds(device, speed):
    response = device.set_motor_speed(speed)

    assert response["status"] == "OK"
    assert response["motor_speed"] == speed


@pytest.mark.parametrize("speed", [-1, 101, 200])
def test_rejects_out_of_range_motor_speeds(device, speed):
    with pytest.raises(ValueError):
        device.set_motor_speed(speed)


@pytest.mark.parametrize("speed", ["fast", None, 50.5])
def test_rejects_invalid_motor_speed_types(device, speed):
    with pytest.raises(TypeError):
        device.set_motor_speed(speed)
