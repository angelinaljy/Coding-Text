def geometric_progression(first_number, last_number, common_ratio):
    list_gp = []
    number_a = first_number
    while True:
        list_gp.append(number_a)
        number_a = number_a * common_ratio
        if number_a > last_number:
            return list_gp
            break

print(geometric_progression(1,10,2))