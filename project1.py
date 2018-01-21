#-*- coding:utf-8 -*-
def statis():
    with open("report.txt","r",encoding = "gbk") as f:
        score = []
        for i in f.readlines():
            score.append(i.split())
        sum = 0
        for i in score:
            sum = 0
            for j in i:
                if i.index(j) != 0:
                    sum += int(j)
            i.append(str(sum))
            ave = sum/(len(i)-2)
            i.append("%.2f"%ave)
        print(sum)
        print(score)
        score.sort(key = lambda s:int(s[-2]),reverse = True)
        sum_per = ["平均"]
        for i in range(len(score[1])-1):
            a = 0
            for j in range(len(score)-1):
                a += float(score[j+1][i+1])
            sum_per.append("%.2f"%(a/(len(score)-1)))
        score.insert(0,sum_per)
        k = 0
        for i in score:
            i.insert(0,str(k))
            k += 1
        score.insert(0,["名次","姓名","语文","数学","英语","物理","化学","生物","政治","历史","地理","总分","平均分"])
        return score
with open("statis.txt","w",encoding = "utf-8") as f:
    for i in statis():
        f.writelines(" ".join(i) + "\n")