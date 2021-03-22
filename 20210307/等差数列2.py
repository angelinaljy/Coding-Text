def arith_progress(first_number, com_dif_num, num_nums):
    a = 1
    list_ap = []
    while True:
        list_ap.append(first_number)
        first_number += com_dif_num
        a += 1
        if a == num_nums + 1:
            return list_ap
            break

    return list_ap

print(arith_progress(1,5,5))
