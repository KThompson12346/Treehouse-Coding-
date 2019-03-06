import random

class Character:
    def __init__(self, name, **kwargs):
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)


class Thief(Character):
    sneaky = True

    def __init__(self, name, sneaky=True, **kwargs): # will override the parent class method __init__
        super().__init__(name, **kwargs) # a call to the parent classes __init__ method
        self.sneaky = True

    def pickpocket(self): # methods always take one parameter that represents the instance that uses the method, can use self to talk about current instance
        return self.sneaky and bool(random.randint(0, 1))


    def hide(self, light_level):
        return self.sneaky and light_level < 10




###########################################

class Student:
    name = "Your Name"

    def __init__(self, name, **kwargs):
        self.name = name
        for key, value in kwargs.items():
            setattr(self, key, value)

    def praise(self):
        return "You inspire me, {}".format(self.name)

    def reassurance(self):
        return "Chin up, {}. You'll get it next time!".format(self.name)

    def feedback(self, grade):
        if grade > 50:
            return self.praise()
        return self.reassurance()


##########################################

class RaceCar:

    def __init__(self, color, fuel_remaining, laps, **kwargs):
        self.color = color
        self.fuel_remaining = fuel_remaining
        self.laps = 0
        for key, value in kwargs.items():
            setattr(self, key, value)

    def run_lap(self, length):
            self.fuel_remaining -= length * 0.125
            self.laps += 1
