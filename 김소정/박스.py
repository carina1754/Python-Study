box=input().split()
dot=input().split()
for i in dot:
    if j in box:
        if (i[0] < j[0]) or (i[0]>j[2]) or (i[1]<j[1])or(i[1]>j[3]):
            print('out')
        else :
            print('in')