class Vehicle:
    def __init__(self, make, model, model_year, is_4_wheel_drive, retail_price, mpg):
        self.make = make
        self.model = model
        self.modelYear = model_year
        self.is4WheelDrive = is_4_wheel_drive
        self.retailPrice = retail_price
        self.MPG = mpg

        # test2


class Car(Vehicle):
    def __init__(self, make, model, model_year, is_4_wheel_drive, retail_price, mpg, is_convertible):
        self.is_convertible = is_convertible

        Vehicle.__init__(self, make, model, model_year, is_4_wheel_drive, retail_price, mpg)


class Truck(Vehicle):
    def __init__(self, make, model, model_year, is_4_wheel_drive, retail_price, mpg, has_side_step, tow_capacity):
        self.has_side_step = has_side_step
        self.tow_capacity = tow_capacity

        Vehicle.__init__(self, make, model, model_year, is_4_wheel_drive, retail_price, mpg)
