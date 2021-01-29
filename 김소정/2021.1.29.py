a=int(input())
b=int(input())
c=int(input())
d=a*b*c
D=list(str(d))
print(D)
count_0=0
count_1=0
count_2=0
count_3=0
count_4=0
count_5=0
count_6=0
count_7=0
count_8=0
count_9=0
num=0
for i in range(1):
    for j in range(len(D)):
        if D[num]=='0':
            count_0 +=1
            num+=1
        elif D[num]=='1':
            count_1 +=1
            num+=1
        elif D[num]=='2':
            count_2 +=1
            num+=1
        elif D[num]=='3':
            count_3 +=1
            num+=1
        elif D[num]=='4':
            count_4 +=1
            num+=1
        elif D[num]=='5':
            count_5 +=1
            num+=1
        elif D[num]=='6':
            count_6 +=1
            num+=1
        elif D[num]=='7':
            count_7 +=1
            num+=1
        elif D[num]=='8':
            count_8 +=1
            num+=1
        elif D[num]=='9':
            count_9 +=1
            num+=1
print('0:',count_0,
       '1:',count_1,
       '2:',count_2,
       '3:',count_3,
       '4:',count_4,
       '5:',count_5,
       '6:',count_6,
       '7:',count_7,
       '8:',count_8,
       '9:',count_9,)
