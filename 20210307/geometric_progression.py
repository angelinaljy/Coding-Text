def geometric_progression(first_number, common_ratio, num_nums):
    list_ap = []
    a = first_number
    for num in range(0, num_nums):
        list_ap.append(a)
        a = a * common_ratio
    return list_ap


print(geometric_progression(1, 5, 5))
