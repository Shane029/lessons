word1 = input('Enter the first word:   ')
word2 = input('Enter the second word:   ')
annogramm1 = {}
annogramm2 = {}
count = 1
for i in word1:
    annogramm1[i] = count
for j in word2:
    annogramm2[j] = count
      
print(annogramm1 == annogramm2 and len(word1) == len(word2))