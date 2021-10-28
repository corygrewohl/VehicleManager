class Vehicle:
    def __init__(self, make, model, model_year, is_4_wheel_drive, retail_price, mpg):
        self.make = make
        self.model = model
        self.model_year = model_year
        self.is_4_wheel_drive = is_4_wheel_drive
        self.retail_price = retail_price
        self.mpg = mpg

    def print_vehicle(self):
        print(self.model_year)
        print(self.make)
        print(self.model)
        if self.is_4_wheel_drive is True:
            print("4WD")
        print("$" + f"{self.retail_price:,}")
        print(str(self.mpg) + "MPG")


class Car(Vehicle):
    def __init__(self, make, model, model_year, is_4_wheel_drive, retail_price, mpg, is_convertible):
        self.is_convertible = is_convertible

        Vehicle.__init__(self, make, model, model_year, is_4_wheel_drive, retail_price, mpg)

    def print_vehicle(self):
        super(Car, self).print_vehicle()
        print(self.is_convertible)


class Truck(Vehicle):
    def __init__(self, make, model, model_year, is_4_wheel_drive, retail_price, mpg, has_side_step, tow_capacity):
        self.has_side_step = has_side_step
        self.tow_capacity = tow_capacity

        Vehicle.__init__(self, make, model, model_year, is_4_wheel_drive, retail_price, mpg)

    def print_vehicle(self):
        super(Truck, self).print_vehicle()
        if self.has_side_step is True:
            print("Has Side Step")
        else:
            print("No Side Step")
        print("Tow up to " + str(self.tow_capacity) + " tons")
