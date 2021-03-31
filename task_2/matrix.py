while True:
    rang = input("Введите ранг матрицы: ")
    try:
        rang = int(rang)
        if rang == 0:
            print("\033[31mНе существует 0-ранговой матрицы\033[0m")
        else:
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

for iteration in range(rang // 2):
    for i in range(rang - cell):
        matrix[iteration][i + iteration] = counter
        counter += 1
    for i in range(iteration + 1, rang - iteration):
        matrix[i][-iteration - 1] = counter
        counter += 1
    for i in range(iteration + 1, rang - iteration):
        matrix[-iteration - 1][-i - 1] = counter
        counter += 1
    for i in range(iteration + 1, rang - (iteration + 1)):
        matrix[-i - 1][iteration] = counter
        counter += 1
    cell += 2
    print('Iteration:', iteration + 1)
    for i in range(rang):
        print(matrix[i])
    print("-" * 30)

for i in range(0, rang):
    string = ''
    for j in range(0, rang):
        string = string + str(matrix[i][j]) + '\t'
    print(string)