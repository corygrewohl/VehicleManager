from Vehicle import Vehicle, Car, Truck


class Inventory:
    def __init__(self):
        self.inventory = []

    def add_vehicle(self, vehicle: Vehicle):
        self.inventory.append(vehicle)

    def remove_vehicle(self, vehicle: Vehicle):
        self.inventory.remove(vehicle)

    def find_cheapest_vehicle(self):
        if len(self.inventory) > 0:
            vehicle_min = self.inventory[0].retail_price

            for i in range(len(self.inventory)):
                if self.inventory[i].retail_price < vehicle_min:
                    vehicle_min = self.inventory[i].retail_price

            return vehicle_min
        else:
            print("The given inventory contains no items.")

    def print_average_price_of_all_vehicles(self):
        average = 0

        for i in range(len(self.inventory)):
            average += self.inventory[i].retail_price

        average /= len(self.inventory)
        return average

    def print_list(self):
        print(self.inventory)
