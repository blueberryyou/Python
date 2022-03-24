# x=0
# for i in range(0,10):
#     for j in range(0,10):
#         x=60000+40+2+i*1000+j*100
#         if x%57==0 and x%67==0:
#             print(x)

for i in range(60042,69943,100):
    if i % 57 == 0 and i % 67 == 0:
        print(i)