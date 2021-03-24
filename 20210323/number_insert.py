# 有一个已经从小到大排好序的列表。现输入一个数，要求按原来的规律将它插入列表中。（不可以使用sort方法）

def number_insert(list_numbers, number_inputted):
    if number_inputted < list_numbers[0]:
        list_numbers.insert(0, number_inputted)
        return list_numbers
    elif number_inputted >= list_numbers[-1]:
        list_numbers.append(number_inputted)
        return list_numbers
    else:
        for num in range(0, len(list_numbers)):
            if number_inputted >= list_numbers[num] and number_inputted < list_numbers[num + 1]:
                list_numbers.insert(num +1, number_inputted)
                return list_numbers

the_list = [1, 3, 5, 9, 14, 28, 59, 99, 140]
print(number_insert(the_list, 150))