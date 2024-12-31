def calculate_area():
    while True:
        print("\nI can calculate the area of a shape for you.")
        shape = [
            "1. triangle",
            "2. rectangle",
            "3. square",
            "4. circle"
        ]

        # Display the shape options
        for option in shape:
            print(option)

        # Input validation loop
        calculate = ""
        while calculate not in ["1", "2", "3", "4"]:
            calculate = input("\nWhich shape do you want me to calculate the area of (1-4): ")

        # Process based on the user's choice
        if calculate == "1":
            base = float(input("Please enter the base of the triangle: "))
            height = float(input("Please enter the height of the triangle: "))
            area = 0.5 * base * height
            print(f"The area of the triangle is: {area:.2f} square units.")
        
        elif calculate == "2":
            length = float(input("Please enter the length of the rectangle: "))
            width = float(input("Please enter the width of the rectangle: "))
            area = length * width
            print(f"The area of the rectangle is: {area:.2f} square units.")
        
        elif calculate == "3":
            side = float(input("Please enter the side length of the square: "))
            area = side ** 2
            print(f"The area of the square is: {area:.2f} square units.")
        
        elif calculate == "4":
            radius = float(input("Please enter the radius of the circle: "))
            area = 3.14159 * radius ** 2
            print(f"The area of the circle is: {area:.2f} square units.")

        # Ask if the user wants to calculate again
        again = input("\nDo you want to calculate the area of another shape? (yes/no): ").lower()
        if again != "yes":
            print("Goodbye!")
            break  # Exit the loop and end the program

# Call the function to start the program
calculate_area()
