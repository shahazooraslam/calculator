a=int(input("enter a number"))
b=int(input("enter the second value"))
print("1-addition/n 2-substraction/n 3-multiplication/n 4-division/n ")
c=int(input('enter the number'))
if c==1:
    print(a+b)
elif c==2:
    print(a-b)
elif c==3:
    print(a*b)
elif c==4:
    print(a/b)
else:
    print('invalid option')

