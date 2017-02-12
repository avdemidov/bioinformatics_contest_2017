import sys
from collections import defaultdict

MAX_ELEM = 0xffffffff 
MAX_REACTIONS = 10**5 + 10 

substrate_in_rections = defaultdict(lambda : []) 
number_of_missing_chemicals = [0]*MAX_REACTIONS  

right = []
left = []
n = 0
chemicals = set([int(x) for x in sys.stdin.readline().strip().split(" ")])
lines = sys.stdin.readlines();
for line in lines:
    l, r = [set([int(y) for y in x.split("+")]) for x in line.strip().split("->")]
    left.append(l)
    right.append(r)
    # store the list of reactions in which an element is a substrate
    for e in l:
        substrate_in_rections[e].append(n)
    # store the number of required substrates
    number_of_missing_chemicals[n] = len(l)
    n += 1

# BFS
queue = list(chemicals)
queue_len = len(queue)
while queue_len > 0:
    cur = queue.pop()
    queue_len -= 1
    for x in substrate_in_rections[cur]:
        number_of_missing_chemicals[x] -= 1
        assert number_of_missing_chemicals[x] >= 0, "Number of not presented chemicals could not be negative!"
        if number_of_missing_chemicals[x] == 0:
            for y in right[x]:
                if y not in chemicals:
                    queue.insert(0, y)
                    queue_len += 1
                    chemicals.add(y)

print(" ".join(str(c) for c in chemicals))
