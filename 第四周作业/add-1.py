var = "hello python"
print(var.lstrip())  # 方法用于截掉字符串左边的空格或指定字符
print(var.rsplit())  # 使用后跟空格的逗号作为分隔符，将字符串拆分为列表
print(var.strip())  # 删除字符串开头和结尾的空格
print(var.strip().strip("on")) # 方法删除任何前导（开头的空格）和尾随（结尾的空格）字符（空格是要删除的默认前导字符）。
print(var.strip().strip("h").strip("e"))
one = var.replace("", ",")  # 替换
two = var.replace("hello", "good")
third = var.replace("h", "")
print(one)
print(two)
print(third)

# strip()
# txt = ",,,,,rrttgg.....banana....rrr"
# x = txt.strip(",.grt")
# print(x)
#
# <<banana
