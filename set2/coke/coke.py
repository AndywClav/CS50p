coca_cola = 50
posible_value = [25, 10, 5]
print(f'Amount Due: { coca_cola }')

while coca_cola > 0:
    insert = int(input('Insert Coin: '))
    if insert in posible_value:
        change_own = coca_cola - insert
        coca_cola = change_own

    print(f'Amount Due: { coca_cola }')

print(f'Change Owed: { abs(change_own) }')

