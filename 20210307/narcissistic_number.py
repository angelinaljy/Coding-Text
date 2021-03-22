def narcissistic_number():
    list_a = [1,4,5,6,9]
    all_narcis_nums = []
    the_num = 0
    for num_a in list_a:
        for num_b in list_a:
            for num_c in list_a:
                the_num = num_a * 100 + num_b * 10 + num_c * 1
                all_narcis_nums.append(the_num)

    return all_narcis_nums


print(narcissistic_number())