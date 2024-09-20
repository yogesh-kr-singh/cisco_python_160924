class CabVehicle:
    def __init__(self, vehicle_no, category, fare):
        self.vehicle_no = vehicle_no
        self.category = category
        self.fare = fare

    def __str__(self):
        return f'[vehicle_no={self.vehicle_no}, category={self.category}, fare={self.fare}]'

    def __repr__(self):
        return self.__str__()

cab_vehicles = []

def add_cab_vehicle(vehicle_no, category, fare):
    global cab_vehicles
    cab_vehicle = CabVehicle(vehicle_no, category, fare)
    cab_vehicles.append(cab_vehicle)
    print('Cab vehicle added successfully')

def remove_cab_vehicle(vehicle_no):
    global cab_vehicles
    for cab_vehicle in cab_vehicles:
        if cab_vehicle.vehicle_no == vehicle_no:
            print(cab_vehicle)
            if input('Are you sure to delete (yes/no)?').lower() == 'yes':
                cab_vehicles.remove(cab_vehicle)
                print('Cab vehicle deleted successfully')
            return
    print(f'No such cab vehicle {vehicle_no}')

def display_cab_vehicles():
    global cab_vehicles
    for cab_vehicle in cab_vehicles:
        print(cab_vehicle)

def display_cab_vehicle_by_no(vehicle_no):
    global cab_vehicles
    for cab_vehicle in cab_vehicles:
        if cab_vehicle.vehicle_no == vehicle_no:
            print(cab_vehicle)
            return
    print('Invalid cab vehicle number')

def update_cab_vehicle(vehicle_no):
    global cab_vehicles
    for cab_vehicle in cab_vehicles:
        if cab_vehicle.vehicle_no == vehicle_no:
            print(cab_vehicle)
            category = input(f'Enter new category ({cab_vehicle.category}): ')
            fare = float(input(f'Enter new fare ({cab_vehicle.fare}): '))  # Ensure fare is stored as a float
            cab_vehicle.category = category
            cab_vehicle.fare = fare
            print('Cab vehicle updated successfully')
            return
    print(f'No such cab vehicle {vehicle_no}')

def menu():
    choice = int(input('''1-add cab vehicle
2-delete cab vehicle by number
3-display all cab vehicles
4-read cab vehicle by number
5-update cab vehicle by number
7-end
your choice: '''))
    if choice == 1:
        vehicle_no = input('Enter cab vehicle number: ')
        category = input('Enter cab vehicle category: ')
        fare = float(input('Enter cab vehicle fare: '))  # Ensure fare is entered as a float
        add_cab_vehicle(vehicle_no, category, fare)
    elif choice == 2:
        vehicle_no = input('Enter cab vehicle number to delete: ')
        remove_cab_vehicle(vehicle_no)
    elif choice == 3:
        display_cab_vehicles()
    elif choice == 4:
        vehicle_no = input('Enter cab vehicle number: ')
        display_cab_vehicle_by_no(vehicle_no)
    elif choice == 5:
        vehicle_no = input('Enter cab vehicle number: ')
        update_cab_vehicle(vehicle_no)
    elif choice == 7:
        pass
    else:
        print('Invalid menu')
    return choice

def menus():
    choice = menu()
    while choice != 7:
        choice = menu()
    print('Thank you for using the app')

menus()