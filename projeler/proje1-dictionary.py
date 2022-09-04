n, m = map(int, input().split())

from collections import defaultdict

l1 = defaultdict(list)
l2 = []

for i in range(n):
    l1[input()].append(i+1)


for x in range(m):
    l2.append(input())
    

for y in range(m):
    if l2[y] in l1:
        print(*l1[l2[y]]) # * işareti normalde dictionary output olarak [1,2,3] şeklinde çıkarken * ile 1 2 3 olarak çıkıyor.
    else:
        print("-1")