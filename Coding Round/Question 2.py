
#Program to find the LCM of a given array elements
def lcm_array(no1,no2):
    if no1>no2:
        nu=no1
        de=no2
    else:
        nu=no2
        de=no1
    re=nu%de
    while(re!=0):
        nu=de
        de=re
        re=nu%de
    gc=de
    lc=int(int(no1*no2)/int(gc))
    return lc
size=int(input("Enter the size of array: "))
arr=[]
for i in range(size):
    arr.append(int(input("Value: ")))
no1=arr[0]
no2=arr[1]
lcm=lcm_array(no1,no2)
for i in range(2,len(arr)):
    lcm=lcm_array(lcm,arr[i])
print(lcm)
