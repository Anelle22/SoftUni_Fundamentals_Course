fires_input = input().split("#")
water = int(input())

valid_ranges = {
    "High": range(81, 126),
    "Medium": range(51, 81),
    "Low": range(1, 51)
}

cells_put_out = []
effort = 0
total_fire = 0

for fire in fires_input:
    fire_type, value = fire.split(" = ")
    value = int(value)

    # Check if the fire value is in the valid range for its type
    if value in valid_ranges[fire_type]:
        if water >= value:
            water -= value
            cells_put_out.append(value)
            effort += value * 0.25
            total_fire += value

# Print results
print("Cells:")
for cell in cells_put_out:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")