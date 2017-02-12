import sys

max_elem = 10**5+10    

p = [-1]*max_elem
rank = [0]*max_elem

def make_set(x):
    p[x] = x
    rank[x] = 0

def union(x, y):
    if rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]





flags = [False]*max_elem
chemicals = [int(x) for x in sys.stdin.readline().strip().split(" ")]
for c in chemicals:
    flags[c] = True

first_chemical =  chemicals[0]

react = []
n = 0
lines = sys.stdin.readlines()
for line in lines:
    l, r = [[int(y) for y in x.split("+")] for x in line.strip().split("->")]
    react.extend([tuple([l,r])])
    n += 1

if n == 0:
    i = 0
    while i < max_elem:
        if flags[i]:
            print(i, end=" ")
        i += 1
    print()
    exit()

link_n = list(range(1, n+1))
link_n[n-1] = 0

link_p = list(range(-1, n-1))
link_p[0] = n-1

i = 0
while i < n: 
    for e in react[i][0]: 
        flags[e] = True
    for e in react[i][1]:
        flags[e] = True
    i += 1

i = 0
while i < max_elem:
    if flags[i]:
        make_set(i)
    i += 1 

# set of substrate
for c in chemicals:
    union(first_chemical, c)

found = True
b = -1
i = 0
while found:
    found = False
    j = 0
    while j < n: # go along reactions list
        # if all of left part exits in "main set"
        if all(find_set(first_chemical) == find_set(le) for le in react[i][0]): 
            for ri in react[i][1]: # add right part chemicals to "main set"
                union(first_chemical, ri)
            found = True
            link_n[ link_p[i] ] = link_n[i]
            link_p[ link_n[i] ] = link_p[i]
            n -= 1
        j += 1
        b = i
        i = link_n[i]
        if b == i: 
            found = False
            break

i = 0
while i < max_elem:
    if flags[i]:
        if find_set(first_chemical) == find_set(i):
            print(i, end=" ")
    i += 1
print()