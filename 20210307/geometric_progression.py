def geometric_progression(first_number, common_ratio, num_nums):
    a = 1
    list_ap = []
    while True:
        list_ap.append(first_number)
        first_number = first_number * common_ratio
        a += 1
        if a == num_nums + 1:
            return list_ap
            break

print(geometric_progression(1,5,5))