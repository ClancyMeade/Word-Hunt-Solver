# File creates a Trie for valid WordHunt words 

# Node in a Trie used to store a character in a word 
class TrieNode: 
    def __init__(self, character, is_complete_word, parent): 
        self.letter = character 
        self.children = {} # (Key = character, Value = TrieNode)
        self.is_complete_word = is_complete_word
        self.parent = parent 
    
    def __repr__(self): 
        return "TN(%s, %s, %s)" % (self.character, self.is_complete_word, self.children) 

# Trie data structure (type of k-ary search tree)
# Each Node represents a character in a word
# Used to store all valid words for quick lookup 
class Trie: 
    def __init__(self): 
        self.root = TrieNode("root", False, None)
        self.num_words = 0
    
    def __repr__(self): 
        return "Trie: %s words" % (self.num_words)

    # String -> Void 
    # Loads all words in filename into the Trie 
    def load(self, filename): 
        valid_words_file = open(filename, 'r')
        #temp = self.num_words
        for line in valid_words_file: 
            word = line.strip().upper()
            self.add_word(word)
        #num_loaded = self.num_words - temp
        #print("Words Loaded: %s \nTotal Words: %s" %(num_loaded, self.num_words))
        valid_words_file.close()
     
    # String -> Void
    # Adds a single word to the Trie 
    # If the word is already in the Trie, doesn't change anything 
    def add_word(self, word): 
        curr_trie_node = self.root
        for i in range(0, len(word)): 
            character = word[i]
            if character not in curr_trie_node.children: 
                character_node = None 
                if i == len(word)-1: 
                    # End of word, set node as a complete word 
                    character_node = TrieNode(character, True, curr_trie_node)
                    self.num_words += 1
                else: 
                    # Not at end of word, just add node 
                    character_node = TrieNode(character, False, curr_trie_node)
                curr_trie_node.children[character] = character_node
                curr_trie_node = character_node
            else: 
                if i == len(word)-1: 
                    # Letter already in trie, but full word, set as complete word 
                    curr_trie_node.children[character].is_complete_word = True
                else: 
                    # Not full word, and already in Trie, move to it's children 
                    curr_trie_node = curr_trie_node.children[character]
    # Trie Node -> Void 
    # Prunes Trie until curr_node has no children, or we ar eat the root 
    def prune(self, curr_node):
        child_node = curr_node
        parent_node = child_node.parent
        while parent_node and len(child_node.children) == 0:
            del parent_node.children[child_node.letter]
            child_node = parent_node
            parent_node = parent_node.parent
        
    

