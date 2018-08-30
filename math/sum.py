list = []
sum=0
user_input = int(input("input a number"))
for i in range(1,user_input):
    sum = sum + i
    list.append(i)
    print('1', end='')
    for k in range(1, len(list)):
        print("+", end='')
        print(list[k], end = '')
    print("=", sum)

