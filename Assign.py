a=int(input())
b=int(input())
c=int(input())
if (a+b+c)==180:
    print(" valid triangle")
else:
    print("invalid triangle ")

#
a=int(input())
if a>=40:
    print("pass")
else:
    print("fail")

#
a=int(input())
b=int(input())
c=int(input())                    
if a>=b and a>=c:
    print(a,"maximum")
elif b>=a and b>=c:
    print(b,"maximum")
else:
    print(c,"maximum")
    

#
temp=int(input())
if temp>35:
    print("hot")
elif 20<temp<=35:
    print("normal")
elif temp<20:
    print("cold")
else:
    print("invalid")

