def check_the_room(current_room):
    total_free_chairs = 0
    needed_chairs = 0
    for room in range(1, current_room + 1):
        free_chairs_in_room, visitors = input().split()
        difference = len(free_chairs_in_room) - int(visitors)
        if difference < 0:
            print(f"{abs(difference)} more chairs needed in room {room}")
            needed_chairs += abs(difference)
        else:
            total_free_chairs += difference

    return total_free_chairs, needed_chairs


number_of_rooms_in_business_center = int(input())
total_free_chairs, total_needed_chairs = check_the_room(number_of_rooms_in_business_center)
if total_free_chairs >= total_needed_chairs:
    print(f"Game On, {total_free_chairs} free chairs left")
