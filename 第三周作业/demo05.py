# 在原题稍加变动，判断是否是建党、建国整十年或者十年的倍数
year=int(input())
if (year-1949)%10==0:
    print("建国{}周年".format(int((year-1949))))
else :
    print("{}不是建国周年".format(int(year)))
if (year - 1921) % 10 == 0:
    print("建党{}周年".format(int((year - 1921))))
else :
    print("{}不是建党周年".format(int(year)))
if year%4==0 and year%100==0 or year%400==0:
    print("闰年")
else :
    print("{}不是闰年".format(int(year)))

