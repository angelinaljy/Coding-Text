# def fac(n):
#     if n == 1 or n < 0:
#         return 1
#     else:
#         return n*fac(n-1)

def number(line, order):
    if order == 1:
        the_number = 1
        return the_number
    elif order == line:
        the_number = 1
        return the_number
    else:
        the_number = number(line - 1, order - 1) + number(line - 1, order)
        return the_number


def yanghuis_triangle(n):
    number_width = (len(str(number(n, n // 2))))

    for line in range(1, n + 1):
        print(" " * number_width * (n - line), end="")

        for order in range(1, line + 1):
            if order != line:
                print(f"{number(line, order):^{number_width}}", end=" " * (number_width))
            else:
                print(f"{number(line, order):^{number_width}}")


if __name__ == "__main__":
    yanghuis_triangle(15)
