def del_duplicate_element():
    the_string = input("Please write down any string here.")
    the_new_string = ""
    for the_element in the_string:
        if the_element in the_new_string:
            pass
        else:
            the_new_string += the_element

    print(the_new_string)


if __name__ == "__main__":
    del_duplicate_element()