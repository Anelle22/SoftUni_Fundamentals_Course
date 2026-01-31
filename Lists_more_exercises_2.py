numbers = input().split()
half_index = len(numbers) // 2
left_racer = numbers[:half_index]
right_racer = numbers[half_index + 1:]
right_racer.reverse()

left_racer_time = 0
right_racer_time = 0

for i in range(len(left_racer)):
    if left_racer[i] == '0':
        left_racer_time = left_racer_time * 0.8
    if right_racer[i] == '0':
        right_racer_time = right_racer_time * 0.8

    left_racer_time += int(left_racer[i])
    right_racer_time += int(right_racer[i])

if left_racer_time < right_racer_time:
    print(f"The winner is left with total time: {left_racer_time:.1f}")
else:
    print(f"The winner is right with total time: {right_racer_time:.1f}")
