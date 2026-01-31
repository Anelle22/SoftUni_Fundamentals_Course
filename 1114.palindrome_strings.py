words = input().split()
searched_palindrome = input()
palindromes = [word for word in words if word == word[::-1]]


print(palindromes)
print(f"Found palindrome {words.count(searched_palindrome)} times")
