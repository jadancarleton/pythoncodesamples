#Jadan Carleton
#Saturday, March 1st, 2025

#Problem 6: Car Class
#This program initializes a class that contains data about a car's model,
#year, color, type, and manufacturer. It also allows for this information
#to be retrieved individually, or all together as a set of full specs.


class car:

    def __init__(self, model, year, color, cartype, manufacturer):
        self.model = model
        self.year = year
        self.color = color
        self.cartype = cartype
        self.manufacturer = manufacturer

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_cartype(cartype):
        return self.cartype

    def get_manufacturer(self):
        return self.manufacturer

    def fullspecs(self):
        return str(self.year) + ' ' + self.manufacturer + ' ' + self.model + ' ' + self.color + ' ' + self.cartype


car1 = car("Corvette", 2012, "Blue", "Sports", "Chevrolet")
car2 = car("Jetta", 2020, "Black", "Sedan", "Volkswagen")


print(car1.get_color())
print(car1.get_model())
print(car2.get_color())
print(car1.fullspecs())
print(car2.fullspecs())
