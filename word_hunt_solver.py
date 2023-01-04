# Program: word_hunt_solver: 
#   Finds valid words in a 4*4 grid of letters 
#   Returns list of all valid words 

from trie import * 
from grid import * 

NUM_ROWS = 4
NUM_COLS = 4

class WordHuntSolver: 
    def __init__(self):
        self.grid = Grid()
        self.valid_words = Trie()
        self.words_found = set([])
        self.paths = {}
    
    # Finds all words in Grid using Trie of valid words 
    # Places words found in array 
    def find_words(self): 
        for i in range(NUM_ROWS): 
            for j in range(NUM_COLS): 
                curr_cell = self.grid.cells[i][j]
                if curr_cell.character in self.valid_words.root.children:
                    curr_word = curr_cell.character
                    curr_node = self.valid_words.root.children[curr_cell.character]
                    cells_used = []
                    cells_used.append(curr_cell)
                    self.find_words_helper(curr_node, curr_cell, curr_word, cells_used)
    
    # TrieNode, Cell, String -> Void (Adds words to words_found)
    # Recursively finds valid words from curr_node in Trie
    # Builds words from paths in Trie according to chars in Grid 
    def find_words_helper(self, curr_node, curr_cell, curr_word, cells_used):
        if curr_node.is_complete_word == True:
            self.words_found.add(curr_word)
            self.paths[curr_word] = cells_used
        if curr_node.is_complete_word == True: 
            self.words_found.add(curr_word)
            self.valid_words.prune(curr_node)
        for neighbor_cell in self.grid.get_neighbors(curr_cell): 
            if (neighbor_cell.character in curr_node.children) and (neighbor_cell not in cells_used): 
                child_node = curr_node.children[neighbor_cell.character] 
                new_used = cells_used + [neighbor_cell] 
                self.find_words_helper(child_node, neighbor_cell, curr_word + neighbor_cell.character, new_used)

def main():
    solver = WordHuntSolver() 
    # Load valid words 
    solver.valid_words.load("valid_words.txt") 
    # Load grid 
    solver.grid.load()
    # Find valid words  
    solver.find_words()
    #print(solver.words_found)
    result = list(filter(lambda x: len(x) > 2, solver.words_found))
    my_list = sorted(result, key=lambda x: (-len(x),x))
    for word in my_list: 
        print(word)
        #coord = (solver.paths[word][0].row, solver.paths[word][0].col)
        #print(coord)
 

if __name__ == "__main__":
    main()

    # TO DO !!!!!
    # add Trie pruning to improve speed 