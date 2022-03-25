import random

surname = '赵，钱，孙，李，周，吴'
second = '中，万，斯，近，元，伟'
third = '隆，智，渝，顺，乐，天'
a1 = random.randrange(0, 12, 2)
b1 = random.randrange(0, 12, 2)
c1 = random.randrange(0, 12, 2)
a2 = random.randrange(0, 12, 2)
b2 = random.randrange(0, 12, 2)
name1 = surname[a1]+second[b1]+third[c1]
name2 = surname[a2]+second[b2]
print(name1)
print(name2)



