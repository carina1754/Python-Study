word = input('단어를 입력하시오')
n = len(word)
for i in range(n//2):
    if word[i] == word[-1-i]:
        print('회문입니다')
        break
    else:
        print('회문이 아닙니다')
        break