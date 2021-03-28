#文本文件中存储了一个较长的字符串，从控制台输入一个较短的字符串，统计输入的字符串在文件中出现的次数，并打印出出现的次数及对应的索引位置；
zen_python = "Beautiful is better than ugly Explicit is better than implicit"

def count_n_index():
    short_input = input("Please write down the short content here.")

    count_numBer = 0
    index_list = []
    the_list_zen = zen_python[:]
    the_list_zen = the_list_zen.split(" ")
    for word in the_list_zen:
        if short_input.lower() == word.lower():
            count_numBer += 1

    for index_num in range(0, len(the_list_zen)):
        if the_list_zen[index_num].lower() == short_input.lower():
            index_list.append(index_num)

    print(count_numBer)
    print(index_list)


if __name__ == "__main__":
    count_n_index()


