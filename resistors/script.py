with open('Widerstand.txt') as file:
    for line in file:
        line = line.strip().split('=')
        print(f'{line[0]}={eval(line[1].replace("<", "(").replace(">", ")").replace("-", "+"))}')
file.close()
