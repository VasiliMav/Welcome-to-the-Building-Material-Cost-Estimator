
# Welcome to the Building Material Cost Estimator!

#EXERCISE FOR PYTHON (HARDWARE_2)

#GOALS_OF_THE_EXERCISE
#1. CALCULATE ROOM AREA
#2  CHOOSE FLOORING MATERIAL
#3  CALCULATE TOTAL COST
#4  SAVE PROJECT DETAILS 

import csv

# 1. CALCULATE ROOM AREA

TOTAL_AREA = 0  # Initially define the total area as 0

while True:
    try:
        ROOM_COUNT = int(input("Enter the number of rooms: "))  # The user can insert the number of rooms
        if ROOM_COUNT > 0:
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

for i in range(ROOM_COUNT):  # For each room apply the following
    print(f"Room {i+1}:")  # Display room number
    
    while True:
        try:
            LENGTH = float(input("What is the length of the room?: "))  # Get room length
            if LENGTH > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    while True:
        try:
            WIDTH = float(input("What is the width of the room?: "))  # Get room width
            if WIDTH > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    ROOM_AREA = LENGTH * WIDTH  # Calculate room area
    TOTAL_AREA += ROOM_AREA  # Add to total area
    print("The total area of this room is", ROOM_AREA, "square feet.")  # Display room area

print("The total area of all rooms is", TOTAL_AREA, "square feet.")  # Display total area

# 2. CHOOSE FLOORING MATERIAL

MATERIAL_OPTIONS = {"1": ("Wood", 8), "2": ("Concrete", 12), "3": ("Brick", 10), "4": ("Tiles", 5)}

print("Choose a material for the floor:")
print("1. Wood ($8/sq ft)")
print("2. Concrete ($12/sq ft)")
print("3. Brick ($10/sq ft)")
print("4. Tiles ($5/sq ft)")

while True:
    MATERIAL_CHOICE = input("Enter the number of the material: ")
    if MATERIAL_CHOICE in MATERIAL_OPTIONS:
        MATERIAL, MATERIAL_PRICE = MATERIAL_OPTIONS[MATERIAL_CHOICE]
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")

# 3. CALCULATE TOTAL COST

TOTAL_COST = MATERIAL_PRICE * TOTAL_AREA  # Calculate total flooring cost
print(MATERIAL, "has a cost of $", MATERIAL_PRICE, "/sq ft.")  # Display cost per square foot
print("In conclusion, the total cost for the floor is $", round(TOTAL_COST, 2))  # Display total cost

# 4. SAVE PROJECT DETAILS

while True:
    SAVE = input("Do you want to save this project? Type y for yes and n for no: ").lower()  # Give the user the option to save project
    if SAVE == "y":
        with open("building_material_cost_estimator.csv", mode="a", newline="") as CSV_FILE:  # Open CSV file for appending
            WRITER = csv.writer(CSV_FILE)  # Create CSV writer
            WRITER.writerow(["Material", "Material cost", "Total Area", "Total Cost"])
            WRITER.writerow([MATERIAL, MATERIAL_PRICE, TOTAL_AREA, round(TOTAL_COST, 2)])  # Write project details
        print("Project saved successfully!")  # Confirm save
        break
    elif SAVE == "n":
        print("Thank you for using the estimator!")  
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

#Thank you for using the estimator!