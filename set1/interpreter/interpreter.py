valueC = input("Expression: ").strip()
calculator = valueC.replace(" ", "")
sum = '+' in calculator
sub = '-' in calculator
multi = '*' in calculator
divis = '/' in calculator

if sum == True:
    sepa = sum.split('+')
    part = sepa
    total = int(part[0]) + int(part[1])
    print(calculator)
elif sub == True:
    print(calculator)
elif multi == True:
    print(calculator)
elif divis == True:
    print(calculator)
