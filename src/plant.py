# Code taking and interpreting plant data
# Created:     2024-06-29
# Modified:    2024-06-29 (last status: working fine)
# Author:      Kagan Dikmen

# TODO: Add more plant types

class Plant:
    def __init__(self, name):
        self.name = name

    def optimalTemperature(self):
        match self.name:
            case "tulip":   return [4.5, 12]
            case "wheat":   return [12.5, 25]
            case "test":    return [-4, 45]
            case _:         return [100, 100]