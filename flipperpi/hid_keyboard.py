#USB HID Payload Injector:
#Turn your Raspberry Pi Zero 2 W into a BadUSB keyboard, typing automated payloads when plugged into a PC. 
# Mimics Flipper Zero's “BadUSB” feature.
# Launch this from main.py option 5 and the Pi will type “hello world” when plugged into a PC via OTG


# On Linux, Pi Zero's OTG port can emulate USB gadgets using g_hid or gadgetfs.
# Uses a script that writes keypress sequences to the USB device.

# To Do:
# Enable USB HID gadget mode.
# Mount the HID endpoint.
# Send keystroke payloads in the correct format.


# One-Time Setup (Raspberry Pi Zero 2 W)
# 1. Add this to /boot/config.txt:
#dtoverlay=dwc2

# 2. Add to /boot/cmdline.txt (append modules-load=dwc2,g_hid):
# console=serial0,115200 ... rootwait modules-load=dwc2,g_hid


import time

# Path to HID device (keyboard)
HID_DEV = "/dev/hidg0"

# Simple key map (subset for demo)
KEY_CODES = {
    "ENTER": 0x28,
    "ESC": 0x29,
    "a": 0x04,
    "b": 0x05,
    "c": 0x06,
    "d": 0x07,
    "e": 0x08,
    "f": 0x09,
    "g": 0x0A,
    "h": 0x0B,
    "i": 0x0C,
    "j": 0x0D,
    "k": 0x0E,
    "l": 0x0F,
    "m": 0x10,
    "n": 0x11,
    "o": 0x12,
    "p": 0x13,
    "q": 0x14,
    "r": 0x15,
    "s": 0x16,
    "t": 0x17,
    "u": 0x18,
    "v": 0x19,
    "w": 0x1A,
    "x": 0x1B,
    "y": 0x1C,
    "z": 0x1D,
    " ": 0x2C,
}

def press_key(code):
    with open(HID_DEV, 'rb+') as fd:
        fd.write(bytes([0x00, 0x00, code, 0x00, 0x00, 0x00, 0x00, 0x00]))
        fd.write(bytes(8))  # Release key

def type_string(text):
    for char in text:
        code = KEY_CODES.get(char.lower(), 0)
        press_key(code)
        time.sleep(0.05)

if __name__ == "__main__":
    print("Typing payload...")
    type_string("hello world")
    press_key(KEY_CODES["ENTER"])
    print("Payload sent.")



















