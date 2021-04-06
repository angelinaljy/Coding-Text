def circle_drop_by3(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        old_list = list(range(1, n+1))
        new_list = old_list[:]

        while True:
            old_list = new_list[:]
            # 找出上一列中需要退出的数的位置数
            index_number = []
            the_drop_list = []
            for num in range(2, len(new_list), 3):
                index_number.append(num)
                the_drop_list.append(new_list[num])
            # print(index_number)

            # 刚才退出位置的数的列表
            # print(the_drop_list)

            # 删除掉刚才找出来的数
            for the_drop_num in the_drop_list:
                new_list.remove(the_drop_num)
            # print(new_list)



            # 重新调整新的一列
            if (len(old_list)-1)- index_number[-1] == 1:

                new_list.insert(0, new_list.pop())
                # print(new_list)
                continue

            if (len(old_list)-1) - index_number[-1] == 2:
                new_list.insert(0, new_list.pop())
                new_list.insert(0, new_list.pop())
                # print(new_list)
                continue

            if len(new_list) == 2:
                if len(new_list) - index_number[-1] == 0:
                    return new_list[1]

                else:
                    return new_list[0]





if __name__ == "__main__":
    print(circle_drop_by3(11))
