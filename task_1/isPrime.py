def isPrime(number):
    primeFactor = False
    if (number == 1):
        return False
    elif (number == 2):
        return True
    elif (number < 0):
        print("Число не соответствует правилу!")
        exit(0)
    for i in range(2, number):
        if (number % i != 0):
            primeFactor = True
        else:
            primeFactor = False
            break
    return primeFactor

number = int(input("Введите число для проверки: "))

if (isPrime(number)):
    print("Число простое!")
else:
    print("Число не простое!")