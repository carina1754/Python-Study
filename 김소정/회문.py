word: int(input('단어를 입력하시오:'))
n=len(word)
for i in range(n):
    if word[i]==word[n-1-i]:
        print('회문입니다.')
    else :
        print('회문이 아닙니다')
    
    
    