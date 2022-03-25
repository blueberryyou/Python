# 11111111111111
import random

var = "hello python"
print(var.lstrip())  # 方法用于截掉字符串左边的空格或指定字符
print(var.rsplit())  # 使用后跟空格的逗号作为分隔符，将字符串拆分为列表
print(var.strip())  # 删除字符串开头和结尾的空格
print(var.strip().strip("on"))  # 方法删除任何前导（开头的空格）和尾随（结尾的空格）字符（空格是要删除的默认前导字符）。
print(var.strip().strip("h").strip("e"))
one = var.replace("", ",")  # 替换
two = var.replace("hello", "good")
third = var.replace("h", "")
print(one)
print(two)
print(third)
# strip()例题
# txt = ",,,,,rrttgg.....banana....rrr"
# x = txt.strip(",.grt")
# print(x)
#
# <<banana

# 2222222222222222
item = ''
num = ''
password = ''
new = chr(ord(item) + 3)
low = random.choice(num)
upp = random.choice(num).upper()
password += upp + new + low
s1 = "Python"
uppers1 = s1.upper()
print(uppers1)
lowers1 = uppers1.lower()
print(lowers1)
capitalizes1 = s1.capitalize()
print(capitalizes1)
name = "赵钱孙李周吴郑王"
for i in range(len(name)):
    print(name[i])
for index, item in enumerate(name):
    print(index + 1, item)

# 3333333333333333333
name = "玄德出马，左有云长，右有翼德"
count = name.count(name[6])
new = name.find("德", 5)
len(name[0:2])
surname = '赵构钱丽孙周可安李冯赵周同吴钱郑周'
print(surname.count("周"))
print(surname.count("冯", 3))
name = "www.miniaturising.com,www.huawei.com,www.jd.com"
print(name.count("com", 5))
print(name.count("www"))
