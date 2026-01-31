people_waiting = int(input())
current_lift = input().split(" ")
new_lift_position = []

for wagon in current_lift:
    taken_spaces = int(wagon)
    free_spaces = 4 - taken_spaces
    if taken_spaces < 4:
        if people_waiting >= free_spaces:
            spaces_now_taken = 4
            people_waiting -= free_spaces
        else:
            spaces_now_taken = people_waiting + taken_spaces
            people_waiting -= people_waiting

        new_lift_position.append(str(spaces_now_taken))

    else:
        new_lift_position.append(str(wagon))
        continue

lift_full = True
for wagon in new_lift_position:
    if int(wagon) != 4:
        lift_full = False

if lift_full == False and people_waiting <=0:
    print("The lift has empty spots!")
    print(" ".join(new_lift_position))

if lift_full and people_waiting > 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    print(" ".join(new_lift_position))

if lift_full and people_waiting <= 0:
    print(" ".join(new_lift_position))

