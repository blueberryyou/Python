x = 1
print("100以内符合黄蓉所说的数有：")
while x <= 100:
    if x % 3 == 2 and x % 5 == 3 and x % 7 == 2:
        print(x)
    x = x+1
