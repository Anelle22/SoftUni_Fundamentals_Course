schedule_of_lessons = input().split(", ")

while True:
    command = input()
    if command == "course start":
        break

    instructions = command.split(":")
    action, lesson_title = instructions[0], instructions[1]

    if action == "Add":
        if lesson_title not in schedule_of_lessons:
            schedule_of_lessons.append(lesson_title)

    elif action == "Insert":
        index = int(instructions[2])
        if lesson_title not in schedule_of_lessons:
            schedule_of_lessons.insert(index, lesson_title)

    elif action == "Remove":
        if lesson_title in schedule_of_lessons:
            schedule_of_lessons.remove(lesson_title)
        if (lesson_title + "-Exercise") in schedule_of_lessons:
            schedule_of_lessons.remove(lesson_title + "-Exercise")

    elif action == "Swap":
        lesson_title_two = instructions[2]
        if lesson_title in schedule_of_lessons and lesson_title_two in schedule_of_lessons:
            index_of_lesson_title = schedule_of_lessons.index(lesson_title)
            index_of_lesson_title_two = schedule_of_lessons.index(lesson_title_two)
            schedule_of_lessons[index_of_lesson_title], schedule_of_lessons[index_of_lesson_title_two] = schedule_of_lessons[index_of_lesson_title_two], schedule_of_lessons[index_of_lesson_title]

        if (lesson_title + "-Exercise") in schedule_of_lessons:
            index_of_lesson_title = schedule_of_lessons.index(lesson_title)
            schedule_of_lessons.remove(lesson_title + "-Exercise")
            schedule_of_lessons.insert(index_of_lesson_title + 1, lesson_title + "-Exercise")

        if (lesson_title_two + "-Exercise") in schedule_of_lessons:
            index_of_lesson_title_two = schedule_of_lessons.index(lesson_title_two)
            schedule_of_lessons.remove(lesson_title_two + "-Exercise")
            schedule_of_lessons.insert(index_of_lesson_title_two + 1, lesson_title_two + "-Exercise")


    elif action == "Exercise":
        if lesson_title in schedule_of_lessons:
            if (lesson_title + "-Exercise") not in schedule_of_lessons:
                index_of_lesson_title = schedule_of_lessons.index(lesson_title)
                schedule_of_lessons.insert(index_of_lesson_title + 1, lesson_title + "-Exercise")
        else:
            schedule_of_lessons.append(lesson_title)
            schedule_of_lessons.append(lesson_title + "-Exercise")

numerator = 1
for element in schedule_of_lessons:
    print(f"{numerator}.{element}")
    numerator += 1


