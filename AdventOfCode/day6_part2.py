time = 53897698
dist= 313109012141201

endf = time//2 + 1
endr = time//2 - 1

flist=list(range(0,endf))
blist=list(range(time,endr,-1))
z=[(f,b) for f, b in zip(flist,blist)
            if f*b > dist]

wins=(len(z) - 1)*2 + 1

print(wins)