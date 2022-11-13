import random

def InputNumber(inputText):
    ok = False
    while not ok:
        try:
            number = int(input(f"{inputText}"))
            ok = True
        except ValueError:
            print("Error. Only integer numbers. Try again...")
    return number

def CreateListFromNegativeNtoN(N):
    array = []
    for i in range(-N, N + 1):
        array.append(i)
    return array

def CreateRandomList(elements, arrayLenght):
    array = []
    number = random.randint(0, arrayLenght)
    array.append(number)
    i = 1
    while i < elements:
        number = random.randint(0, arrayLenght)
        ok = True
        for j in array:
            if j == number:
                ok = False
        if ok:
            array.append(number)
            i += 1
    return array

def RandomNumbersForFileTxt(number):
    data = open('file.txt', 'a')
    data.close()
    arrayLenght = number * 2
    elements = random.randint(2, number * 2)
    array = CreateRandomList(elements, arrayLenght)
    with open('file.txt', 'w') as data:
        for i in range(elements):
            data.write(f'{array[i]}\n')

def ExtractPositionsFromFileTxt():
    array = []
    i = 0
    path = 'file.txt'
    data = open(path, 'r')
    for line in data:
        array.append(line)
        array[i] = array[i].replace('\n', '')
        i += 1
    data.close()
    array = [int(item) for item in array]
    array.sort()
    return array

def MultiplicationStoredPostions(numbers, positions):
    multiplication = 1
    i = 0
    while i < len(positions) :
        multiplication = multiplication * numbers[positions[i]]
        i += 1
    return multiplication

# Fifth task

def ListShuffling(numbers):
    answer = ''
    ok = False
    while not ok:
        answer = input("Do you want randomize your numbers? Y/N: ")
        if (answer == 'y') or (answer == 'Y') or (answer == 'n') or (answer == 'N'):
            ok = True
        else:
            print("Error. Please use only Y/N to answer. Try again...")
    if (answer == 'n') or (answer == 'N'):
        return numbers
    else:
        arrayLength = len(numbers) - 1
        i = 0
        while i < arrayLength:
            rand = random.randint(0, arrayLength)
            tmp = numbers[i]
            numbers[i] = numbers[rand]
            numbers[rand] = tmp
            i += 1
        print(numbers)
    return numbers

n = InputNumber("Enter any integer number: ")
NumbersFromNegativeNtoN = CreateListFromNegativeNtoN(n)
print(NumbersFromNegativeNtoN)
NumbersFromNegativeNtoN = ListShuffling(NumbersFromNegativeNtoN)
RandomNumbersForFileTxt(n)
positionsFromTxt = ExtractPositionsFromFileTxt()
print(f"Positions that will be multiplicated: {positionsFromTxt}")
print(f"Multiplication of the elements at the specified posistions: {MultiplicationStoredPostions(NumbersFromNegativeNtoN, positionsFromTxt)}")