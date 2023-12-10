import re
"""Part 1"""
"""sum_possible = 0
Impossible = {'red':12,
              'green':13,
              'blue':14}

with open("data2.txt", "r") as file:
    for line_number, line in enumerate(file):
        line = line.replace(':',',')
        line = line.replace(';',',')
        line_list = [c.strip() for c in line.split(',')]
        game = line_number + 1
        
        for c in line_list[1:]:
            num,colour=c.split(' ')
            num = int(num)
            if num > Impossible[colour]:
                break
        else:
            sum_possible += game
print(sum_possible)"""

"""Part 2"""

sum_power = 0
with open("data2.txt", "r") as file:
    for line in (file):
        line = line.replace(':',',')
        line = line.replace(';',',')
        line_list = [c.strip() for c in line.split(',')]
        d = {'green':0,'red':0,'blue':0} 

        for c in line_list[1:]:
            num,colour=c.split(' ')
            if d[colour] < int(num):
                d[colour] = int(num)

        power = d['blue']*d['green']*d['red']
        sum_power += power

print(sum_power)