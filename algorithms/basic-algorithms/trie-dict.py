import collections

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root

        for i, char in enumerate(word):
            if i == len(word) - 1:
                node.children[char].is_word = True
            else:
                node = node.children[char]

    def exists(self, word):
        node = self.root

        for i, char in enumerate(word):
            if i == len(word) - 1:
                return node.children[char].is_word
            else:
                node = node.children[char]

valid_words = ['the', 'a', 'there', 'answer', 'any', 'by', 'bye', 'their']
word_trie = Trie()
for valid_word in valid_words:
    word_trie.add(valid_word)

# Tests
assert word_trie.exists('the')
assert word_trie.exists('any')
assert not word_trie.exists('these')
assert not word_trie.exists('zzz')
print('All tests passed!')
