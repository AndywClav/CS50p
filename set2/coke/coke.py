coca_cola = 50
posible_value = [25, 10, 5]

while coca_cola > 0:
    print(f'Amount Due: { coca_cola }')
    insert = int(input('Insert Coin: '))
    if insert in posible_value:
        change_own = coca_cola - insert
