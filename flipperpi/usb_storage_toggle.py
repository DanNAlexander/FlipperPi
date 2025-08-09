# Enable/Disable USB Mass Storage Mode

# Used to simulate a USB flash drive when FlipperPi is plugged into a host computer, similar to Flipper Zero’s USB storage mode.


# Uses Linux g_mass_storage kernel module.
# Toggles between:
# Enabling USB mass storage with a backing .img file 
# Disabling the gadget and reverting USB state

# Works on Pi Zero 2 W via OTG (USB OTG port = USB port, not PWR)


# Create a small .img file to simulate a USB drive
# Add to: flipperpi/files/storage.img manually or see below to use dd

# Create a storage.img in dd via BASH:
# dd if=/dev/zero of=storage.img bs=1M count=32
# mkfs.vfat storage.img
# Then move that file to: /home/pi/flipperpi/files/storage.img



import subprocess
import os

GADGET_PATH = "/sys/kernel/config/usb_gadget/flipperpi"
IMAGE_PATH = "/home/pi/flipperpi/files/storage.img"

def enable_usb_mass_storage():
    print("Enabling USB Mass Storage...")
    os.makedirs(GADGET_PATH, exist_ok=True)

    cmds = [
        f"modprobe g_mass_storage file={IMAGE_PATH} stall=0 removable=1 ro=0",
    ]

    for cmd in cmds:
        subprocess.run(cmd, shell=True, check=False)

    print("Mass Storage Mode enabled.")

def disable_usb_mass_storage():
    print("Disabling USB Mass Storage...")
    subprocess.run("rmmod g_mass_storage", shell=True)
    print("Disabled.")

if __name__ == "__main__":
    print("[1] Enable USB storage")
    print("[2] Disable USB storage")
    choice = input("Choose option: ").strip()
    
    if choice == "1":
        enable_usb_mass_storage()
    elif choice == "2":
        disable_usb_mass_storage()
    else:
        print("Invalid choice.")

