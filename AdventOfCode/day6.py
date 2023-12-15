time_dist = {53:313,89:1090,76:1214,98:1201}
p=1
for key,value in time_dist.items():
    endf = key//2 + 1
    if key%2 == 0:
        endr = key//2 - 1
    else:
        endr = key//2

    flist=list(range(0,endf))
    blist=list(range(key,endr,-1))
    z=[(f,b) for f, b in zip(flist,blist)
            if f*b > value]
    if key%2 == 0:
        wins=(len(z) - 1)*2 + 1
    else:
        wins=(len(z)*2)
    p *= wins


print(p)
