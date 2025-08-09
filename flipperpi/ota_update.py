# Self-Updater from GitHub:

# Allows FlipperPi to download updated scripts directly from a GitHub repo, replacing local files. Ex. firmware/network update feature.
# Connects to GitHub over HTTPS.
# Downloads files from a raw URL 
# Saves/overwrites local versions in flipperpi/
# Optionally reboots or relaunches the menu.

# Make a GitHub Repo and follow the FilePathSetup.txt in this project.You’ll be referencing these raw URLs in the update script.

# Change instances of YOURUSER in the code to your username used in your repo

# Optionally add a version text file in the project to check where you last updated to, etc. 


import requests
import os

GITHUB_REPO = "https://raw.githubusercontent.com/YOURUSER/flipperpi/main/flipperpi/"
FILES_TO_UPDATE = [
    "main.py",
    "hid_keyboard.py",
    "cc1101_send.py",
    "nfc_reader.py",
    "ir_transmit.py",
    "ir_receive.py",
    "wifi_setup.py",
    "payload_locker.py",
    "usb_storage_toggle.py"
]

def download_file(filename):
    url = GITHUB_REPO + filename
    local_path = os.path.join(os.path.dirname(__file__), filename)
    try:
        print(f"Downloading {filename}...")
        response = requests.get(url)
        response.raise_for_status()
        with open(local_path, "w") as f:
            f.write(response.text)
        print(f"{filename} updated.")
    except Exception as e:
        print(f"Failed to update {filename}: {e}")

if __name__ == "__main__":
    print("Updating FlipperPi scripts from GitHub...\n")
    for fname in FILES_TO_UPDATE:
        download_file(fname)
    print("\n Update complete.")

