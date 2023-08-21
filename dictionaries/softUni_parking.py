registered_cars = {}
number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input().split()
    if command[0] == "register":
        username, license_plate_number = command[1], command[2]
        if username not in registered_cars.keys():
            registered_cars[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")
    if command[0] == "unregister":
        username = command[1]
        if username not in registered_cars.keys():
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del registered_cars[username]


for key, value in registered_cars.items():
    print(f"{key} => {value}")
