# NFC Tag Scanner:
# Read NFC tags using a PN532 module (over I2C or UART), similar to Flipper Zero’s NFC reader.

# This module now integrates with main.py option 2 (NFC Reader).
# It continuously scans and prints NFC tag UIDs.

# Uses adafruit_pn532 library to talk to a PN532 reader (e.g., via I2C)
# Scans and displays UID of nearby NFC tags


# Hardware Setup (Raspberry Pi Zero 2 W)
# PN532 → Raspberry Pi GPIO (I²C):
# PN532       Raspberry Pi GPIO
# ------      -------------------
# SDA         GPIO 2 (Pin 3)
# SCL         GPIO 3 (Pin 5)
# VCC         3.3V (Pin 1)
# GND         GND (Pin 6)


# Enable I2C in BASH:
# sudo raspi-config
# -> Interface Options -> I2C -> Enable
# sudo apt install -y python3-pip i2c-tools
# pip3 install adafruit-circuitpython-pn532


import board
import busio
from adafruit_pn532.i2c import PN532_I2C

# Setup I2C bus
i2c = busio.I2C(board.SCL, board.SDA)
pn532 = PN532_I2C(i2c, debug=False)

# Configure PN532
pn532.SAM_configuration()

print("Ready to scan NFC tags. Hold one near...")

try:
    while True:
        uid = pn532.read_passive_target(timeout=0.5)
        if uid is not None:
            print("NFC Tag Detected! UID:", [hex(i) for i in uid])
except KeyboardInterrupt:
    print("\nExiting NFC reader.")
