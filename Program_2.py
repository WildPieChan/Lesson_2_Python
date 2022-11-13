def InputNumbers(inputText):
    ok = False
    while not ok:
        try:
            number = int(input(f"{inputText}"))
            ok = True
        except ValueError:
            print("Error. Only integer number. Try again...")
    return number

def MultiplicationFromOneToN(number):
    multiplication = 1
    for i in range (1, n + 1):
        multiplication *= i
        print(multiplication, end = ' ')

n = InputNumbers("Enter any integer number: ")
MultiplicationFromOneToN(n)