# Wi-Fi Scanner & Connector

# Used to scan nearby Wi-Fi networks and allow the user to choose and connect to one by entering a password; similar to Flipper Zero’s Wi-Fi devboard management feature.

# Uses nmcli to scan and connect to networks.
# Interactive CLI input for SSID and password.
# Requires NetworkManager (included in Raspberry Pi OS Desktop; can be added to Lite).

# One-Time Setup in BASH:
# sudo apt install network-manager
# sudo systemctl stop dhcpcd
# sudo systemctl disable dhcpcd
# sudo systemctl enable NetworkManager
# sudo reboot



import subprocess

def scan_wifi():
    print("Scanning for networks...\n")
    try:
        result = subprocess.run(["nmcli", "-f", "SSID,SIGNAL", "dev", "wifi"], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"Scan failed: {e}")

def connect_wifi(ssid, password):
    print(f"Connecting to {ssid}...")
    try:
        subprocess.run(["nmcli", "dev", "wifi", "connect", ssid, "password", password], check=True)
        print("Connected!")
    except subprocess.CalledProcessError:
        print("Failed to connect. Check credentials.")

if __name__ == "__main__":
    scan_wifi()
    ssid = input("Enter SSID to connect: ").strip()
    password = input("Enter password: ").strip()
    connect_wifi(ssid, password)

