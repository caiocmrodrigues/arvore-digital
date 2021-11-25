import csv
import re
from collections import Counter

meanings = []
enrolledWords = []


def openCsvFile(csvFileName):
    with open(csvFileName, "r", encoding='utf-8-sig') as file:
        csvFile = csv.reader(file, delimiter=";")
        for row in csvFile:
            enrolledWords.append(row[0])
            meanings.append(row[1])


# SPELLING CORRECTOR
def words(text): return re.findall(r'\w+', text.lower())


WORDS = Counter(words(open('teste.csv').read()))


def P(word, N=sum(WORDS.values())):
    "Probability of `word`."
    return WORDS[word] / N


def correction(word):
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)


def candidates(word):
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])


def known(words):
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)


def edits1(word):
    "All edits that are one edit away from `word`."
    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)


def edits2(word):
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))


# DICTIONARY
def trieMaker(words):
    _end = 'meaning'
    root = dict()
    i = 0

    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict[_end] = meanings[i]
        i += 1
    return root


def existingWord(word):
    current_dict = trieMaker(enrolledWords)
    for letter in word:
        if letter not in current_dict:
            return 'você quis dizer: ' + correction(word)
        current_dict = current_dict[letter]
    return current_dict.get('meaning')


def main():
    print("Insira o nome do banco de dados (csv):")
    csvFileName = input()

    print("Insira a palavra:")
    wordToCheck = input()

    openCsvFile(csvFileName)
    # print(trieMaker(enrolledWords))
    print(existingWord(wordToCheck))


# Start!
main()
