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
        the_number = number(line-1, order-1) + number(line-1, order)
        return the_number


def yanghuis_triangle(n):
    for line in range(1,n+1):
        print(" " * (n - line), end="")

        for order in range(1,line+1):
            if order != line:
                print(str(number(line, order)), end=" ")
            else:
                print(str(number(line, order)))


            # if line_n == 1:
            #     print("1 ", end="")
            #
            # else:
            #     if num_m == 1:
            #         print("1 ", end="")
            #     else:
            #         num_a = fac(line_n-1)
            #         num_b = fac(line_n-num_m-2)
            #         num_c = fac(num_m-1)
            #         the_number = num_a//(num_b*num_c)
            #         print(f"{the_number} ", end="")



if __name__=="__main__":

    yanghuis_triangle(10)

