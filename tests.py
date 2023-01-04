import unittest
from unittest.mock import patch 
from trie import * 
from grid import * 

class TestWordHunt(unittest.TestCase): 
    def test_trie_addword_01(self): 
        my_trie = Trie()
        self.assertEqual(my_trie.num_words, 0) 
        my_trie.add_word("CAT")
        self.assertEqual(my_trie.num_words, 1)
        my_trie.add_word("CAT")
        self.assertEqual(my_trie.num_words, 1)
        my_trie.add_word("CATS")
        self.assertEqual(my_trie.num_words, 2)
        self.assertFalse(my_trie.root.children["C"].children["A"].is_complete_word)
        self.assertTrue(my_trie.root.children["C"].children["A"].children["T"].is_complete_word)
        self.assertTrue(my_trie.root.children["C"].children["A"].children["T"].children["S"].is_complete_word) 
        my_trie.add_word("CATS")
        my_trie.add_word("CAT")
        self.assertEqual(my_trie.num_words, 2)
    
    def test_trie_load_01(self): 
        my_trie = Trie()
        my_trie.load("testfile.txt")
        self.assertEqual(my_trie.num_words, 6)
        my_trie.load("testfile.txt")
        self.assertEqual(my_trie.num_words, 6)
    
    def test_trie_load_02(self): 
        my_trie = Trie()
        self.assertEqual(my_trie.root.children, {})
        my_trie.load("valid_words.txt")
        self.assertEqual(my_trie.num_words, 279496)
    
    @patch('builtins.input', return_value="abcdefghijklmnop")
    def test_grid_load(self, mock_inputs): 
        my_grid = Grid()
        my_grid.load()
        self.assertEqual(my_grid.characters, "ABCDEFGHIJKLMNOP")
        self.assertTrue(my_grid.cells["A"].row == 0 and my_grid.cells["A"].col == 0)
        self.assertTrue(my_grid.cells["K"].row == 2 and my_grid.cells["K"].col == 2)

    @patch('builtins.input', return_value="abcdefghijklmnop")
    def test_grid_within_range(self, mock_inputs): 
        my_grid = Grid()
        my_grid.load()
        cell1 = my_grid.cells["A"]
        cell2 = my_grid.cells["B"]
        self.assertTrue(my_grid.within_range(cell1, cell2))
        cell3 = my_grid.cells["F"]
        cell4 = my_grid.cells["P"]
        self.assertFalse(my_grid.within_range(cell3, cell4))
        self.assertTrue(my_grid.within_range(cell1, cell3))
        self.assertTrue(my_grid.within_range(cell2, cell3))
        self.assertFalse(my_grid.within_range(cell1, cell4))

if __name__ == '__main__': 
    unittest.main()

    