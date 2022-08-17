# Problem #5
class Planet:
    def __init__(self, weight2, planet):
        self.weight2 = weight2
        self.planet = planet

    def calculate_spaceweight(self, weight2, planet):
        self.weight2 = weight2
        self.planet = planet
        planets = ["Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
        planetweights = [0.38, 0.91, 0.38, 2.34, 0.93, 0.92, 1.12, 0.62]
        self.weight2 = weight2
        for i in range(8):
            if planets[i] == planet:
                return print("Your weight will be", weight2 * planetweights[i])
                break
            else:
                continue



if __name__ == "__main__":
    weight = int(input("What is your weight?:"))
    destination = input("Where will you be going?:")
    p1 = Planet(weight, destination)
    p1.calculate_spaceweight(weight, destination)


