# a = 1
# b = 1
#
# while True:
#     print("\t")
#     for a in range(1,b+1):
#         print(f"{a}*{b}={a*b}", end=" ")
#     if b == 9:
#         break
#     else:
#         b += 1
#         continue

for b in range(1,10):
    for a in range(1,b+1):
        print(f"{a}*{b}={a*b}", end=" ")
    if b < 9:
        print()
    #print(end="\n" if b<9 else "")

