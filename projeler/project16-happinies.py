'''
def change(s, num):
    for i in range(num):
        s[i] = int(s[i])
    
    return s


a, b = map(int, input().split())
l1 = input()
a1 = input()
b1 = input()

l2 = l1.split(" ")
a2 = a1.split(" ")
b2 = b1.split(" ")

happinees = 0

l2 = change(l2, a)
a2 = change(a2, b)
b2 = change(b2, b)

for x in l2:
    if x in a2:
        happinees +=1
    if x in b2:
        happinees -=1

print(happinees)
'''
'''
_, _ = input().split()
s = input().split()
a = set(input().split())
b = set(input().split())
print(len([x for x in s if x in a]) - len([x for x in s if x in b]))
'''
def DifferentCases(str): 
    newStr = ''
    finalWord = []
    
    for char in str:
        if char.isalpha():
            newStr += char
        else:
            newStr += ' '
            
    for word in newStr.split():
        word = word.replace(word[0], word[0].upper())
        word = word.replace(word[1:len(word)], word[1:len(word)].lower())
        finalWord.append(word)
        
    return ''.join(finalWord)
print(DifferentCases(input()))