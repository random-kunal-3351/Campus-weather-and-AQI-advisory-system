def get_valid_aqi():
    while True:
        try:
            val = int(input("Enter today's AQI score: "))
            if val < 0:
                print("AQI cannot be negative. Try again.")
                continue
            return val
        except ValueError:
            print("Invalid input! Please enter a number only.")