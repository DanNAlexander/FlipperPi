# Create hid_gadget.sh to define USB keyboard gadget:

# Save To:
# Local: /home/pi/flipperpi/hid_gadget.sh
# Global:/usr/local/bin/hid_gadget.sh
# BASH Pathing: chmod +x /home/pi/flipperpi/hid_gadget.sh


# How to Run It on Boot in BASH
# Edit /etc/rc.local and add before exit 0:
# bash /home/pi/flipperpi/hid_gadget.sh

# Or use a systemd service (optional but better) in BASH:
# sudo nano /etc/systemd/system/flipperhid.service
# and Paste in:
# [Unit]
# Description=Setup USB HID Gadget
# After=multi-user.target

# [Service]
# Type=oneshot
# ExecStart=/home/pi/flipperpi/hid_gadget.sh
# RemainAfterExit=true

# [Install]
# WantedBy=multi-user.target

# Then in BASH:
# sudo systemctl daemon-reexec
# sudo systemctl enable flipperhid
# sudo systemctl start flipperhid

# Confirm It Worked:
# After reboot or script execution use in BASH:
# ls /dev/hidg0



#Make it executable in BASH:
# chmod +x hid_gadget.sh

# !/bin/bash
modprobe libcomposite
cd /sys/kernel/config/usb_gadget/
mkdir -p hidgadget
cd hidgadget

echo 0x1d6b > idVendor
echo 0x0104 > idProduct
echo 0x0100 > bcdDevice
echo 0x0200 > bcdUSB

mkdir -p strings/0x409
echo "deadbeef1234" > strings/0x409/serialnumber
echo "FlipperPi" > strings/0x409/manufacturer
echo "HID Keyboard" > strings/0x409/product

mkdir -p configs/c.1/strings/0x409
echo "Config 1" > configs/c.1/strings/0x409/configuration
echo 120 > configs/c.1/MaxPower

mkdir -p functions/hid.usb0
echo 1 > functions/hid.usb0/protocol
echo 1 > functions/hid.usb0/subclass
echo 8 > functions/hid.usb0/report_length
echo -ne \\x05\\x01\\x09\\x06\\xa1\\x01\\x05\\x07\\x19\\xe0\\x29\\xe7\\x15\\x00\\x25\\x01\\x75\\x01\\x95\\x08\\x81\\x02\\x95\\x01\\x75\\x08\\x81\\x01\\x95\\x05\\x75\\x01\\x05\\x08\\x19\\x01\\x29\\x05\\x91\\x02\\x95\\x01\\x75\\x03\\x91\\x01\\x95\\x06\\x75\\x08\\x15\\x00\\x25\\x65\\x05\\x07\\x19\\x00\\x29\\x65\\x81\\x00 > functions/hid.usb0/report_desc

ln -s functions/hid.usb0 configs/c.1/
ls /sys/class/udc > UDC






