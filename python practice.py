'''Write a program to swap two variables without using a temporary variable.'''
'''a=int(input("a="))
b=int(input("b="))
#a,b=b,a
a=a+b
b=a-b
a=a-b
print(a,b)

#Write a program to check if a number is positive, negative, or zero.

n=int(input("n="))
if n>0:
    print("n is positive number")
elif n==0:
    print("this number is zero")
else:
    print("it is negative number")



def bignumber(a,b,c):
    if a>=b and a>=c:
        print(a,"is a big")
    elif b>=a and b>=c:
        print(b,"is a big")
    else:
        print(c,"is a big number")
largest=bignumber(22,33,444)
print(largest)

''' 
#Write a program to print numbers from 1 to 10 using a for loop.

'''n=int(input("enter the value n"))
for i in range(1,n+1):
    print(i,end="  ")'''

#Write a program to print the multiplication table of a number using a while loop.
'''
n=1
c=99
while n<=10:
    k=n*c
    print(n,"*",c,'=',k)
    n+=1'''
#Write a program to find the sum of all even numbers between 1 and 100.
k=0
for i in range(1,101):
    if i%2==0:
        
        k=k+i
print("sum of the even numbers",k)
    



