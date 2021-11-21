_end = '_end_'

def make_trie(*words):
    root = dict()
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        current_dict[_end] = _end
    return root

make_trie('foo', 'bar', 'baz', 'barz')
{'b': {'a': {'r': {'_end_': '_end_', 'z': {'_end_': '_end_'}}, 
             'z': {'_end_': '_end_'}}}, 
 'f': {'o': {'o': {'_end_': '_end_'}}}}

def in_trie(trie, word):
    current_dict = trie
    for letter in word:
        if letter not in current_dict:
            return False
        current_dict = current_dict[letter]
    return _end in current_dict

in_trie(make_trie('foo', 'bar', 'baz', 'barz'), 'baz')
True
in_trie(make_trie('foo', 'bar', 'baz', 'barz'), 'barz')
True
in_trie(make_trie('foo', 'bar', 'baz', 'barz'), 'barzz')
False
in_trie(make_trie('foo', 'bar', 'baz', 'barz'), 'bart')
False
in_trie(make_trie('foo', 'bar', 'baz', 'barz'), 'ba')
False
