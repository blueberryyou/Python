x = 1
i = 0
j = 0
for i in range(1, 53):
    for j in range(4, 8):
        x = x * (1 + 0.01)
print("一年后的能力值为{}".format(x))
