# 1. Write a python program for the implementation of vacuum cleaner

# Function to clean a room
def vacuum_cleaner(room_status):
    for room in room_status:
        if room_status[room] == "Dirty":
            print("Room", room, "is Dirty.")
            print("Cleaning Room", room, "...")
            room_status[room] = "Clean"
        else:
            print("Room", room, "is already Clean.")

    print("\nFinal Room Status:")
    for room in room_status:
        print("Room", room, ":", room_status[room])

# Input room status
room_status = {
    "A": input("Enter status of Room A (Clean/Dirty): "),
    "B": input("Enter status of Room B (Clean/Dirty): ")
}

# Run Vacuum Cleaner
vacuum_cleaner(room_status)