test= [1,1,2,3,1,4,3,0,0]
ntest=[]
"""for c in test:
    if c not in ntest:
        ntest.append(c)
print(ntest)"""
for i,c in enumerate(test):
    if c in test[:i]:
        del test[i]
print(test)




"""
test=[1,1]
for i in range(1,11):
    for j in range(i):
        test.append(0)
    test.append(1)
print(test)
"""