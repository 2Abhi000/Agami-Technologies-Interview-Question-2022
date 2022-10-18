
#Program to find gcd or hcf of two numbers
def mygcdprog(a,b):
    res=min(a,b)
    while res:
        if a%res== 0 and b%res==0:
            break
        res-=1
    return res
n1=int(input("Enter the number1: "))
n2=int(input("Enter the number2: "))
ans=mygcdprog(n1,n2)
print(ans)

