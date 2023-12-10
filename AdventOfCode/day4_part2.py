lines=['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11']

totalcards=0
cards={i:[1,[]] for i in range(1,217)}
with open("data4.txt", "r") as file:
    for line in file: # this loop adds the list of matching cards to each card
        line_list = line.split('|')
        card=line_list[1].split(' ')
        card= [int(c) for c in card if c != '']
        win = line_list[0].split(' ')
        win=[s for s in win if s]
        card_num = int(win[1].strip(':'))
        win = [int(c) for c in win if c.isdigit()]
        matched=0
        for i in card:
            if i in win:
                matched += 1
        if matched > 0:
            end=card_num+matched+1
            for j in range(card_num+1,end): #matching cards are gotten by increment the card numbe in a range of 1 until the total number of matches
                cards[card_num][1].append(j)

def scratchcards(match_card): #this recursive functions tries to get all instances of cards won from original card, calls itself until it reaches a card with no matches
    global cards
    cards[match_card][0] += 1
    if len(cards[match_card][1]) > 0:
        for m in cards[match_card][1]:
            scratchcards(m)


for key in cards:
    if len(cards[key][1]) > 0:
        for i in cards[key][1]:
            scratchcards(i)
    
for key in cards:
    totalcards += cards[key][0]
print(totalcards)
