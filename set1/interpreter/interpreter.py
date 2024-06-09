valueC = input("Expression: ").strip()
calculator = valueC.replace(" ", "")
sum = '+' in calculator
sub = '-' in calculator
multi = '*' in calculator
divis = '/' in calculator

if sum == True:
    print(calculator)
elif sub == True:
    print(calculator)
elif multi == True:
    print(calculator)
elif divis == True:
    print(calculator)
