"""Part 2"""
import time
start_time = time.time()
#lines=['467..114..','...*......','..35..633.','......#...','617*......','.....+.58.','..592.....','......755.','...$.*....','.664.598..']
#length = len(lines)

def check_left(left): #where left(left side) only contains 3 characters to the left of * 
    if left[3].isdigit():
        for j in range(1,4):
            if left[j:].isdigit():
                num = left[j:]
                return int(num)
    else:
        for j in range(0,3):
            if left[j:3].isdigit():
                num = left[j:3]
                return int(num)
        
def check_right(right): #where right(right side) only contains 3 characters to the left of * 
    if right[0].isdigit():
        for j in range(3,0,-1):
            if right[:j].isdigit():
                num = right[:j]
                return int(num)
    else:
        for j in range(4,0,-1):
            if right[1:j].isdigit():
                num = right[1:j]
                return int(num)

sumgear=0

def gear_product(pdt):
    gearp = int(pdt[0])*int(pdt[1])
    global sumgear
    sumgear += gearp

with open("data3.txt", "r") as file: #reading data
    lines=file.readlines() #converting to a list because I need the length of the file and file does not have a len() function
    length = len(lines)
for line_number,line in enumerate(lines): #loop would run on each line of the file
    if line_number-1 < 0:
        line_above = ''
    else: line_above = lines[line_number - 1]
    if line_number + 1 >= length:
        line_below = ''
    else: line_below = lines[line_number + 1]

    for i,c in enumerate(line):
        if c != '*':
            continue
        gear=[]
        if line[i-1].isdigit() or line[i+1].isdigit():
            pnum = check_left(line[i-3:i+1])
            if pnum is not None:
                gear.append(pnum)
            pnum = check_right(line[i:i+4])
            if pnum is not None: 
                gear.append(pnum)
            if len(gear) == 2:
                gear_product(gear)
                continue
        if line_above != '': #check line above
            if line_above[i-1:i+2].isdigit():
                gear.append(int(line_above[i-1:i+2]))
                if len(gear) == 2:
                    gear_product(gear)
                    continue
            elif (line_above[i+1].isdigit is False) or (line_above[i-1].isdigit()):
                pnum = check_left(line_above[i-3:i+1])
                if pnum is not None: 
                    gear.append(pnum)
                if len(gear) == 2:
                    gear_product(gear)
                    continue   
            elif (line_above[i-1].isdigit is False) or (line_above[i+1].isdigit()):
                pnum = check_right(line_above[i:i+4])
                if pnum is not None:
                    gear.append(pnum)
                if len(gear) == 2:

                    gear_product(gear)
                    continue
            elif line_above[i].isdigit():
                pnum = int(line_above[i])
                if pnum is not None:
                    gear.append(pnum)
                if len(gear) == 2:

                    gear_product(gear)
                    continue
        if line_below != '': #check in line below
            if line_below[i-1:i+2].isdigit():
                gear.append(int(line_below[i-1:i+2]))
                if len(gear) == 2:
                    gear_product(gear)   
                    continue
            elif (line_below[i+1].isdigit is False) or (line_below[i-1].isdigit()):
                pnum = check_left(line_below[i-3:i+1])
                if pnum is not None:
                    gear.append(pnum)
                if len(gear) == 2:
                    gear_product(gear)
                    continue
            elif (line_below[i-1].isdigit is False) or (line_below[i+1].isdigit()):
                pnum = check_right(line_below[i:i+4])
                if pnum is not None:
                    gear.append(pnum)
                if len(gear) == 2:
                    gear_product(gear)
                    continue
            elif line_below[i].isdigit():
                pnum = int(line_below[i])
                if pnum is not None:
                    gear.append(pnum)
                if len(gear) == 2:

                    gear_product(gear)
                    
                    continue
        print(gear)
print(sumgear)

