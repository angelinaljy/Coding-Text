a = 1
b = 1

while True:
    print("\t")
    for a in range(1,b+1):
        print(str(a) + "*" + str(b) + "=" + str(a*b), end=" ")
    if b == 9:
        break
    else:
        b += 1
        continue

