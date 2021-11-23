_end = '_end_'
meanings = []

def trieMaker(*words):
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict[_end] = _end
    return root

# TODO WE MUST CHANGE THIS HARDCODED LIST FOR A DATABASE
trie = trieMaker('foo', 'bar', 'baz', 'barz')

def existingWord(word):
   current_dict = trie
   for letter in word:
       if letter not in current_dict:
           return False
       current_dict = current_dict[letter]
   return _end in current_dict

def insertMeaning(word, meaning):
    if(existingWord(word)):
        meanings.append([word, meaning])
        return "Definição adicionada"
    else:
        return "Palavra não encontrada"

def gettingMeaning(word):
    if(existingWord(word)):
        return meanings[0][1]
    else:
        return "Definição não encontrada"

insertMeaning('bar', 'testing a definition')
print(gettingMeaning('taua'))
