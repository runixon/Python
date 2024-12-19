def fizz_buzz(n):
    for number in range(1, n + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


n = int(input("Введите число n: "))
fizz_buzz(n)
