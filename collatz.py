def collatz(number):
    if (number % 2) == 0:
        print(number // 2)
        return number // 2
    else:
        result = 3 * number + 1
        print(result)
        return result

try:
    n = input("Give me a number: ")
except ValueError:
    print('No valid integer! Please enter a number')
while n != 1:
    n = collatz(int(n))
