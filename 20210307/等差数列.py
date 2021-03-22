def arith_progress(first_number, last_number, com_dif_num):
    list_ap = []
    number_a = first_number
    while True:
        list_ap.append(number_a)
        number_a += com_dif_num
        if number_a > last_number:
            return list_ap
            break

print(arith_progress(1,10,4))