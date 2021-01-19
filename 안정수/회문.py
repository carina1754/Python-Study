word = input('input word : ')

for i in range(len(word)//2):
    if word[i] != word[-i-1]:
        print("회문아님")
        break
else:
    print("회문")