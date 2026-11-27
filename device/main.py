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


