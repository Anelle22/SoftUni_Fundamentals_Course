shelf_of_books = input().split("&")

while True:
    command = input()
    if command == "Done":
        break

    instructions = command.split(" | ")
    action = instructions[0].split(" ")
    book_name = instructions[1]

    if action[0] == "Add":
        if book_name not in shelf_of_books:
            shelf_of_books.insert(0, book_name)

    elif action[0] == "Take":
        if book_name in shelf_of_books:
            shelf_of_books.remove(book_name)

    elif action[0] == "Swap":
        second_book_name = instructions[2]
        if book_name in shelf_of_books and second_book_name in shelf_of_books:
            first_book_index = shelf_of_books.index(book_name)
            second_book_index = shelf_of_books.index(second_book_name)
            shelf_of_books[first_book_index], shelf_of_books[second_book_index] = shelf_of_books[second_book_index], shelf_of_books[first_book_index]

    elif action[0] == "Insert":
        if book_name not in shelf_of_books:
            shelf_of_books.append(book_name)

    elif action[0] == "Check":
        index = int(book_name)
        if index in range(len(shelf_of_books)):
            print(shelf_of_books[index])

print(", ".join(shelf_of_books))



