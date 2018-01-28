# -*-coding=utf_8 -*-
import datetime

def input_bill():
    with open("company_money.txt") as f:
        company_money = f.readlines()
        company_money = [int(i) for i in company_money[0].split()]
        if not company_money:
            company_money = [0,0,0]
    with open("money_flow.txt","r",encoding = "utf-8") as f:
        money_flow = [i.split() for i in f.readlines()]
        if not money_flow:
            money_flow = [["交易对象","收入","支出","应收账款","应付账款","交易时间"]]
    print("\n记账模式")
    while True:
        try:
            duel_object = str(input("交易对象"))
            money_in = int(input("收入/万"))
            money_out = int(input("支出/万"))
            bill_in = int(input("应收账款/万"))
            bill_out = int(input("应出账款/万"))
        except:
            print("输入错误，请重新输入")
        else:
            break
    if len(money_flow) == 1:
        money_flow.append([duel_object,str(money_in) + "万",str(money_out) + "万",str(bill_in) + "万",str(bill_out) + "万",datetime.date.today()])
    else:
        money_flow.insert(1,[duel_object,str(money_in) + "万",str(money_out) + "万",str(bill_in) + "万",str(bill_out) + "万",datetime.date.today()])
    company_money[0] += money_in - money_out
    company_money[1] += bill_out - bill_in
    company_money[2] = company_money[0] - company_money[1]
    print("\n交易已记录\n当前资产状况\n最新资产：%d万\n最新负债：%d万\n最新净资产：%d万"%(company_money[0],company_money[1],company_money[2]))
    with open("company_money.txt","w") as f:
        f.writelines(" ".join([str(i) for i in company_money]))
    with open("money_flow.txt","w",encoding = "utf-8") as f:
        for i in money_flow:
            f.writelines(" ".join([str(j) for j in i]) + "\n")

def search_recently():
    with open("money_flow.txt","r",encoding = "utf-8") as f:
        money_flow_recently = [i.split() for i in f.readlines()]
        if len(money_flow_recently) <= 11:
            for i in money_flow_recently:
                print(" ".join(i))
        else:
            for i in range(11):
                print(" ".join(money_flow_recently[i]))

def search_company(company_name):
    with open("money_flow.txt","r",encoding = "utf-8") as f:
        money_flow = [i.split() for i in f.readlines()]
        if not money_flow:
            money_flow = [["交易对象","收入","支出","应收账款","应付账款","交易时间"]]
        company_flow = []
        for i in money_flow:
            if i[0] == company_name:
                company_flow.append([j for j in i[1:]])
        print("与%s共有%d笔交易"%(company_name,len(company_flow)))
        for i in company_flow:
            print("交易时间：%s\n收入：%s\n支出：%s\n应收账款：%s\n应出账款：%s\n"%(i[-1],i[0],i[1],i[2],i[3]))

def search_company_money():
    with open("company_money.txt") as f:
        company_money = f.readlines()
        company_money = [i for i in company_money[0].split()]
        if not company_money:
            company_money = ["0","0","0"]
    with open("money_flow.txt","r",encoding = "utf-8") as f:
        money_flow = [i.split() for i in f.readlines()]
        if not money_flow:
            money_flow = [["交易对象","收入","支出","应收账款","应付账款","交易时间"]]
    print("最新资产：%s万\n最新负债：%s万\n最新净资产：%s万"%(company_money[0],company_money[1],company_money[2]))
    if len(money_flow) == 1:
        print("最后更新时间：还没有交易记录！")
    else:
        print("最后更新时间：%s"%money_flow[1][-1])

while True:
    try:
        print("1.查账；2.记账；3.退出")
        mode = int(input("请选择服务："))
    except:
        print("输入有误，请重新输入a")
        continue
    else:
        if mode == 1:
            while True:
                try:
                    print("\n查账模式\n1.查询最近十笔交易记录\n2.查询与某公司交易往来\n3.查询最近资产负债情况")
                    mode_search = int(input("请选择服务："))
                except:
                    print("输入有误，请重新输入b")
                    continue
                else:
                    if mode_search == 1:
                        search_recently()
                    elif mode_search == 2:
                        search_company(str(input("\n请输入公司名：")))
                    elif mode_search == 3:
                        search_company_money()
                    else:
                        print("输入有误，请重新输入c")
                        continue
                    break
        elif mode == 2:
            input_bill()
        elif mode == 3:
            break
        else:
            print("输入有误，请重新输入d")
            continue