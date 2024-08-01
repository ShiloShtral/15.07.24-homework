
n = int(input("give me a number "));

if n > 0:
    for i in range(1 ,n + 1):
        for p in range(1 ,i + 1):
           print(p , end= "")
        print()


    for i in range(n - 1, 0, -1):
        for p in range(1, i + 1):
            print(p, end="")
        print()

