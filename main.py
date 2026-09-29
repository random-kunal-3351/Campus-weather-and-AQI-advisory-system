import logging
import inquiry

while True:
    print("\n--- Campus Health & AQI Advisory System ---")
    print("1. Log Today's AQI")
    print("2. Check Current Advisory")
    print("3. View AQI History")
    print("4. Exit")
    
    choice = input("Enter choice (1-4): ")

    if choice == '1':
        logging.log_aqi()

    elif choice == '2':
        inquiry.check_current()

    elif choice == '3':
        inquiry.view_history()

    elif choice == '4':
        print("Closing program...")
        break
        
    else:
        print("Wrong input. Please type 1, 2, 3, or 4.")