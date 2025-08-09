#BASH Installation
#sudo apt install python3-spidev


# This module will now work via the main menu (main.py) when option 1 is selected.


import spidev
import time

 
# SPI initialization
spi = spidev.SpiDev()
spi.open(0, 0)  # Bus 0, CE0
spi.max_speed_hz = 500000

# CC1101 registers (example subset)
CC1101_IOCFG2 = 0x00
CC1101_FREQ2 = 0x0D
CC1101_FREQ1 = 0x0E
CC1101_FREQ0 = 0x0F
CC1101_PKTLEN = 0x06
CC1101_PATABLE = 0x3E
CC1101_TXFIFO = 0x3F

def write_reg(addr, value):
    spi.xfer2([addr, value])
    time.sleep(0.01)

def write_burst(addr, data):
    spi.xfer2([addr | 0x40] + data)
    time.sleep(0.01)

def send_rf_signal(data):
    print("Sending RF signal...")
    
    # Set frequency (433 MHz)
    write_reg(CC1101_FREQ2, 0x10)
    write_reg(CC1101_FREQ1, 0xB0)
    write_reg(CC1101_FREQ0, 0x71)

    # Set packet length
    write_reg(CC1101_PKTLEN, len(data))

    # Send payload
    write_burst(CC1101_TXFIFO, data)
    print("TX complete.")

if __name__ == "__main__":
    # Example payload
    example_payload = [0xAA, 0xAA, 0xAA, 0xAA, 0xAB]  # Simulates OOK remote signal
    send_rf_signal(example_payload)
