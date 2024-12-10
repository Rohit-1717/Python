class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand + " !"

    def full_Name(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):
        return "Petrol or Diesel"

    @staticmethod  # Decorator
    def general_description():
        return "Cars are means of transport."

    @property  # Decorator not changeable
    def model(self):
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"


my_tesla = ElectricCar("Tesla", "Model S", "85Kwh")

# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla,ElectricCar))

# print(my_tesla.__brand)
# print(my_tesla.get_brand())

# print(my_tesla.fuel_type())

# Car("Tata", "Safari")
# my_car = Car("Mahindra", "BSixE")
# my_car.model = "Bolero"

# print(my_car.model)
# print(safari.fuel_type())

# print(my_car.general_description())
# print(Car.general_description())


# print(Car.total_car)


# print(my_tesla.full_Name())

# my_car = Car("Mahindra", "xl6")
# print(my_car.brand)
# print(my_car.full_Name())


class Battery:
    def battery_info(self):
        return "This is Battery"


class Engine:
    def engine_info(self):
        return "This is Engine"


class ElectricCarTwo(Battery, Engine, Car):
    pass


my_new_tesla = ElectricCarTwo("tesla", "S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())
