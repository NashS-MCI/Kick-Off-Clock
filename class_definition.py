class Taster: #Um den Button zu entprellen
    def __init__(self, pin_nr, entprell_ms=30):
        self.pin = Pin(pin_nr, Pin.IN, Pin.PULL_UP)
        self.entprell_ms = entprell_ms
        self.last_raw = self.pin.value() #quasi last_button_state ->letzte Ausgabe vom Pin
        self.stable = self.pin.value() #der entprellte gültige Zustand
        self.last_change = time.ticks_ms() #Zeitpunkt der letzten Pegeländerung
        self.first_edge = 0     # Zeit der ersten Flanke weg vom stabilen Zustand
        self.press_time = 0     # Zeit der letzten bestätigten Druck-Flanke

    def update(self):
        """Einmal pro Schleifendurchlauf aufrufen. True = gerade (entprellt) gedrückt."""
        gedrueckt = False
        raw = self.pin.value()
        if raw != self.last_raw:
            if self.last_raw == self.stable:
                self.first_edge = time.ticks_ms()
            self.last_raw = raw
            self.last_change = time.ticks_ms()
        if time.ticks_diff(time.ticks_ms(), self.last_change) >= self.entprell_ms and raw != self.stable:
            self.stable = raw
            if self.stable == 0:
                self.press_time = self.first_edge
                gedrueckt = True
        return gedrueckt