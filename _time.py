import calendar
from datetime import datetime, date, time

#1번
li=[]
def leapyear():
    for i in range(1950,2018):
        li.append(calendar.monthrange(i,2))

    for i in range(len(li)):
        if li[i][1]==29:
            if li[i][0]==0:
                print(i+1950, "월요일")
            elif li[i][0]==1:
                print(i+1950, "화요일")
            elif li[i][0]==2:
                print(i+1950, "수요일")
            elif li[i][0]==3:
                print(i+1950, "목요일")
            elif li[i][0]==4:
                print(i+1950, "금요일")
            elif li[i][0]==5:
                print(i+1950, "토요일")
            else:
                print(i+1950, "일요일")

leapyear()

#2번
def days():
    d=date(2017,12,31)
    d2=date(1950,1,1)
    k=(d-d2).days
    print(k)

days()

#3번
def friday():
    li2=[]
    for i in range(1950,2018):
        for j in range(1,13):
            li2.append(calendar.weekday(i,j,13))

    num=0
    for i in range(len(li2)):
        if li2[i]==4:
            num+=1

    print(num)

friday()



