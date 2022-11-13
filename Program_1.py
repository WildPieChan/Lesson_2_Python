def InputNumber(inputText):
    ok = False
    while not ok:
        try:
            number = float(input(f"{inputText}"))
            ok = True
        except ValueError:
            print("Error. Only numbers. Try again...")
    return number

def SumOfNumberDigits(number):
    sum = 0
    for i in str(number):
        if (i != '.') and (i != '-'):
            sum += int(i)
    return sum

n = InputNumber("Enter any number: ")
print(f"Sum of number's digits: {SumOfNumberDigits(n)}")