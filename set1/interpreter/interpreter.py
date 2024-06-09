valueC = input("Expression: ").strip()
calculator = valueC.replace(" ", "")
sum = '+' in calculator
sub = '-' in calculator
multi = '*' in calculator
divis = '/' in calculator

if sum == True:
    sepa = calculator.split('+')
    part = sepa
    total = float(part[0]) + float(part[1])
    print(total)
elif sub == True:
    sepa = calculator.split('-')
    part = sepa
    total = float(part[0]) - float(part[1])
    print(total)
elif multi == True:
    sepa = calculator.split('*')
    part = sepa
    total = float(part[0]) * float(part[1])
    print(total)
elif divis == True:
    sepa = calculator.split('/')
    part = sepa
    total = float(part[0]) / float(part[1])
    print(total)
