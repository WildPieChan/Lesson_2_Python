def InputNumber(inputText):
    ok = False
    while not ok:
        try:
            number = int(input(f"{inputText}"))
            ok = True
        except ValueError:
            print("Erroe. Only integer numbers. Try again...")
    return number

def SumOfNumbersInTheSequence(number):
    sum = 0
    for i in range(1, number + 1):
        sum += (1 + 1 / i)**i
        print(f"{i}: {sum:.0f}  ", end = ' ')

n = InputNumber("Enter any integer number: ")
SumOfNumbersInTheSequence(n)