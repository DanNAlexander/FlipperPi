# FlipperPi

A DIY Flipper Zero–style multi-tool running on a **Raspberry Pi Zero 2 W**. Control HID attacks, sub-GHz RF, NFC, and USB storage tricks from any browser on your local network.

> ⚠️ **For educational and authorized testing use only.** Don't deploy this against systems or signals you don't own or have explicit permission to test.

---

## 🚀 Quick Start

Once installed (see below), launch the app on your Pi:

```bash
cd flipperpi/web
python3 app.py
```

Then visit `http://<Pi-IP>:5000` from any device on the same network.

---

## 📑 Table of Contents

- [Hardware](#-hardware)
- [Installation](#-installation)
  - [1. Flash Raspberry Pi OS Lite](#1-flash-raspberry-pi-os-lite)
  - [2. First Boot](#2-first-boot)
  - [3. Install Required Packages](#3-install-required-packages)
  - [4. Deploy the Project](#4-deploy-the-flipperpi-project)
- [Using the Web UI](#-using-the-web-ui)
- [Run on Boot](#-run-on-boot)
- [License](#-license)

---

## 🔧 Hardware

- Raspberry Pi Zero 2 W
- microSD card (8 GB+)
- *(Optional)* CC1101 RF module — connected via SPI
- *(Optional)* MFRC522 NFC reader — connected via SPI / I²C

---

## 📦 Installation

### 1. Flash Raspberry Pi OS Lite

Download the [Raspberry Pi Imager](https://www.raspberrypi.com/software/) and configure:

| Setting | Value |
| --- | --- |
| OS | Raspberry Pi OS Lite (64-bit) |
| Storage | Your microSD card |
| Hostname | `flipperpi` |
| SSH | ✅ Enabled |
| Wi-Fi | Your SSID & password |

> 💡 Click the **gear icon** in Imager to access SSH, Wi-Fi, and hostname options before flashing.

Flash the card and insert it into the Pi.

### 2. First Boot

Power on the Pi Zero 2 W and SSH in from your PC:

```bash
ssh pi@flipperpi.local
```

> **Default password:** `raspberry` — change it on first login with `passwd`.

Update the system:

```bash
sudo apt update && sudo apt upgrade -y
```

### 3. Install Required Packages

Install Python, Flask, and supporting libraries:

```bash
sudo apt install python3 python3-pip git -y
pip3 install flask spidev mfrc522
```

If you're using the **CC1101 RF module** or **NFC reader**, enable the relevant interfaces:

```bash
sudo raspi-config
```

Enable **SPI** (for CC1101) and **I²C** (for the NFC reader), then reboot:

```bash
sudo reboot
```

### 4. Deploy the FlipperPi Project

From your host PC, copy the project to the Pi:

```bash
scp -r flipperpi_project_full pi@flipperpi.local:/home/pi/
```

On the Pi, launch the app:

```bash
cd ~/flipperpi_project/flipperpi/web
python3 app.py
```

---

## 🖥️ Using the Web UI

Open your browser and navigate to:

```
http://flipperpi.local:5000
```

Enter the PIN you set in `app.py` (**default:** `1234`).

| Button | Script | Function |
| --- | --- | --- |
| 🎹 **HID attack** | `hid_keyboard.py` | Emulates a keyboard for scripted input |
| 📡 **RF send** | `cc1101_send.py` | Transmits a sub-GHz signal via CC1101 |
| 💳 **NFC read** | `nfc_reader.py` | Reads an NFC/RFID tag |
| 💾 **USB storage toggle** | `usb_storage_toggle.py` | Toggles USB mass-storage mode |

> 🔐 Change the default PIN in `app.py` before exposing the Pi to anything beyond your trusted LAN.

---

## 🔁 Run on Boot

To launch FlipperPi automatically at startup, edit `/etc/rc.local`:

```bash
sudo nano /etc/rc.local
```

Add this line **before** `exit 0`:

```bash
python3 /home/pi/flipperpi_project/flipperpi/web/app.py &
```

Save and reboot:

```bash
sudo reboot
```

---

## 📄 License

This project is licensed under the **GNU Affero General Public License v3.0**. See [`LICENSE`](LICENSE) for details.

Copyright © 2026 Danton Alexander
