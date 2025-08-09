# Infrared Signal Transmitter:
# Send IR signals (e.g., TV remote commands) using GPIO and an IR LED — mimicking Flipper Zero’s IR sending.
#Works via main.py option 3 — sends NEC IR signal using real carrier frequency

# Uses PWM (Pulse Width Modulation) to generate a 38kHz IR carrier.
# Modulates the carrier with NEC-encoded data (commonly used in remotes).


# Hardware Setup:
# IR LED to GPIO18 (PWM pin):
# GPIO18 (Pin 12) → 220Ω Resistor → IR LED → GND


# Enable hardware PWM on GPIO18 (used by pigpio)in BASH:
# Install pigpio daemon for hardware PWM:
# sudo apt install pigpio python3-pigpio
# sudo systemctl enable pigpiod
# sudo systemctl start pigpiod


import pigpio
import time

# NEC Protocol encoding
def send_nec_code(gpio, pi, code):
    def send_mark(duration):
        pi.hardware_PWM(gpio, 38000, 500000)  # 38kHz, 50% duty
        time.sleep(duration)
        pi.hardware_PWM(gpio, 0, 0)

    def send_space(duration):
        time.sleep(duration)

    print(f"Sending NEC code: {hex(code)}")
    
    # Send leading mark + space
    send_mark(0.009)   # 9ms
    send_space(0.0045) # 4.5ms

    # Send 32 bits
    for i in range(32):
        send_mark(0.000562)
        if code & (1 << (31 - i)):
            send_space(0.00169)
        else:
            send_space(0.000562)

    # Stop bit
    send_mark(0.000562)
    send_space(0.04)  # End frame

# MAIN
if __name__ == "__main__":
    pi = pigpio.pi()
    if not pi.connected:
        print("Could not connect to pigpio daemon.")
        exit(1)

    GPIO = 18  # PWM output pin
    try:
        remote_code = 0x20DF10EF  # Example: Samsung power button
        send_nec_code(GPIO, pi, remote_code)
        print("IR signal sent.")
    finally:
        pi.hardware_PWM(GPIO, 0, 0)
        pi.stop()

















