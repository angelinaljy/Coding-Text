# def amount_peach(nums_peach_left, nums_days):
#     for num_day in range(1,nums_days):
#         nums_peach_left = (nums_peach_left + 1) * 2
#     return nums_peach_left
#
#
# print(amount_peach(1, 10))

def amount_peach(n):
    if n == 1:
        return 1
    else:
        return (amount_peach(n - 1) + 1) * 2


print(amount_peach(10))
