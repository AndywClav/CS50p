def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d.remove('$', '')
    dollars = float(d)
    dollars = round(dollars, 2)
    return dollars



def percent_to_float(p):
    p.remove('%', '')
    percent = 


main()
