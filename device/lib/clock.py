# Uhr-/Timer-Logik. Beispielmodul – nach Bedarf erweitern.
import time


class Clock:
    def __init__(self):
        self._start = time.ticks_ms()

    def reset(self):
        self._start = time.ticks_ms()

    def elapsed_ms(self):
        return time.ticks_diff(time.ticks_ms(), self._start)

    def elapsed_s(self):
        return self.elapsed_ms() // 1000
