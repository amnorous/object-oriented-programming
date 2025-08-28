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

class Superhero(Character):
    def __init__(self, name, power_level, superpower):
        super().__init__(name, power_level)
        self.superpower = superpower

    def use_power(self):
        return f"{self.name} uses {self.superpower} to save the day!"

    # Polymorphism: override introduce
    def introduce(self):
        return f"Hero {self.name} here! Power: {self.superpower}, Level: {self._power_level}"

class Villain(Character):
    def __init__(self, name, power_level, evil_plan):
        super().__init__(name, power_level)
        self.evil_plan = evil_plan

    def execute_plan(self):
        return f"{self.name} executes the evil plan: {self.evil_plan}!"

    # Polymorphism: override introduce
    def introduce(self):
        return f"Villain {self.name} lurks in the shadows... Power Level: {self._power_level}"

hero = Superhero("Photon", 85, "Light Beam")
villain = Villain("Darkthorn", 90, "Plunge world into darkness")

print(hero.introduce())
print(hero.use_power())

print(villain.introduce())
print(villain.execute_plan())

# Encapsulation in action
print(hero.get_power_level())
hero.set_power_level(95)
print(hero.get_power_level())


