import re

with open('w.txt') as file:
    for line in file:
        line = line.strip().split('=')
        formula = line[1]
        while any(symbol in formula for symbol in ['<', '<', '(', ')', '-', '+', '/']):
            formula = eval(re.sub(r'<(([0-9]*>))/([0-9]*)>', r'1/(1/\1+1/\2)', str(formula)).replace('<', '(').replace('>', ')').replace('-', '+'))
        print(line[0], formula)
        print(f'{line[0]}\t=\t{formula}\t≈\t{int(round(formula, -1))}')
