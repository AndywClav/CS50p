camelCase = input('camelCase: ').strip()
snake_case = ""

for char in camelCase:
    if char.isupper():
        snake_case += "_" + char.lower()
    else:
        snake_case += char

        
if snake_case.startswith('_'):
    snake_case = snake_case[1:]

print(f'snake_case: {snake_case}')
