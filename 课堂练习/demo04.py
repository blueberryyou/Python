year=int(input())
if (year-1949)%10==0:
    print("建国{}周年".format(int((year-1949))))
if (year - 1921) % 10 == 0:
    print("建党{}周年".format(int((year - 1921))))
if year%4==0 and year%100==0 or year%400==0:
    print("闰年")

