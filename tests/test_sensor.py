import pytest

from src.simulator import DeviceSimulator


def test_sensor_returns_expected_data():
    device = DeviceSimulator()

    data = device.read_environment()

    assert 20 <= data["temperature"] <= 30
    assert 30 <= data["humidity"] <= 70


def test_sensor_failure_is_reported():
    device = DeviceSimulator()
    device.sensor_failed = True

    with pytest.raises(
        RuntimeError,
        match="Sensor communication failed",
    ):
        device.read_environment()
