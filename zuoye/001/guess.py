import random
print("我在一百内想了一个数，你猜猜看啊")
count=0
ran=random.randint(1, 101)
print(ran)
while(1):
    
    
    count+=1
    user_input=input("please input a number,input q to quit")
    try:
        if isinstance(int(user_input),int): 
            if ran < int(user_input) :
                print("大了,请重新猜")
                print("您已经玩了{}次了".format(count))
                continue
            elif ran > int(user_input) :
                print("小了,请重新猜")
                print("您已经玩了{}次了".format(count))
                continue
            elif ran== int(user_input):
                print("恭喜你猜对了")
                print("您一共玩了{}次了".format(count))
                user_input2=input("输入y继续玩").lower().strip()
                if user_input2=="y":
                    count=0
                    ran=random.randint(1,101)
                    continue
                else:
                    break
    except:
        break
