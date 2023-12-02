word_to_digit = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}
lines = ['gtlbhbjgkrb5sixfivefivetwosix','ninevct4cpdvqfxmspbz9xrvxfvbpzthreesfnncrqn','26rqmtqznds','78four']
digits=[]
for line in lines:
    ldigit=''
    for i, c in enumerate(line):
        if c.isdigit():
            ldigit += c
        for j in range(3,6):
            word = ''
            if i+j < len(line):
                word = line[i:i+j]
                #print(i,j,i+j,word)
            elif i+j == len(line):
                word = line[i:]
                #print(i,j,i+j,word)
            if word in word_to_digit:
                #print('d',word)
                ldigit += word_to_digit[word]
                #print(ldigit)
    digits.append(ldigit)

print(digits)