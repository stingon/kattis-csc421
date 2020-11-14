Created on Sat Nov 14 00:02:41 2020

@author: dt
"""

def findIndex(k, n):
    if (n==1):
        return 'N'
    elif (n == 2):
        return 'A'
    a = length[n-2]
    if(k > a):
        return findIndex(k-a,n-1)
    return findIndex(k,n-2)

[n , k] = input().split()
n = int(n)
k = int(k)
length=[]
for i in range (n):
    if(i == 0):
        length.append(0)
    if(i==1):
        length.append(1)
    else:
        length.append(length[i-2] +length[i-1])

print(findIndex(k,n))
