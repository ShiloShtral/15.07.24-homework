positivenum = 0
negativenum = 0
devidedby7 = 0
zerocount = 0
lastpositive = None
lastnegative = None


for i in range(10):
    num = int(input("Enter A Number"))

    if num == -9999:
        break

    if num > 1000 or num < -1000:
        continue

    if num > 0:
        positivenum += 1
        lastpositive = num

    elif num < 0:
        negativenum += 1
        lastnegative = num

    else:
        zerocount =+ 1

    if num % 7 == 0:
        devidedby7 +=1

else:
    print(f"Positive numbers entered: {positivenum} ")
    print(f"Negative numbers entered: {negativenum}")
    print(f"Devided by 7 numbers entered: {devidedby7}")
    print(f"number of times zero was entered : {zerocount}")
    print(f"the last positive number entered : {lastpositive}")
    print(f"The last negative number entered: {lastnegative}")