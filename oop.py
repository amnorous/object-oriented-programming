class Character:
    def __init__(self, name, power_level):
        self.name = name
        self._power_level = power_level  # Encapsulated (protected)

    def introduce(self):
        return f"I am {self.name} with a power level of {self._power_level}!"

    def get_power_level(self):
        return self._power_level

    def set_power_level(self, new_level):
        if new_level >= 0:
            self._power_level = new_level
        else:
            print("Power level can't be negative.")
