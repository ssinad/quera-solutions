backseats = []
for cnt in range(4):
    name, door = [tmp for tmp in input().split()]
    if door == 'R':
        backseats.append(name)
    elif door == 'L':
        backseats.insert(0, name)
print(backseats[1])
