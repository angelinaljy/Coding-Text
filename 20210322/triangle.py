# def triangle(n):
# for num_a in range(1,n+1):
#     print(" "*(n - num_a), end="")
#     print("* "*(num_a-1) + "*")


def triangle(n):
    for num_a in range(1, n + 1):
        print(" " * (n - num_a), end="")
        for num_b in range(1, num_a):
            print("* ", end="")
        print("*")


if __name__ == "__main__":
    triangle(5)
    triangle(10)
