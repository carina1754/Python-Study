n=int(input('n:(1<=n<=10000)'))
n_list=list(range(1,n+1))
hap=0
num=0
for i in range(len(n_list)):
    hap+=n_list[num]
    num+=1
print(hap)