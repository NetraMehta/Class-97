introString = input('Enter your introduction: ')

print(introString)

characterCount = 0

for i in introString : 
    characterCount = characterCount + 1

print(characterCount)

wordCount = 1

for i in introString : 
    if i==' ' : 
        wordCount = wordCount + 1

print(wordCount)