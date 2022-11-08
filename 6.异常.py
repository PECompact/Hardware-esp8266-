'''import traceback#异常的库
while True:
    try:
        n1 = int(input("请输入第1个数"))
        n2 = int(input("请输入第2个数"))
        print("{0}/{1}={2}".format(n1,n2,n1/n2))
    except Exception as e:
        print("出现异常")
        print(e)#打印异常的基本信息
        print(repr(e))#打印异常的类型和基本信息
        print(traceback.format_exc())#打印异常的详细信息'''


number = 1
Test_Scores = []
q = 0
uu=0
report = "成绩单："
_report = 0


while True:
    try:
        Number_of_persons = int(input("人数"))
        p=Number_of_persons
        for q in range(Number_of_persons):
            e = "第",number,"个人"
            individual_results = int(input(e))
            Test_Scores.append(individual_results)
            _report=(Test_Scores[q])
            w = str(Test_Scores[q])
            q=q+1
            report = report+w+"\t"
            number = number+1
            uu=uu+_report
        uu=uu/p
        print(report)
        print("平均分为：",_report)
    except Exception as e:
        print("出现异常")
        print(repr(e))#打印异常的类型和基本信息
