x1 = 1
y1 = 1
z1 = 1
x2 = 1
y2 = 1
z2 = 1
for i in range(8):
    x1 = x1 * (1 + 0.01)
print("一周后进步了{}".format(x1 - 1))
for i in range(31):
    y1 = y1 * (1 + 0.01)
print("一月后进步了{}".format(y1 - 1))
for i in range(366):
    z1 = z1 * (1 + 0.01)
print("一年后进步了{}".format(z1 - 1))
for i in range(8):
    x2 = x2 * (1 - 0.01)
print("一周后退步了{}".format(1 - x2))
for i in range(31):
    y2 = y2 * (1 - 0.01)
print("一月后退步了{}".format(1 - y2))
for i in range(366):
    z2 = z2 * (1 - 0.01)
print("一年后退步了{}".format(1 - z2))
