def main():
    days = int(input("Enter the number of days: "))
    temperatures = []

    # Input temperatures
    for i in range(days):
        temp = float(input(f"Enter temperature for day {i + 1}: "))
        temperatures.append(temp)

    # Calculate average temperature
    total_temperature = sum(temperatures)
    average_temperature = total_temperature / days
    print("Average temperature:", average_temperature)

    # Count days with temperature above average
    days_above_average = sum(1 for temp in temperatures if temp > average_temperature)
    print("Number of days with temperature above average:", days_above_average)


 
main()
