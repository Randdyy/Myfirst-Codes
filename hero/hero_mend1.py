map1 = "*#########"
print(map1,"\n* is your hero")
l = list(map1)
while True:
    for j in range(0, len(l)):
        if l[j] == "*":
            i = j
        pass
    user_input = str(input("input f to go forward b to back and q to quit"))
    if user_input == "f":
        l[i], l[i+1] = l[i+1], l[i]
        map2 = ''.join(l)
        print(map2)
        continue
    elif user_input == "b":
        l[i], l[i - 1] = l[i - 1], l[i]
        map2 = ''.join(l)
        print(map2)
        continue
    elif user_input == "q":
        break
    else :
        print("only 'f' 'b' and 'q' ")
        continue
