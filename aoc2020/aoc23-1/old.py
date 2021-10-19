cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]
# cups = [6, 8, 5, 9, 7, 4, 2, 1, 3]

cups_min = min(cups)
cups_max = max(cups)


def arrayCurrentCups(array, current):
    data = [f'({a}) ' if index == current else f'{a} ' for index, a in enumerate(array)]
    return ''.join(data) 


for current_index in range(0, 10):
    print(f'-- move {current_index + 1} --')

    destination = cups[current_index % len(cups)] - 1
    print(f'cups: {arrayCurrentCups(cups, current_index)}')
    
    pickup = cups[current_index + 1 % len(cups):current_index + 4 % len(cups)]
    print(f'pick up: {pickup}')
    
    if destination <= cups_min:
        destination = cups_max

    while destination in pickup:
        destination -= 1
        if destination <= cups_min:
            destination = cups_max
    
    print(f'destination: {destination}\n')
    cups = [x for x in cups if x not in pickup]

    current_index = cups.index(destination)
    for index, pick in enumerate(pickup):
        cups.insert(current_index + index + 1 % len(cups), pick)

print('\n-- final --')
print(f'cups: {cups}')