while True:
    rang = input("Введите ранг матрицы: ")
    try:
        rang = int(rang)
        break
    except ValueError:
        print("\033[31mНеверное значение ранга матрицы\033[0m")

matrix = [[0] * rang for i in range(0, rang)]
counter = 1
cell = 0

if rang % 2 == 0:
    matrix[rang // 2][rang // 2 - 1] = rang ** 2
else:
    matrix[rang // 2][rang // 2] = rang ** 2

for element in range(rang // 2):
    for i in range(rang - cell):
        matrix[element][i + element] = counter
        counter += 1
    for i in range(element + 1, rang - element):
        matrix[i][-element - 1] = counter
        counter += 1
    for i in range(element + 1, rang - element):
        matrix[-element - 1][-i - 1] = counter
        counter += 1
    for i in range(element + 1, rang - (element + 1)):
        matrix[-i - 1][element] = counter
        counter += 1
    cell += 2

for i in range(0, rang):
    string = ''
    for j in range(0, rang):
        string = string + str(matrix[i][j]) + '\t'
    print(string)