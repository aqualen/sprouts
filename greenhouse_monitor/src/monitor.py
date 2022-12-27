"""
December 2022
Class: sprouts
Author: Leonard Vaughn (@aqualen)
"""
import logging
from datetime import datetime

import google.cloud.logging
import serial
import yaml

# Load configuration
# Connect to XBee port
# Authenticate to Google Cloud

# Do Forever: Read data from port, (mumble) log to cloud

if __name__ == '__main__':
    print("Welcome to sprouts monitor")

    print("Loading configuration")
    with open('monitor.yml', 'r') as f:
        config = yaml.safe_load(f)
        monitor_config = config[0]['monitor']

    port = monitor_config["port"]
    keys = monitor_config["keys"]
    # port = "/dev/cu.usbserial-A600exNO"  # TODO: Read from external configuration
    # keys = "/Users/l/gcp/test-sprouts-5f2330e47aea.json"  # TODO: Read from configuration

    print("Connecting to GCP Logging service")
    client = google.cloud.logging.Client.from_service_account_json(keys)
    client.setup_logging()
    logging.info(f"Sprouts MONITOR Connecting at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    print("Listening for greenhouse telemetry...")

    try:
        with serial.Serial(port) as ser:
            print(f"Connected to {port}")
            logging.info(
                f"Sprouts MONITOR successfully connected to inbound telemetry port {port}")

            while True:
                line = ser.readline().decode('ASCII').strip()
                print(f"line: {line}")
                # I could simply send to GCP at this point...and filter there.
                logging.info(line)

    except serial.serialutil.SerialException:
        print(f"Unable to open the serial port {port}.  Make sure your device is connected "
              "and you have identified the proper port in the monitor.yml configuration file.")
