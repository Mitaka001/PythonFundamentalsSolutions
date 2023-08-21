gifts = input().split()

while True:
    command = input()

    if command == "No Money":
        break

    for gift in gifts:
        command_parts = command.split()
        action = command_parts[0]

        if action == "OutOfStock":
            gift_to_remove = command_parts[1]
            if gift_to_remove in gifts:
                index = int(gifts.index(gift_to_remove))
                gifts[index] = "None"

        elif action == "Required":
            gift_to_replace = command_parts[1]
            index = int(command_parts[2])
            if 0 <= index < len(gifts):
                gifts[index] = gift_to_replace

        elif action == "JustInCase":
            gifts[-1] = command_parts[1]

formatted_gifts = " ".join(gift for gift in gifts if gift is not "None")
print(formatted_gifts)
