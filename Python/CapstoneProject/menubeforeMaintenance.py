def menuBeforeMaintenance():
    while True:
        print("Menu:")
        print("1. Display Selected Cars")
        print("2. Update Maintenance Status")
        print("3. Main Menu")
        choice = keyboardInput(int, "Enter your choice (1/2/3): ", "Choice must be an integer")

        if choice not in [1, 2, 3]:
            print("Invalid choice. Please enter a valid option.")
            continue

        if choice == 3:
            print ("We will go back to Main Menu.")
            main()
            break

        displayCM()
        no_plat = input("Enter the number plate of the car: ").strip()
        if no_plat == "":
            print("No car plate entered. Please try again.")
            continue
        elif no_plat == "exit":
            print("Exiting...")
            break

        if choice == 1:
            clear_screen()
            display_selected_cars(no_plat)
        elif choice == 2:
            clear_screen()
            updateCM(no_plat)