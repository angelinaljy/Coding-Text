# # 从键盘输入一个字符串，判断这个字符串是不是回文，回文是指从左到右读与从右到左读是一样的，如：123454321就是一个回文
#
def palindromic_judge():
    the_number = input("Please write a number.")

    the_number_list = list(the_number)
    the_new_list = the_number_list[:]
    the_new_list.reverse()

    if the_new_list == the_number_list:
        print("It's a palindromic.")
    else:
        print("It's not.")

if __name__=="__main__":
    palindromic_judge()