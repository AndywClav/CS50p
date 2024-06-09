valueC = input("Expression: ").strip()
calculator = valueC.replace(" ", "")
sum = '+' in calculator
sub = '-' in calculator
multi = '*' in calculator
divis = '/' in calculator
if sum == True:
    print(calculator)
if sub == True:
    print(calculator)
if multi == True:
    print(calculator)
if divis == True:
    print(calculator)
