lines=['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'
]
scards=0
sumpoints=0
with open("data4.txt", "r") as file:
    for line in file:
        line_list = line.split('|')
        card=line_list[1].split(' ')
        card= [int(c) for c in card if c != '']
        win = line_list[0].split(' ')
        win = [int(c) for c in win if c.isdigit()]
        matched=[]
        for i in card:
            if i in win:
                matched.append(i)
        if len(matched) > 0:
            points = 2**(len(matched)-1)
            sumpoints += points
print(sumpoints)