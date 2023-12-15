from collections import Counter

content={'J':0,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'T':9,'Q':10,'K':11,'A':12} #Key for sorting cards of the same type
Five_kinds=[]
Four_kinds=[]
Full_houses=[]
Three_kinds=[]
Two_pairs=[]
One_pairs=[]
High_cards=[]
joker_cards=[]

def joker(jcard,jbid,d,l):
    #figure out how to deal with cards that have J in them.
    if l == 1:
        Five_kinds.append([jcard,jbid]) 
    elif l == 2:
        Five_kinds.append([jcard,jbid])
    elif length == 3:
        if 3 in details.values():
            Four_kinds.append([jcard,jbid]) 
        elif d['J']== 2:
            Four_kinds.append([jcard,jbid]) 
        elif d['J'] == 1:
            Full_houses.append([jcard,jbid]) 
    elif length == 4:
        Three_kinds.append([card,bid]) 
    else:
        One_pairs.append([card,bid]) 

with open("data7.txt", "r") as file:
    #read each line of the input to determine the type of a card following the description from AOC
    for line in file:
        card = line.split()[0]
        bid = int(line.split()[1])
        details=Counter(card)
        length = len(details)
        if 'J' in details:
            joker(card,bid,details,length)
        else:
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
                High_cards.append([card,bid]) #add to Highcard


def sort_cards(card_type):
    """This function sorts the cards for each type. Used bubble sort algorithm on each card_type. The key for comparism comes from the content dictionary"""
    n = len(card_type)
    global content
    for i in range(n):
        for j in range(0,n-i-1):
            for c,s in zip(card_type[j][0],card_type[j+1][0]):
                if content[c] == content[s]: #swap cards based on the strength of its characters as defined by the content dictionary
                    continue
                if content[c] > content[s]:
                    card_type[j],card_type[j+1] = card_type[j+1],card_type[j]
                    break
                if content[c] < content[s]:
                    break
    return card_type

with open("jday7.txt","x") as file:
    #create a new file with the different card_types to determine the rank of each card. Cardtypes are sorted before writing them to the file
    file.write("\n".join([" ".join(str(element) for element in sublist) for sublist in sort_cards(High_cards)])) #for each card in a cardtype, add it as a newline with the type and bid separated by space, and each card separated by a newline
    file.write("\n") #newline for each new card_type
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
with open("jday7.txt","r") as file:
    #read from the sorted file of cards and compute their winnings, then sum for total winnings
    for line_num, line in enumerate(file):
        product = 0
        index=line_num+1
        bid = int(line.split()[1])
        product = index*bid
        sumbid += product

print(sumbid)