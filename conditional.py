#

person=input("enter the name")
age=int(input("enter the age"))
if age >= 18:
    print("Eligible")
else:
    print("Not eligible")


#
num=int(input("enter the number"))
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero")


#
n=int(input("enter the num"))
if n % 2==0:
    print("even")
else:
    print("odd")

# %%programme3
a=int(input("enter num"))
b=int(input("num"))
if a>b:
    print("a is greater")
elif b>a:
    print("b is greater")
else:
    print("equal")


#
a=int(input())
if a%5==0 and a%11==0:
    print("divisible")
else:
    print("not divisible")

#
year=int(input())
if year%4==0 and year%100 !=0 or year%400==0:
    print("leap year")
else:
    print("not leap year")

#
ch=input()
if 'A' <= ch <='Z':
    print("uppercase")
elif 'a'<= ch <='z':
    print("lowercase")
    



