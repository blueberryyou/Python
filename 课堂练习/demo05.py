sum1=0
sum2=0
sum3=1

for i in range(1,101):
    sum1+=i
print(sum1)

# for i in range(1,101,2)
for i in range(1,101):
    if i%2!=0:
        sum2+=i
print(sum2)

n=int(input())
for i in range(1,n+1):
    sum3*=i
print(sum3)


