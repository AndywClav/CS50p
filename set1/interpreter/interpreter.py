valueC = input("Expression: ").strip()
calculator = valueC.replace(" ", "")
array = '+' in calculator
if array == '+':
    print(calculator)
