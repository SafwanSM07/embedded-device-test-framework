# Embedded Device Automated Test Framework

A Python-based automated testing framework for simulated embedded
devices. The project demonstrates functional, boundary, negative,
failure-handling, regression and reliability testing.

## Features

- Simulated motor-control device
- Simulated temperature and humidity sensor
- Motor speed validation
- Sensor failure simulation
- Device reset testing
- Repeated-operation reliability testing
- Automated testing using Pytest
- Continuous testing using GitHub Actions

## Technologies

- Python
- Pytest
- PySerial
- GitHub Actions

## Installation

Clone the repository:

```bash
git clone https://github.com/SafwanSM07/embedded-device-test-framework.git
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Run the tests

```bash
pytest -v
```

## Testing strategy

| Test area | Coverage |
|---|---|
| Motor control | Valid, boundary and invalid inputs |
| Sensors | Expected values and communication failure |
| Device reset | Return to a safe default state |
| Reliability | 1,000 repeated motor commands |
| Automation | Tests run automatically after every push |

## Planned improvements

- ESP32 serial communication
- Communication timeout handling
- JSON command protocol
- HTML test reports
- Test coverage reporting
- Hardware-in-the-loop testing
