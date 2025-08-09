
This is a DIY Flipper Zero-style multi-tool running on Raspberry Pi Zero 2.


Run the app on your Pi in BASH:
cd flipperpi/web
python3 app.py
Then visit http://<Pi-IP>:5000 from any device on the same network.






-------------------------------------------------------------------------------
INSTALLATION & HARDWARE SET-UP
-------------------------------------------------------------------------------


FLASH RASPBERRY PI OS LITE:

Download Raspberry Pi Imager:
https://www.raspberrypi.com/software/

OS: Raspberry Pi OS Lite (64-bit)
Storage: Your microSD card

Click the gear icon in Imager:
Enable SSH
Set Wi-Fi SSID & Password
Set hostname: flipperpi

Flash the card and insert into your Pi.






FIRST BOOT:

Power on the Pi Zero 2 W
Defauly Passs: raspberry

Connect via SSH from your PC
EX. PowerShell: ssh pi@flipperpi.local

Update system in BASH:
sudo apt update && sudo apt upgrade -y






INSTALL REQUIRED PACKAGES:

Install Python & Flask in BASH:
sudo apt install python3 python3-pip git -y
pip3 install flask spidev mfrc522

If you are using an RF CC1101 module via SPI, in BASH:
sudo raspi-config
Then Enable SPI, I2C (NFC reader requirement). Reboot once changed.








DEPLOY THE FLIPPERPI PROJECT:

In your host PC:
EX. PowerShell: scp -r flipperpi_project_full pi@flipperpi.local:/home/pi/

In the PI BASH:
cd ~/flipperpi_project/flipperpi/web
python3 app.py






TEST THE WEB UI:

On your host PC's browser: http://flipperpi.local:5000

Enter the PIN you set in app.py (default: 1234)

Try pressing:
HID attack → Executes hid_keyboard.py
RF send → Executes cc1101_send.py
NFC read → Runs nfc_reader.py
USB storage toggle → Runs usb_storage_toggle.py







SET FLASK TO RUN AT BOOT:

In PI BASH:
sudo nano /etc/rc.local

Before the exit 0 line, add:
python3 /home/pi/flipperpi_project/flipperpi/web/app.py &

Save and reboot:
sudo reboot



