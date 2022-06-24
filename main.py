
s = 'azerdii'
k = 5

# Write your code here
s = list(s)
print(s[0:7])
alph = ['a', 'e', 'i', 'o', 'u']
mx = 0
i = 0
vowels = 0
ans = ''
print(s, k, len(s))
while i <= len(s):
    if i >= k:
        print(s[i - k:i], i - k, i, len(s))
    if i == k:
        for j in alph:
            vowels += s[i - k:i].count(j)
    elif i > k:
        if s[i - k - 1] in alph:
            vowels -= 1
        if s[i - 1] in alph:
            vowels += 1
        if vowels > mx:
            mx = vowels
            ans = ''.join(s[i - k:i])
    print(vowels)
    i += 1
print(ans)


