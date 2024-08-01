while True:
    n = int(input("Give me a number greater than 0: "))

    if n > 0 and n % 2 != 0:
        break
    else:
        print("The number must be positive and odd.")

for i in range(1, n + 1, 2):
    spaces = (n - i) // 2
    print(" " * spaces + "*" * i)
