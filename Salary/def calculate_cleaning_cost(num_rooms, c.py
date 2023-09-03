# This program calculates the cost of the house cleaning based on the number of rooms and the type of cleaning.
def calculate_cleaning_cost(num_rooms, cleaning_type):
    # Define prices for different cleaning types
    prices = {
        "general cleaning": {"small": 40, "medium": 60, "large": 80},
        "deep cleaning": {"small": 55, "medium": 75, "large": 95},
        "mopping": {"small": 30, "medium": 50, "large": 70},
    }

    # Determine the size of the house based on the number of rooms
    house_size = ""
    if num_rooms <= 4:
        house_size = "small"
    elif num_rooms <= 8:
        house_size = "medium"
    else:
        house_size = "large"

    # Check if the cleaning type is valid
    if cleaning_type not in prices:
        return "Invalid cleaning type."

    # Calculate the cost based on house size and cleaning type
    cost = prices[cleaning_type][house_size]

    return cost


def main():
    # Get user input
    num_rooms = int(input("Enter the number of rooms in the house: "))
    print("Choose a cleaning type:")
    print("1. general cleaning")
    print("2. deep cleaning")
    print("3. mopping")
    choice = input("Enter the number of the cleaning type: ")

    # Map user choice to cleaning type
    cleaning_types = {
        "1": "general cleaning",
        "2": "deep cleaning",
        "3": "mopping",  
    }

    cleaning_type = cleaning_types.get(choice)

    if cleaning_type is None:
        print("Invalid choice. Please select a valid cleaning type.")
    else:
        # Calculate and display the cost
        cost = calculate_cleaning_cost(num_rooms, cleaning_type)
        print(f"The cost of {cleaning_type} cleaning for your [house_size] house is: ${cost}")


if __name__ == "__main__":
    main()