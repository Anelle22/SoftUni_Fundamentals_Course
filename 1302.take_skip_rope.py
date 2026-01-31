some_text = str(input())
digits_list = []
symbols_list = []
take_list = []
skip_list = []
result_string = []

for i in range(0, len(some_text)):
    if some_text[i].isdigit():
        digits_list.append(int(some_text[i]))
    else:
        symbols_list.append(some_text[i])

for i in range (0, len(digits_list)):
    if i % 2 == 0:
        take_list.append(digits_list[i])
    else:
        skip_list.append(digits_list[i])

for i in range(0, len(take_list)):
    take = int(take_list[i])
    skip = int(skip_list[i])
    if take != 0:
        for n in range(0, take):
            result_string.append(symbols_list[n])
        del symbols_list[:take]
    if skip != 0:
        del symbols_list[:skip]

print("".join(result_string))
