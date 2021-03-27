# def fac(n):
#     if n == 1 or n < 0:
#         return 1
#     else:
#         return n*fac(n-1)

# 方法二：使用递归
# def number(line, order):
#     if order == 1:
#         the_number = 1
#         return the_number
#     elif order == line:
#         the_number = 1
#         return the_number
#     else:
#         the_number = number(line-1, order-1) + number(line-1, order)
#         return the_number
#
#
# def yanghuis_triangle(n):
#     number_width = (len(str(number(n, n//2))))
#
#     for line in range(1,n+1):
#         print(" " * number_width * (n - line), end="")
#
#         for order in range(1,line+1):
#             if order != line:
#                 print(f"{number(line, order):^{number_width}}", end=" "*(number_width))
#             else:
#                 print(f"{number(line, order):^{number_width}}")


# 第三种方法：
def yanghuis_triangle(n):
    number_width = 5

    the_old_list = []
    for line in range(1, n + 1):
        print(" " * number_width * (n - line), end="")

        the_new_list = []
        for order in range(0, line):
            if line == 1:
                the_new_list.append(1)
                print(f"{the_new_list[order]:^{number_width}}")
            elif order == 0:
                the_new_list.append(1)
                print(f"{the_new_list[order]:^{number_width}}", end=" " * number_width)
            elif order < line - 1:
                the_number = the_old_list[order - 1] + the_old_list[order]
                the_new_list.append(the_number)
                print(f"{the_new_list[order]:^{number_width}}", end=" " * number_width)
            elif order == line - 1:
                the_new_list.append(1)
                print(f"{the_new_list[order]:^{number_width}}")
        the_old_list = the_new_list


if __name__ == "__main__":
    yanghuis_triangle(15)
