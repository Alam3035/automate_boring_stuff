print('Enter the English message to translate into Pig Latin')

message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = []

for word in message:
    # Separate the non-letters at the start of this word:
    prefixNonLetter = ''
    while len(word) > 0 and word[0].isalpha():
        prefixNonLetter += word[0]
        word = word[1:]

    if len(word) == 0:
        pigLatin.append(prefixNonLetter)
        continue

    # Separate the non-letters at the end of this word:
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[-1]

    # Remember if the word was in uppercase or title case:
    wasUpper = word.isupper()
    wasTitle = word.istitle()
    word = word.lower()
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[1:]
    
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'

    if wasUpper:
        word = word.upper()
    
    if wasTitle:
        word = word.title()

    pigLatin.append(prefixNonLetter + word + suffixNonLetters)

print(' '.join(pigLatin))
