import array
import time

start = time.time()

# puzzle = [3, 8, 9, 1, 2, 5, 4, 6, 7]
puzzle = [6, 8, 5, 9, 7, 4, 2, 1, 3]
cups = array.array('i', puzzle)

cupsMin = min(cups)
cupsMax = max(cups)
cupsLen = len(cups)

for i in range(cupsMax + 1, 1_000_001):
    cups.append(i)

end = time.time()
print(f'creating the puzzle input took {end - start} seconds')


def arrayCurrentCups(array, current):
    data = [f'({a}) ' if index == current else f'{a} ' for index, a in enumerate(array)]
    return ''.join(data) 


def move(currentCupIndex):
    currentCup = cups[currentCupIndex]

    c1 = cups.pop((currentCupIndex + 1) % cupsLen)
    currentCupIndex = cups.index(currentCup)
    c2 = cups.pop((currentCupIndex + 1) % (cupsLen - 1))
    currentCupIndex = cups.index(currentCup)
    c3 = cups.pop((currentCupIndex + 1) % (cupsLen - 2))

    # print(f'pick up: {c1, c2, c3}')

    destinationCup = currentCup - 1

    while destinationCup in (c1, c2, c3) or destinationCup < cupsMin:
        destinationCup -= 1
        if destinationCup < cupsMin:
            destinationCup = cupsMax
    # print(f'destination: {destinationCup}\n')
    
    cups.insert(cups.index(destinationCup) + 1, c1)
    cups.insert(cups.index(destinationCup) + 2, c2)
    cups.insert(cups.index(destinationCup) + 3, c3)

    nextCupIndex = cups.index(currentCup) + 1
    if nextCupIndex == cupsLen: 
        nextCupIndex = 0
    return nextCupIndex

if __name__ == '__main__':
    start = time.time()
    currentCupIndex = 0
    for i in range(0, 10_000_000):
        if i % 1000 == 0:
            print(f'-- move {i + 1} --')
        # print(f'cups: {arrayCurrentCups(cups, currentCupIndex)}')
        currentCupIndex = move(currentCupIndex)

    # print('\n-- final --')
    # print(f'cups: {cups}')

    cupOneIndex = cups.index(1)
    print(f'next two labels on the cups after cup 1: {cups[cupOneIndex + 1]} * {cups[cupOneIndex + 2]} = {cups[cupOneIndex + 1] * cups[cupOneIndex + 2]}')
    end = time.time()
    print(f'{end - start} seconds')
