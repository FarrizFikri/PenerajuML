def menuOne(file_name):
    cars = {}
    with open(file_name, 'r') as file:
        for line in file:
            car = eval(line.strip())
            number_plate = list(car.keys())[0]
            cars[number_plate] = car[number_plate]

    while True:
        print("=" * 60)
        print("\t\tCar Maintenance Tracking System")
        print("=" * 60)
        print("1. Select a Car")
        print("2. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            print("Select a Car:")
            for i, (number_plate, car) in enumerate(cars.items(), 1):
                print(f"{i}. {number_plate} - {car['model']} ({car['brand']}, {car['color']})")
            car_choice = int(input("Enter the car number: "))
            if 1 <= car_choice <= len(cars):
                number_plate = list(cars.keys())[car_choice - 1]
                selected_car = cars[number_plate]
                print(f"You have selected {number_plate} - {selected_car['model']} ({selected_car['brand']}, {selected_car['color']})")
            else:
                print("Invalid car number. Please try again.")
        elif choice == '2':
            print("Thank you for using the Car Maintenance Tracking System")
            break
        else:
            print("Invalid choice. Please try again.")

menuOne("listofcars.txt")

