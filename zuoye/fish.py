import random as r
import time
legal_x = [0, 9]
legal_y = [0, 9]

class SeaFood:
    def __init__(self):
        self.x = r.randint(legal_x[0], legal_x[1])
        self.y = r.randint(legal_y[0], legal_y[1])
        #定义初始位置
    def move(self):
        self.new_x = self.x + r.choice([-1,1,-2,2])
        self.new_y = self.y + r.choice([-1,1,-2,2])
        #每次可以上下左右走一格或者两格
        if self.new_x < legal_x[0]:
            self.x = legal_x[0]
            #横坐标是否超过左边界
        elif self.new_x > legal_x[1]:
            self.x = legal_x[1]
        else:
            self.x = self.new_x
            #把移动后的位置传递给当前位置

        if self.new_y < legal_y[0]:
            self.y = legal_y[0]
        elif self.new_y > legal_y[1]:
            self.y = legal_y[1]
            #判断纵坐标
        else:
            self.y = self.new_y
        return(self.x, self.y)


class Turtle(SeaFood):
    def __init__(self):
        self.power = 100
        self.x = r.randint(legal_x[0], legal_x[1])
        self.y = r.randint(legal_y[0], legal_y[1])
        #定义初始位置
    def Hpdown(self):
        self.power -=1

    def eat(self):
        self.power +=20
        if self.power > 100:
            self.power = 100


class Fish(SeaFood):
    def eaten(self):
        pass





turtle = Turtle()
fishlis = []
for i in range(2):
    new_fish = Fish()
    fishlis.append(new_fish)

while True:
    time.sleep(0.5)
    map1 = [['#','#','#','#','#','#','#','#','#','#'],
            ['#','#','#','#','#','#','#','#','#','#'],
            ['#','#','#','#','#','#','#','#','#','#'],
            ['#','#','#','#','#','#','#','#','#','#'],
            ['#','#','#','#','#','#','#','#','#','#'],
            ['#','#','#','#','#','#','#','#','#','#'],
            ['#','#','#','#','#','#','#','#','#','#'],
            ['#','#','#','#','#','#','#','#','#','#'],
            ['#','#','#','#','#','#','#','#','#','#'],
            ['#','#','#','#','#','#','#','#','#','#']]

    if not len(fishlis):
        print('fish is done')
        break
    if not turtle.power:
        print("turtle is done")
        break
    pos = turtle.move()
    turtle.Hpdown()
    map1[turtle.x][turtle.y]  = "T"
    for j in range(0, len(fishlis)):
        map1[fishlis[j].x][fishlis[j].y]= 'F'
    for i in map1:
        print("\r", i)
    print('\r 乌龟爬了一下爬到了{}::{}，还有{}体力'.format(turtle.x,turtle.y,turtle.power))
    for each_fish in fishlis[:]:
        if each_fish.move() ==pos:
            # 鱼被吃
            turtle.eat()
            fishlis.remove(each_fish)
            print('有一条鱼被吃掉了，乌龟体力+10')

