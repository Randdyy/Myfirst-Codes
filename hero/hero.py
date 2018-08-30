import os
print("welcome to 英雄无敌")
dict1 = {'phoenix':'123'}
select = input("input l to login and r to regist!")
flag = True
if select == 'r':
    while True:
        ID = input("请输入您想创建的用户名")
        pas1 = input("输入您的账户密码")
        pas2 = input("确认密码")
        if pas1 == pas2 :
            with open('passwd.db', "a+") as p:
                p.write(ID+':+:'+pas1+'\n')
                print("注册成功")
                break
        else :
            print("两次密码不一致，请重新输入")
            continue

elif select =='l' :
    for k in range(3):
        while flag:
            ID = input("请输入用户名")
            pas = input("请输入密码")
            if not os.path.exists('{}.lock'.format(ID)):
                with open('passwd.db') as p:
                    for line in p:
                        upl = line.split(':+:')
                        print(upl)
                        if ID == upl[0] and pas == upl[1].strip():
                            print("恭喜您登录成功")
                            hero = input('请输入你的英雄昵称')
                            print("hello", hero,"welcome！！！")
                            map1 = "*#########"
                            print(map1, "\n* is your hero")
                            l = list(map1)
                            while True:
                                for j in range(0, len(l)):
                                    if l[j] == "*":
                                        i = j
                                    pass
                                user_input = str(input("input f to go forward b to back and q to quit\n"))
                                if user_input == "f":
                                    l[i], l[i + 1] = l[i + 1], l[i]
                                    map2 = ''.join(l)
                                    print(map2)
                                    continue
                                elif user_input == "b":
                                    l[i], l[i - 1] = l[i - 1], l[i]
                                    map2 = ''.join(l)
                                    print(map2)
                                    continue
                                elif user_input == "q":
                                    flag = False
                                    break
                                else:
                                    print("only 'f' 'b' and 'q' ")
                                    continue
                            break
                        else:
                            print("用户名或密码不正确")
            else:
                print('user{} is locked!'.format(ID))
                break
    else:
        with open('{}.lock'.format(ID), 'w') as f:
            pass
else:
    pass 
