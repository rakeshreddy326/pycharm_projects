# # Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.
# number1 = 40
# number2 = 30
# product = number1 * number2
# addition = number1 + number2
# if product <= 1000:
#     print(product)
# else:
#     print(addition)
#
# prev_num = 0
# for x in range(1, 11):
#     x_sum = prev_num + x
#     print("current num: ", x, "previous num: ", prev_num, "sum: " )
#     prev_num = x
#
#
word = input("pynative")
size = len(word)
for i in range(0, size - 1, 2):
    print(word[i])
