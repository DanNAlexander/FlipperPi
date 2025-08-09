# Send RF signals (ASK/OOK/FSK) using a CC1101 module via SPI, similar to Flipper Zero's Sub-GHz feature.
# Uses spidev to communicate with the CC1101 chip over SPI.

# Sends a basic modulated payload (for example: simulated remote key fob).
# Note: This mockup assumes you're using the ELECHOUSE CC1101 module or similar on SPI pins.



import os

def show_menu():
    print("\n=== FlipperPi Main Menu ===")
    print("1. RF Signal Send (CC1101)")
    print("2. NFC Reader")
    print("3. IR Transmit")
    print("4. IR Receive")
    print("5. HID Payload")
    print("6. OTA Update")
    print("7. Wi-Fi Setup")
    print("8. Payload Locker")
    print("9. USB Mass Storage Toggle")
    print("0. Exit")

def run():
    while True:
        show_menu()
        choice = input("Select an option: ").strip()
        if choice == "1":
            os.system("python3 cc1101_send.py")
        elif choice == "2":
            os.system("python3 nfc_reader.py")
        elif choice == "3":
            os.system("python3 ir_transmit.py")
        elif choice == "4":
            os.system("python3 ir_receive.py")
        elif choice == "5":
            os.system("python3 hid_keyboard.py")
        elif choice == "6":
            os.system("python3 ota_update.py")
        elif choice == "7":
            os.system("python3 wifi_setup.py")
        elif choice == "8":
            os.system("python3 payload_locker.py")
        elif choice == "9":
            os.system("python3 usb_storage_toggle.py")
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid input.")

if __name__ == "__main__":
    run()
