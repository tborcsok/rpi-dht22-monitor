# DHT22 data collector

Python script that runs on Raspberry Pi and reads [DHT22](https://www.adafruit.com/product/385) sensor values. This sensor measures temperature and relative humidity.

The script and setup are based on [this tutorial](https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/python-setup).

## Physical setup

This script assumes that the sensor is connected to the D22 pin of the Raspberry Pi.

## How to run

The entrypoint to the data collection is `test_scheduled.py`. The Python environment is defined by `requirements.txt` and Python version is found in `version.txt`. The environment is compatible with my Raspberry Pi 3 Model B running Raspbian 10.

The CircuitPython package requires that you instal `libgpiod2` with apt.

My recommended way of creating the Python environment on the Pi is the `venv` package. To use or update it, install `python3-venv` and `python3-wheel` with apt. Then in your folder of choice, you can create a new Python environment in a folder called env: `python3 -m venv env`.

![DHT22 sensor](https://cdn-shop.adafruit.com/970x728/385-00.jpg)
