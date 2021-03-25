def narcissistic_number():
    all_narcis_nums = []
    for num_a in range(0, 10):
        for num_b in range(0, 10):
            for num_c in range(0, 10):
                if num_a or num_b != 0:
                    final_num = num_a * 100 + num_b * 10 + num_c
                    the_num = num_a ** 3 + num_b ** 3 + num_c ** 3
                    if final_num == the_num:
                        all_narcis_nums.append(final_num)

    return all_narcis_nums


print(narcissistic_number())
