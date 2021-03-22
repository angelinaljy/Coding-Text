def arith_progress(first_number, com_dif_num, num_nums):
    list_ap = []
    a = first_number
    for num in range(0, num_nums):
        list_ap.append(a)
        a += com_dif_num
    return list_ap


print(arith_progress(1, 5, 5))
