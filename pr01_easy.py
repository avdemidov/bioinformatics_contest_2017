import sys

chemicals = set([int(x) for x in sys.stdin.readline().strip().split(" ")])

r = []
l = []
n = 0
used_numbers = set()

lines = sys.stdin.readlines();
for line in lines:
    left, right = [set([int(y) for y in x.split("+")]) for x in line.strip().split("->")]
    if left.issubset(chemicals):
        chemicals = chemicals.union(right)
    else:
        l.append(left)
        r.append(right)
        used_numbers.add(n)
        n += 1

found = True
while found:
    found = False
    for i in used_numbers:
        if l[i].issubset(chemicals):
            chemicals = chemicals.union(r[i])
            found = True
            used_numbers.remove(i)
            break

for c in chemicals:
    print(c, end=" ")
print()
