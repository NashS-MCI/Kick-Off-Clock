# Einstiegspunkt: wird nach boot.py automatisch ausgeführt.
# Hier nur Module importieren und die Hauptschleife starten.
from machine import Pin, ADC, PWM
import time

from clock import Clock


def main():
    clock = Clock()
    while True:
        print("Laufzeit: {} s".format(clock.elapsed_s()))
        time.sleep(1)


main()

##Pinbelegung
RGB_LED_1 = PWM(Pin(...)) # TODO
RGB_LED_2 = PWM(Pin(...)) # TODO
RGB_LED_3 = PWM(Pin(...)) # TODO
RGB_LED_4 = PWM(Pin(...)) # TODO
LED_POTI_VORGABE = ADC(Pin(...)) # TODO
LED_POTI_AUFGABE = ADC(Pin(...)) # TODO
POTENTIOMETER = ADC(Pin(...)) # TODO
TASTER_LED_1 = Pin(..., Pin.IN, Pin.PULL_UP) # TODO
TASTER_LED_2 = Pin(..., Pin.IN, Pin.PULL_UP) # TODO
TASTER_LED_3 = Pin(..., Pin.IN, Pin.PULL_UP) # TODO
TASTER_LED_4 = Pin(..., Pin.IN, Pin.PULL_UP) # TODO
TASTER_START_STOP = Pin(..., Pin.IN, Pin.PULL_UP) # TODO
DISPLAY_SDA = Pin(...) # TODO
DISPLAY_SCL = Pin(...) # TODO
PULSOXYGEN_SDA = Pin(...) # TODO
PULSOXYGEN_SCL = Pin(...) # TODO
LAUTSPRECHER = Pin(...) # TODO

## Zustände
STATE_AUS = 0
STATE_AUFWACHEN = 1
STATE_FARBWECHSEL = 2
STATE_POTENTIOMETER = 3
STATE_PULSOXYGEN = 4
STATE_WACH = 5

state = STATE_AUS


while True:
    if state == STATE_AUS:
        pass
    elif state == STATE_AUFWACHEN:
        pass
    elif state == STATE_FARBWECHSEL:
        pass
    elif state == STATE_POTENTIOMETER:
        pass
    elif state == STATE_PULSOXYGEN:
        pass
    elif state == STATE_WACH:
        pass


    if state == STATE_AUS:
        pass
    elif state == STATE_AUFWACHEN:
        pass
    elif state == STATE_FARBWECHSEL:
        pass
    elif state == STATE_POTENTIOMETER:
        pass
    elif state == STATE_PULSOXYGEN:
        pass
    elif state == STATE_WACH:
        pass