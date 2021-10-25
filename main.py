# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from Vehicle import Vehicle, Car, Truck


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
v = Vehicle("Ford", "F150", 2010, False, 25000, 12)
c = Car("Ford1", "F250", 2012, True, 20000, 14, True)
t = Truck("Ford", "F150", 2010, False, 25000, 12, True, 2000)

v.print_vehicle()
print()
c.print_vehicle()
print()
t.print_vehicle()
