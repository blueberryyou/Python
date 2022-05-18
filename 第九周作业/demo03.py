import json
f=open("身份证码值对照表.txt","r",encoding='utf-8')
content=f.read()
content_dict=json.loads(content)    #转换为字典类型
num=str(input("请输入身份证前6位："))
print(content_dict[num])
