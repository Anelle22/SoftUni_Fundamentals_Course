words = input().split(" ")

updated_words = [word for word in words if len(word) % 2 == 0]

print("\n".join(updated_words))

