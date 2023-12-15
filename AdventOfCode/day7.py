from collections import Counter

content={'2':0,'3':1,'4':2,'5':3,'6':4,'7':5,'8':6,'9':7,'T':8,'J':9,'Q':10,'K':11,'A':12} #Key for sorting cards of the same type
Five_kinds=[]
Four_kinds=[]
Full_houses=[]
Three_kinds=[]
Two_pairs=[]
One_pairs=[]
High_cards=[]

"""with open("data7.txt", "r") as file:
    #read each line of the input to determine the type of a card following the description from AOC
    for line in file:
        card = line.split()[0]
        bid = int(line.split()[1])
        details=Counter(card)
        length = len(details)
        if length == 1:
            Five_kinds.append([card,bid]) #add to five_kind
        elif length == 2:
            if 1 in details.values():
                Four_kinds.append([card,bid]) #add to four
            else:
                Full_houses.append([card,bid]) #add to fullhouse
        elif length == 3:
            if 3 in details.values():
                Three_kinds.append([card,bid]) #add to threekind
            else:
                Two_pairs.append([card,bid]) #add to twopair
        elif length == 4:
            One_pairs.append([card,bid]) #add to onepair
        else:
            High_cards.append([card,bid]) #add to Highcard"""


def sort_cards(card_type):
    """This function sorts the cards for each type. This first step in this sorting is to separate each card type into a list of numbers only and then a mixed list
        Then we use a bubble sort algorithm to sort the mixed list. The key for comparism comes from the content dictionary"""
    num=[sublist for sublist in card_type if sublist[0].isdigit()]
    num.sort()
    mixed=[sublist for sublist in card_type if sublist[0].isdigit() is False]
    n = len(mixed)
    global content
    for i in range(n):
        for j in range(0,n-i-1):
            for c,s in zip(mixed[j][0],mixed[j+1][0]):
                if content[c] == content[s]:
                    continue
                if content[c] > content[s]:
                    mixed[j],mixed[j+1] = mixed[j+1],mixed[j]
                    break
                if content[c] < content[s]:
                    break
    return num+mixed

with open("day7.txt","x") as file:
    #create a new file with the different card_types to determine the rank of each card. Cardtypes are sorted before writing them to the file
    file.write("\n".join([" ".join(str(element) for element in sublist) for sublist in sort_cards(High_cards)]))
    file.write("\n")
    file.write("\n".join([" ".join(str(element) for element in sublist) for sublist in sort_cards(One_pairs)]))
    file.write("\n")
    file.write("\n".join([" ".join(str(element) for element in sublist) for sublist in sort_cards(Two_pairs)]))
    file.write("\n")
    file.write("\n".join([" ".join(str(element) for element in sublist) for sublist in sort_cards(Three_kinds)]))
    file.write("\n")
    file.write("\n".join([" ".join(str(element) for element in sublist) for sublist in sort_cards(Full_houses)]))
    file.write("\n")
    file.write("\n".join([" ".join(str(element) for element in sublist) for sublist in sort_cards(Four_kinds)]))
    file.write("\n")
    file.write("\n".join([" ".join(str(element) for element in sublist) for sublist in sort_cards(Five_kinds)]))

sumbid=0
with open("day7.txt","r") as file:
    #read from the sorted file of cards and compute their winnings, then sum for total winnings
    for line_num, line in enumerate(file):
        product = 0
        index=line_num+1
        bid = int(line.split()[1])
        product = index*bid
        sumbid += product

print(sumbid)