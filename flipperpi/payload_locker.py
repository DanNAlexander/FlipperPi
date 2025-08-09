# PIN-Protected Payload Launcher

# This script adds a basic PIN-based lock around sensitive actions, like:
    # USB keystroke injection
    # Radio frequency spoofing    
    # Custom payload launches

# Prompts for a 4-digit PIN.
# If correct, runs the requested payload script (you can plug in any function or file).
# Stores the correct PIN in plain text for now (will be encrypted later).


# *** Security Note:
# *** This is a basic security layer, not suitable for sensitive applications but it keeps accidental misuse of tools like HID payloads or RF jammers under some control.




import getpass
import subprocess
import os

# For demo: simple plaintext pin check
PIN_FILE = os.path.join(os.path.dirname(__file__), "pin.txt")
PROTECTED_PAYLOAD = os.path.join(os.path.dirname(__file__), "hid_keyboard.py")

def load_pin():
    if not os.path.exists(PIN_FILE):
        with open(PIN_FILE, "w") as f:
            f.write("1234")  # Default PIN
    with open(PIN_FILE, "r") as f:
        return f.read().strip()

def run_protected_script():
    print(f"Protected payload: {os.path.basename(PROTECTED_PAYLOAD)}")
    pin = getpass.getpass("Enter PIN: ")
    if pin == load_pin():
        print("Access granted. Running payload...")
        subprocess.run(["python3", PROTECTED_PAYLOAD])
    else:
        print("Invalid PIN.")

if __name__ == "__main__":
    run_protected_script()

