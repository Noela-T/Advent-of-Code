from string import punctuation
symbols = punctuation.replace('.','')
sum_parts=0
line='......194..380....@....900..........639....467........478*..............582...........798.............326...........894.........#...........'
print(line[54:54+4])
def symbol_same_line(fnum,sline,before,after):
    for c in sline[before:after]:
        if c in symbols:
            part_num = int(fnum) #if yes, then it is a part_num
            print(part_num)
            global sum_parts 
            sum_parts += part_num #add it to sum of parts
            return sum_parts

            
symbol_same_line(478,line,54,57+1)