def findLoopSize(publicKey):
    value, loops = 1, 0
    while value != publicKey:
        value = (value * 7) % 20201227
        loops += 1
    return loops


def transform(subject, loopSize):
    value = 1
    for _ in range(0, loopSize):
        value = (subject * value) % 20201227
    return value


if __name__ == '__main__':
    with open('input.txt') as file:
        doorPublicKey, cardPublicKey = [int(line.strip()) for line in file if line != '\n']
    doorLoopSize, cardLoopSize = findLoopSize(doorPublicKey), findLoopSize(cardPublicKey)
    encryptionKey1, encryptionKey2 = pow(doorPublicKey, cardLoopSize, 20201227), pow(cardPublicKey, doorLoopSize, 20201227)
    # encryptionKey1, encryptionKey2 = transform(doorPublicKey, cardLoopSize), transform(cardPublicKey, doorLoopSize)

    if encryptionKey1 == encryptionKey2: print(f'encryption key is {encryptionKey1}')
