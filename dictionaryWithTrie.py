import csv

meanings = []
enrolledWords = []

with open("teste.csv", "r", encoding='utf-8-sig') as arquivo:
	arquivo_csv = csv.reader(arquivo,delimiter =";")
	for linha in arquivo_csv:
            enrolledWords.append(linha[0])
            meanings.append(linha[1])    

_end = 'meaning'

def trieMaker(words):
    
    root = dict()  
    i = 0

    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict[_end] = meanings[i]
        i += 1 
    return root
    
trie = trieMaker(enrolledWords)

def existingWord(word):
   current_dict = trie
   for letter in word:
       if letter not in current_dict:
           return False
       current_dict = current_dict[letter]
   return current_dict.get('meaning')

print(existingWord('lousa'))
