N= input()
k= input()
s = k.split(" ")
a = []
for ia in s:
    a.append(int(ia))
N = len(a)
e=0
for i in range(0, N-1):
    for j in range(0, N-1-i):
        if a[j]>a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
            e+=1
            print(" ".join(map(str, a)))
if e ==0:
    print("0")

