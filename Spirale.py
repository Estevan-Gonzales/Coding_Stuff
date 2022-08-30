import sys

target_values = []
print(" ")

with open(sys.argv[1], 'r') as file: #
    for line in file:
        line = line.rstrip()
        target_values.append(int(line))

dimension = target_values.pop(0)
max_side = int((dimension - 1) / 2)

x = 0
y = 0
value = 1
positions = []
values = []

positions.append((x,y))
values.append(value)

def update_spiral():
    positions.append((x,y))
    values.append(value)

for bound in range(1, max_side + 1):
    while x < bound:
        x += 1
        value += 1
        update_spiral()
    while y > -1 * bound:
        y -= 1
        value += 1
        update_spiral()

    while x > -1 * bound:
        x -= 1
        value += 1
        update_spiral()

    while y < bound:
        y += 1
        value += 1
        update_spiral()

    while x < bound:
        x += 1
        value += 1
        update_spiral()


value_sum = 0
for target_value in target_values:
    for value in values:
        if value == target_value:
            target_position = positions[value - 1]
            value_sum = 0
            index = 0
            for position in positions:
                try:
                    if abs(position[0] - target_position[0]) <= 1:
                        if abs(position[1] - target_position[1]) <= 1:
                            if position != target_position:
                                value_sum += values[index]
                except:
                    1 == 1
                index += 1

    print(value_sum)
