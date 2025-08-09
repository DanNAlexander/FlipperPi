# Infrared Signal Receiver
# Receive and decode raw IR pulses using an IR receiver (e.g., VS1838B) connected to a GPIO pin. 
# Logs signals for later replay, like Flipper Zero’s IR capture feature.

# After 10 seconds of logging, it writes the signal pulse data to ir_log.txt, ready for replay or analysis.

# Hardware Setup:
# IR Receiver → GPIO 17:
# IR OUT (Signal) → GPIO17 (Pin 11)  
# VCC → 3.3V (Pin 1)  
# GND → GND (Pin 6)


# In BASH use pigpio again for precise microsecond pulse timing:
# sudo apt install python3-pigpio
# sudo systemctl start pigpiod



import pigpio
import time

IR_GPIO = 17

class IRLogger:
    def __init__(self, pi, gpio):
        self.pi = pi
        self.gpio = gpio
        self.last_tick = None
        self.pulses = []
        self.cb = self.pi.callback(self.gpio, pigpio.EITHER_EDGE, self._cb)

    def _cb(self, gpio, level, tick):
        if self.last_tick is not None:
            dt = pigpio.tickDiff(self.last_tick, tick)
            self.pulses.append((level, dt))
        self.last_tick = tick

    def stop(self):
        self.cb.cancel()

    def save(self, filename="ir_log.txt"):
        with open(filename, "w") as f:
            for level, duration in self.pulses:
                f.write(f"{level},{duration}\n")
        print(f"IR signal saved to {filename}")

if __name__ == "__main__":
    pi = pigpio.pi()
    if not pi.connected:
        print("Could not connect to pigpiod")
        exit(1)

    print("Listening for IR signals on GPIO17...")
    logger = IRLogger(pi, IR_GPIO)

    try:
        time.sleep(10)  # Listen for 10 seconds
    except KeyboardInterrupt:
        print("\n⏹ Interrupted by user.")
    finally:
        logger.stop()
        logger.save()
        pi.stop()












