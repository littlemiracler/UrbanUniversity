class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


h1 = Building(25, 'Многоэтажка')
h2 = Building(1, 'Загородный дом')
print(h1 == h2)

h3 = Building(25, 'Многоэтажка')
h4 = Building(25, 'Многоэтажка')
print(h3 == h4)
