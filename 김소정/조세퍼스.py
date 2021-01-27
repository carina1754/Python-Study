#소수판별
num = int(input('숫자를 입력:'))
a = 2
while ( int ( num / 2 ) != a ):
    if num % a == 0:
        print('소수아니다')
        break
    a+=1

if (num % a != 0)or(num==2)or(num==3):
    print('소수이다')

