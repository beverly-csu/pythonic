operand = ['+', '-', '*', '/', '^', '%']
numbers = []

temp_num = ''
sumup = 0
counter = 0
index = 0

ex = input('Введите пример: ')

for char in ex:
    counter += 1
    if char not in operand:
        temp_num += char
    elif char in operand:
        numbers.append(temp_num)
        numbers.append(char)
        temp_num = ''
    if counter == len(ex):
        numbers.append(temp_num)

for i in range(0, len(numbers)):
    try:
        a = int(numbers[i + 1])
    except:
        a = int(numbers[i])
    if (i == 0):
        sumup += a
    else:
        if isinstance(a, int):
            try:
                if numbers[i] == '+':
                    sumup += a
                elif numbers[i] == '-':
                    sumup -= a
                elif numbers[i] == '*':
                    sumup *= a
                elif numbers[i] == '/':
                    sumup /= a
                elif numbers[i] == '^':
                    sumup = sumup ** a
                elif numbers[i] == '%':
                    sumup = sumup % a
            except IndexError:
                continue

print(f'Ответ: {sumup}')