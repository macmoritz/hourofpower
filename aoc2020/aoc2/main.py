valid1 = 0
valid2 = 0

with open('input.txt') as file:
    for line in file:
        line = line.strip()
        rule = line.split(':')[0]
        passwd = line.split(':')[1].strip()
        letter = rule[-1]
        occ_range = rule.split(' ')[0]
        low, high = int(occ_range.split('-')[0]), int(occ_range.split('-')[1])

        if low <= passwd.count(letter) <= high:
            valid1 += 1

        if (passwd[low - 1] == letter) ^ (passwd[high - 1] == letter):
            valid2 += 1

print(f'part1: {valid1} passwords are valid')
print(f'part2: {valid2} passwords are valid')
