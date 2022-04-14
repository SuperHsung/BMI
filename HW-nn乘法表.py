n=input("多少數字乘法表：")       # n*n 乘法表

n=int(n)
x=1
while x<=n:
    y=1
    while y<=n:
        print(x,"*",y,"=",str(x*y))
        y=y+1
    x=x+1
