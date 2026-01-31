n = int(input())
list_positives = []
list_negatives = []
sum_of_negatives = 0

for i in range(n):
    number = int(input())
    if number >= 0:
        list_positives.append(number)
    else:
        list_negatives.append(number)
        sum_of_negatives += number

print(list_positives)
print(list_negatives)
print(f"Count of positives: {len(list_positives)}")
print(f"Sum of negatives: {sum_of_negatives}")
