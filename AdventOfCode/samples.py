lines=['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']

sum_power = 0
for line in (lines):
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