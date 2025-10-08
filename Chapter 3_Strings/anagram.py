# Read two strings
A = input().strip()
B = input().strip()

# Check if they are anagrams by sorting and comparing
if sorted(A) == sorted(B):
    print("Yes")
else:
    print("No")