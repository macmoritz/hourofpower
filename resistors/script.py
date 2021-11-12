import re

with open('Widerstand.txt') as file:
    for line in file:
        line = line.strip().split('=')
        formula = re.sub(r'<([0-9]+)/([0-9]+)>', r'1/(1/\1+1/\2)', line[1]).replace('<', '(').replace('>', ')').replace('-', '+')
        print(f'{line[0]}\t=\t{eval(formula)}\t≈\t{int(round(eval(formula), -1))}')

