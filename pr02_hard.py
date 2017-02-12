import sys

complementary = {'G':'C', 'C':'G', 'A':'U', 'U':'A'}

rna = sys.stdin.readline().strip()

rna_len = len(rna)
stack = []

stack_len = 1
stack.append(rna[0])

for i in range(1, rna_len):
    if stack_len > 0 and rna[i] == complementary[stack[stack_len-1]]:
        stack.pop()
        stack_len -= 1
        assert stack_len >= 0, "Length of stack could not be negative!"
    else:
        stack.append(rna[i])
        stack_len += 1

result = "imperfect"
if rna_len % 2 == 0:
    if stack == []:
        result = "perfect"
else:
    # check if stack is a palindrome
    is_palindrome = all(stack[i] == complementary[stack[stack_len-i-1]] for i in range(stack_len // 2))
    if stack_len % 2 == 1 and is_palindrome: 
        result = "almost perfect"
print(result)
