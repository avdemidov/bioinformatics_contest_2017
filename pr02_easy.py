import sys

complementary = {'G':'C', 'C':'G', 'A':'U', 'U':'A'}
d = []

def opt(i, j):
    if i >= j:
        return 0
    if d[i][j] != -1:
        return d[i][j]

    res = 0
    if s[i] == complementary[s[j]]:
        res = opt(i+1, j-1)+1
    else:
        res = max(res, opt(i, j-1), opt(i+1, j))

    for k in range(i+1, j-1):
        res = max(res, opt(i, k)+opt(k+1, j))

    d[i][j] = res
    return res


s = sys.stdin.readline().strip()

len_s = len(s)
for i in range(0, len_s):
    d.append([-1]*len_s)

r = opt(0, len_s-1)

result = "imperfect"
if r == len_s // 2:
    if len_s % 2 == 1:
        result = "almost perfect"
    else:
        result = "perfect"
print(result)
