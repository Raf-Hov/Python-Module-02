class GardenError(Exception):
    def __init__(self, message="Unknown plant error"):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message="tomato"):
        self.meesage = "The " + message + " plant is"
        self.meesage += " wilting!"
        super().__init__(self.meesage)


class WaterError(GardenError):
    def __init__(self, message=None):
        if message:
            super().__init__(self.message)
        else:
            self.message = "Not enough "
            self.message += "water in the tank!"
            super().__init__(self.message)
