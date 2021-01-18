word = input('input word : ')
flag = 0
for i in range(int(len(word)/2)):
    if word[i]==word[-i-1]:
        flag = 1
    else:
        flag = 0
if flag == 1:
    print("회문")
else:
    print("회문아님")