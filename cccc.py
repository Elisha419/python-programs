a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
#a,b,c = input('enter no').split(',')

if (a>b) and (a>c):
    temp=a
elif (b>a) and (b>c):
    temp=b
else:
    temp=c
print("The greatest number is",temp)



