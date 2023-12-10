"""Part 1"""
import time
start_time = time.time()
from string import punctuation

symbols = punctuation.replace('.','')
sum_parts=0

def symbol_same_line(fnum,sline,before,after): #check if number is part_number by having a symbol before/after on the same line
    for c in sline[before:after]:
        if c in symbols:
            part_num = int(fnum) #if yes, then it is a part_num
            global sum_parts 
            sum_parts += part_num #add it to sum of parts
            return sum_parts

def symbol_line_above(fnum,aline,before,after): #check if number is part_number by having a symbol before/after on the lilne above
    if aline == '':
        return None
    for c in aline[before:after]:
        if c in symbols:
            part_num = int(fnum) #if yes, then it is a part_num
            global sum_parts 
            sum_parts += part_num #add it to sum of parts
            return sum_parts
    
def symbol_line_below(fnum,bline,before,after): #check if number is part_number by having a symbol before/after on the line below
    if bline == '':
        return None
    for c in bline[before:after]:
        if c in symbols:
            part_num = int(fnum) #if yes, then it is a part_num
            global sum_parts 
            sum_parts += part_num #add it to sum of parts
            return sum_parts

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
    i=0
    while i < len(line): #loop would run on each character of a line
        if line[i].isdigit() is False:
            i += 1
            continue
        #if any character is a digit, it maybe a part_number
        for j in range(3,0,-1): #this loop groups possible digits together, starting with a number of 3 digits, 2, then 1
            if i+j < len(line): #avoid list out of index error
                num = line[i:i+j] #possible group of numbers
            elif i+j == len(line):
                num = line[i:] #possible group of numbers
            if num.isdigit(): #if group of 3,2,1 digits is a number, it may be a part_number
                sym_before = i-1 #character before number
                sym_after = i+j+1 #character after number
                valid=0
                i = sym_after #change position of counter in each line after finding a group of digits
                if (sym_before >= 0) and (sym_after < len(line)): #dealing with numbers in between the first and last character
                    valid = symbol_same_line(num,line,sym_before,sym_after) 
                    if valid is not None:
                        break #leave for loop
                    valid = symbol_line_above(num,line_above,sym_before,sym_after)
                    if valid is not None:
                        break
                    valid = symbol_line_below(num,line_below,sym_before,sym_after)
                    if valid is not None:
                        break
                elif (sym_before < 0):  #dealing with first characters
                    valid = symbol_same_line(num,line,0,sym_after)
                    if valid is not None:
                        break #leave for loop
                    valid = symbol_line_above(num,line_above,0,sym_after)
                    if valid is not None:
                        break
                    valid = symbol_line_below(num,line_below,0,sym_after)
                    if valid is not None:
                        break
                elif (sym_after == len(line)): #dealing with last characters
                    valid = symbol_same_line(num,line,sym_before,len(line)-1)
                    if valid is not None:
                        break #leave for loop
                    valid = symbol_line_above(num,line_above,sym_before,len(line_above)-1)
                    if valid is not None:
                        break
                    valid = symbol_line_below(num,line_below,sym_before,len(line_below)-1)
                    if valid is not None:
                        break
                break #if group of 3/2/1 is a digit, break out of loop with range function

print(sum_parts)                   

end_time = time.time()
exe = end_time - start_time
print(exe)