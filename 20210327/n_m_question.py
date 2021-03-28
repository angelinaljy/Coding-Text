def n_m_question(the_list_input, m):

    n = len(the_list_input)

    the_index_list = list(range(0, n-m))
    the_index_list.sort(reverse=True)
    for num in the_index_list:
        the_number = the_list_input.pop(num)
        the_list_input.insert(num + m, the_number)

        print(the_list_input)


list_new_number = [1, 2, 3, 4, 5, 6, 7]
n_m_question(list_new_number, 2)

