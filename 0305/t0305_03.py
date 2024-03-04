import operator
a,b,c = 0,0,0
print(a,b,c)

icecream = {'혁신': 4, '초대': 1, '대표': 3, '조국': 5, '법무부': 1}

iList = sorted(icecream.items())
print(iList)
print("-"*20)
iList2 = sorted(icecream.items(),key=operator.itemgetter(0),reverse=True)
print(iList2)
print("-"*20)
print(dict(iList2))
print("-"*20)
iList3 = sorted(icecream.values())
print(iList3)
print("-"*20)
iList4 = sorted(icecream.values(),reverse=True)
print(iList4)
