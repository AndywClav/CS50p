camelCase = input('camelCase: ').strip()
snake_case = ""

for char in camelCase:
    if char.isupper():
        snake_case += "_" + char.lower()
    else:
        snake_case += char

# Asegurarse de que la cadena no comience con un guion bajo
if snake_case.startswith('_'):
    snake_case = snake_case[1:]

print(f'snake_case: {snake_case}')
