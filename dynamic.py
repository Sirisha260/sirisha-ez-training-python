#Fibanocci series in iterative
n=int(input("Enter n: "))
n1=0
n2=1
if (n<=0):
    print(n)
else:
    for i in range(0,n-1):
        n3=n1+n2
        n1=n2
        n2=n3
    print(n2)

#called fast fibanoci algorithm-recursive
def fib(n):
    if n<0:
        print("error")
    elif n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
n=int(input("Enter n: "))
x=fib(n)
print(x)

#Top down memoization code
def fib(n,arr):
    if n==0 or n==1:
        return n
    if arr[n]!=0:
        return arr[n]
    arr[n]=fib(n-1,arr)+fib(n-2,arr)
    return arr[n]
arr=[0,0,0,0,0,0,0]#this takes extra space as table
x=fib(5,arr)
print(x)

#bottom up approach
def fib(n):
    if n==0 or n==1:
        return n
    a=0
    b=1
    for i in range(2,n+1):
        c=a+b
        a=b
        b=c
    return b
x=fib(6)
print(x)
    












    

        
