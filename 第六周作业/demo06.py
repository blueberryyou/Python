dt={}
i=1
while i<=5:
    word=input()
    if word in dt.keys():     #取字典的键的序列
        dt[word]+=1
    else:
        dt[word]=1
    i+=1
result=[]
for x in dt.items():            #取字典的元素的序列，可用于遍历字典
    result.append(x)
result.sort(key=lambda x:(-x[1],x[0]))    #先按照-x[1]的升序，再按照x[2]的升序
for x in result:
    print(x[1],x[0])