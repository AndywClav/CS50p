camelCase = input('camelCase: ').strip()
for i in camelCase:
    if i == i.upper():
        print(f'snake_case: {camelCase}')
    elif i == i:
        print(f'snake_case: {camelCase}')

