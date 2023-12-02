sum = 0
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
with open("data_1.txt", "r") as file:
    for line in file:
        digit_str=''
        for i, c in enumerate(line):
            if c.isdigit():
                digit_str += c
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
                    digit_str += word_to_digit[word]
                    #print(ldigit)
        if len(digit_str) == 1:
            digit_str += digit_str
        else:
            digit_str = digit_str[0] + digit_str[-1]
        digit = int(digit_str)
        sum += digit

print(sum)