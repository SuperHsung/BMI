"""
作品：剪刀石頭布
作者：許超雄
"""
## 方法一
A=input("A玩家出： 0剪刀 1石頭 2布")
B=input("B玩家出： 0剪刀 1石頭 2布")
A=int(A)
B=int(B)

if (A>=0 and A<=2) and  (B>=0 and B<=2):
    if (A==0 and B==2) or (A == 1 and B == 0) or (A == 2 and B == 1):
        print("A 獲勝")
    elif (A==0 and B==1) or (A == 1 and B == 2) or (A == 2 and B == 0):
        print("B 獲勝")
    else:
        print(("平手"))


###  方法二
a=int(input("1剪刀 2石頭 3布 小明選手出："))
b=int(input("1剪刀 2石頭 3布 小三選手出："))
if   a<1 or a>3 or b<1 or b>3:
       print("輸入錯誤")
       exit()
elif a==b:
       print("雙方平手")

elif  a==1 and b==3 or a==2 and b==1 or a==3 and b==2:
       print("小明win")
else:
       print("小三win")
