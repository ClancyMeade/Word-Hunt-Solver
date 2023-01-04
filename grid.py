# File creates a WordHunt Grid (Grid is a Matrix of Cells )

NUM_ROWS = 4
NUM_COLS = 4

# Represents a single cell in a grid 
# Cell has a character and location in grid 
class Cell: 
    def __init__(self, character, row, col): 
        self.character = character 
        self.row = row
        self.col = col 
    
    def __repr__(self): 
        return "Cell: (%s, row: %s, col %s)" % (self.character, self.row, self.col)

    def __eq__(self, other): 
        return type(other) == Cell and \
            self.character == other.character and \
                self.row == other.row and \
                    self.col == other.col 

    def __hash__(self): 
        return hash((self.character, self.row, self.col))

# Represents a matrix of characters with size (NUM_ROWS * NUM_COLS)
# Grid is a Graph (adjacency list implementation) of Cells
class Grid: 
    def __init__(self): 
        self.cells = [[0 for c in range(NUM_COLS)] for r in range(NUM_ROWS)] # Matrix of Cell objects 
        self.characters = ""

    # Loads characters from stdin into Grid in upper case
    def load(self): 
        all_chars = input("Input Grid: ").upper()
        if(len(all_chars) < (NUM_ROWS * NUM_COLS)): 
            print("Invalid grid, must have %s characters." % (NUM_ROWS * NUM_COLS))
            exit(-1)
        self.characters = all_chars
        k = 0
        # Fill Grid Matrix with Cell objects 
        for i in range(0, NUM_ROWS): 
            for j in range(0, NUM_COLS): 
                curr_char = all_chars[k]
                curr_cell = Cell(curr_char, i, j)
                self.cells[i][j] = curr_cell
                k += 1
    
    # Cell -> List of Cells 
    # Returns a list of all neighboring cells of Cell c 
    def get_neighbors(self, c): 
        neighbors = []
        for i in range(c.row-1, c.row+2): 
            for j in range(c.col-1, c.col+2): 
                if (i >= 0 and i < NUM_ROWS) and (j >= 0 and j < NUM_COLS): 
                    if not (i == c.row and j == c.col): 
                        neighbor_cell = self.cells[i][j]
                        neighbors.append(neighbor_cell)
        return neighbors

    # Cell, Cell -> Boolean 
    # Checks if cell2 can be reached from cell1 on the Grid 
    def within_range(self, cell1, cell2): 
        if(cell1 == cell2): 
            return False 
        if abs(cell1.row - cell2.row) <=1 and \
            abs(cell1.col - cell2.col) <= 1: 
            return True 
        return False 