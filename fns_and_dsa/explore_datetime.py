from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format the current date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return current_date  # Return the current date for use in Part 2

# Part 2: Calculate a Future Date
def calculate_future_date(current_date):
    # Prompt the user to enter the number of days to add
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        # Calculate the future date
        future_date = current_date + timedelta(days=days_to_add)
        # Format the future date as "YYYY-MM-DD"
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")
    except ValueError:
        print("Invalid input. Please enter an integer value for the number of days.")

# Main function to run the script
def main():
    current_date = display_current_datetime()  # Display the current date and time
    calculate_future_date(current_date)  # Calculate and display the future date

if __name__ == "__main__":
    main()
