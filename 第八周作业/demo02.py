import jieba
excludes={"一个","那里","怎么","我们","不知","甚么","只见"}
txt=open("西游记.txt","r",encoding="utf-8").read()
words=jieba.lcut(txt)
counts={}
for word in words:
    if len(word)==1:
        continue
    elif word == "行者" or word == "大圣" or word == "老孙":
        rword = "大圣"
    elif word == "师傅" or word == "三藏" or word == "唐僧":
        rword = "唐僧"
    else:
        rword = word
    counts[rword] = counts.get(rword, 0) + 1
for word in excludes:
    del (counts[word])
items=list(counts.items())
items.sort(key=lambda  x:x[1],reverse=True)
for i in range(15):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))