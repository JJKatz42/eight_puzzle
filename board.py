#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: 
# email:
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[0] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        for r in range(3):
            for c in range(3):
                self.tiles[r][c] = int(digitstr[r*3 + c])
                if self.tiles[r][c] == 0:
                    self.blank_r = r
                    self.blank_c = c


    ### Add your other method definitions below. ###

    def __repr__(self):
        """ returns a string representation of a Board object.
        """
        s = ''
        for r in range(3):
            for c in range(3):
                if self.tiles[r][c] == 0:
                    s += '_ '
                else:
                    s += str(self.tiles[r][c]) + ' '
            s += '\n'
        return s
    
    def move_blank(self, direction):
        """ takes as input a string direction that specifies the direction 
            in which the blank should move, and that attempts to modify 
            the contents of the called Board object accordingly
            input: a string direction that specifies the direction in 
            which the blank should move
        """
        if direction != 'up' and direction != 'down' and direction != 'left' and direction != 'right':
            print("unknown direction:", direction)
            return False
        new_blank = 0
        if direction == 'up':
            if self.blank_r - 1 < 0:
                return False
            else:
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r - 1][self.blank_c]
                self.tiles[self.blank_r - 1][self.blank_c] = 0
                self.blank_r -= 1
                return True
        if direction == 'down':
            if self.blank_r + 1 > 2:
                return False
            else:
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r + 1][self.blank_c]
                self.tiles[self.blank_r + 1][self.blank_c] = 0
                self.blank_r += 1
                return True
        if direction == 'left':
            if self.blank_c - 1 < 0:
                return False
            else:
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r][self.blank_c - 1]
                self.tiles[self.blank_r][self.blank_c - 1] = 0
                self.blank_c -= 1
                return True
        if direction == 'right':
            if self.blank_c + 1 > 2:
                return False
            else:
                self.tiles[self.blank_r][self.blank_c] = self.tiles[self.blank_r][self.blank_c + 1]
                self.tiles[self.blank_r][self.blank_c + 1] = 0
                self.blank_c += 1
                return True

    def digit_string(self):
        """ creates and returns a string of digits that corresponds to the 
            current contents of the called Board object’s tiles attribute
        """
        n_digitstr = ''
        for r in range(3):
            for c in range(3):
                n_digitstr += str(self.tiles[r][c])
        return n_digitstr

    def copy(self):
        """ returns a newly-constructed Board object that is a deep copy 
            of the called object
        """
        c_board = Board(self.digit_string())
        return c_board

    def num_misplaced(self):
        """ counts and returns the number of tiles in the called Board 
            object that are not where they should be in the goal state
        """
        num_displaced = 0
        goal_state = '012345678'
        current_state = self.digit_string()
        for i in range(len(current_state)):
            if current_state[i] == '0':
                None
            elif current_state[i] != goal_state[i]:
                num_displaced += 1

        return num_displaced

    def __eq__(self, other):
        """ The method should return True if the called object (self) 
            and the argument (other) have the same values for the tiles 
            attribute, and False otherwise
            input: other is a Board object
        """
        if self.tiles == other.tiles:
            return True
        return False

if __name__ == '__main__':
    b = Board('142358607')
    print(b)
    print(b.num_misplaced())



            

        

