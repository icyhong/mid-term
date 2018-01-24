# -*- coding=utf8 -*-
import random
def data_in(name):
    with open("player_data.txt") as f:
        player_data = {}
        for i in f.readlines():
            d = i.split()
            player_data[d[0]] = [int(k) for k in d[1:]]
        if not player_data.get(name):
            player_data[name] = [0,0,0]
        else:
            print("%s,欢迎回来"%name)
        return player_data


def guess():
    global my_data
    while True:
        num = random.randint(1,100)
        times = 0
        while True:
            print("第%d次"%(times + 1))
            awnser = input("请输入一个1-100的整数：")
            while True:
                try:
                    int(awnser) >= 1 and int(awnser)<= 100
                except:
                    awnser = input("请输入一个1-100的整数：")
                else:
                    break
            if int(awnser) < num:
                print("太小了！")
                times += 1
            if int(awnser) > num:
                print("太大了！")
                times += 1
            if int(awnser) == num:
                print("猜对了！")
                times += 1
                my_data[1] = my_data[1] + times
                if times < my_data[2] or my_data[2] == 0:
                    my_data[2] = times
                break
        my_data[0] += 1
        print("你猜中答案一共用了%d轮\n你一共玩了%d次游戏，平均%.2f次猜中答案\n你的最好成绩是%d次"%(times,my_data[0],my_data[1]/my_data[0],my_data[2]))
        con = input("输入c继续游戏，否则退出游戏")
        if str(con) != "c":
            break

player_name = input("请输入你的名字")
player_data = data_in(player_name)
my_data = player_data.get(player_name)
guess()
player_data[player_name] = my_data
with open("player_data.txt","w") as f:
    for i in player_data:
        f.writelines(i + " " + " ".join([str(k) for k in player_data[i]]) + "\n")