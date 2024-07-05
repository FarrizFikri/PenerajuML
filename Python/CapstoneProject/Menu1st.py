#Function bawah ni utk tarik data details kereta dari file 

def read_cars_from_file(file_name):
    cars = []
    with open(file_name, 'r') as file:
        for line in file:
            number_plate, model, brand, color = line.strip().split(',')
            cars.append({'number_plate': number_plate, 'model': model, 'brand': brand, 'color': color})
    return cars

file_name = "listofcars.txt"
cars = read_cars_from_file(file_name)

while True:
    print("Car Maintenance Tracking System")
    print("-------------------------------")
    print("1. Select a Car")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        print("Select a Car:")
        print("Number Plate - Model (Brand, Color)")
        for i, car in enumerate(cars, 1):
            print(f"{i}. {car['number_plate']} - {car['model']} ({car['brand']}, {car['color']})")
        car_choice = int(input("Enter the car number: "))
        selected_car = cars[car_choice - 1]
        print(f"You have selected {selected_car['number_plate']} - {selected_car['model']} ({selected_car['brand']}, {selected_car['color']})")
    elif choice == '2':
        print("Thank you for using the Car Maintenance Tracking System")
        break
    else:
        print("Invalid choice. Please try again.")


