map1 = ["*######","#######","#######","#######","#######","#######","#######"]
map2 = []
l = []
for s in map1:
    map2.append(list(s))
    print(s)
print("* is your hero")

try:
    flag = True
    while flag:
        flag = False
        for j in range(0, 7):
            for k in range(0, 7):
                if map2[j][k] == "*":
                    x = j
                    y = k
        else:
            user_input = str(input("f:go forward,b:go back,u:go up,d:go down"))
            if user_input == "f":
                map2[x][y], map2[x][y+1] = map2[x][y+1], map2[x][y]
                for f in map2:
                    print(''.join(f))
                flag = True
                continue
            elif user_input == "b":
                map2[x][y], map2[x][y-1] = map2[x][y-1], map2[x][y]
                for f in map2:
                    print(''.join(f))
                flag = True
                continue
            elif user_input == "d":
                map2[x][y], map2[x+1][y] = map2[x+1][y], map2[x][y]
                for f in map2:
                    print(''.join(f))
                flag = True
                continue
            elif user_input == "u":
                map2[x][y], map2[x-1][y] = map2[x-1][y], map2[x][y]
                for f in map2:
                    print(''.join(f))
                flag = True
                continue
            elif user_input == "q":
                flag = False
                continue
            else :
                print("input again!")
                flag = True
                continue
except:
    print("你出界了")
