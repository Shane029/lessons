word1 = input('Enter the first word:   ').lower()
word2 = input('Enter the second word:   ').lower()
annogramm1 = {}
annogramm2 = {}
count = 1
for i in word1:
    if i == ' ':
        continue
    annogramm1[i] = count
for j in word2:
    if j == ' ':
        continue
    annogramm2[j] = count
      
print(annogramm1 == annogramm2 and len(word1) == len(word2))