class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    #Insert word into Trie
    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    #Search exact word
    def search(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    #Search for prefix
    def startsWith(self, prefix: str):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
trie = Trie()
trie.insert("apple")
trie.insert("app")
print(trie.search("app"))
print(trie.search("apz"))
print(trie.startsWith("ap"))