# def circle_drop_by3(n):
n= 10
old_list = list(range(1, n+1))
new_list = old_list[:]

print(new_list)

# while True:
# 找出上一列中需要退出的数的位置数

index_number = []
the_drop_list = []
for num in range(2, len(new_list), 3):
    index_number.append(num)
    the_drop_list.append(new_list[num])
print(index_number)
# 刚才退出位置的数的列表
print(the_drop_list)


# 删除掉刚才找出来的数
for the_drop_num in the_drop_list:
    new_list.remove(the_drop_num)
print(new_list)


# 重新调整新的一列
if (len(old_list)-1) - num == 1:
    the_number_changed = new_list.pop()
    new_list.insert(0, the_number_changed)
    print(new_list)

if (len(old_list)-1) - num == 2:
    the_number_changed = new_list.pop()
    new_list.insert(0, the_number_changed)
    the_number_changed = new_list.pop()
    new_list.insert(0, the_number_changed)



old_list = new_list
print(old_list)

# if __name__ == "__main__":
#     circle_drop_by3(10)
