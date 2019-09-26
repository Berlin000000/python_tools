import base64
from collections import defaultdict
import json
import qrcode

print("输入您想做的事情，实现字符串加密请输入1，实现密文解密请输入2，反转字典请输入3，生成二维码请输入4，退出程序请输入#")
alt=input()

while alt!='#':

    if(alt=='1'):
        try:
            print("input:")
            str=input()
            str=str.encode('utf-8')
            bs64=base64.b64encode(str)
        except:
            print("请输入字符串")
        print("加密结果是")
        print(bs64)

    elif (alt == '2'):
        try:
            print("input:")
            secret=input()
            debs64 = base64.b64decode(secret)
        except:
            print("请输入密文")
        print("解密结果是")
        print(debs64)

    elif (alt=='3'):
        try:
            mydict = {}
            print("输入键值对,输入$表示结束")
            key=input()
            value=input()
            mydict[key]=value
            while(key!='$'):
                key=input()
                if key == "$":
                    break
                value=input()
                mydict[key]=value
        except:
            print("请输入键值对，以$结束")

        j = json.dumps(mydict)
        print(j)
        print(type(j))
        reversed_dict = defaultdict(list)
        for key, value in mydict.items():
            reversed_dict[value].append(key)
        print(reversed_dict)

    elif (alt=='4'):
        try:
            f = open("lalala.txt")
            line = f.readline()
            while line:
                line = f.readline()
            f.close()
        except IOError:
            print("文件读写有误")

        img = qrcode.make(line)
        img.save('test.png')
