#Name: Monica Nguyen 
#Date: Dec 6, 2019
#Usage: python tictactoe.py <rows> <cols> <difficulty> <piece> <optional -h hint -a advanced hint>
#Board to allow tic tac toe game to run. The board is up to 5x5. Difficulty is up to 5. The piece can either be X or O. 
#For example the command line would be: python tictactoe.py 3 3 1 X -h

#Constants for piece types
EMPTY = 0
X = 1
O = 2

#Using this class to focus on Object Oriented Programming
class Board:
    board = None

#Purpose: Creates the board with two-dimensional list with indictated number of rows and columns and filling with EMPTY. 
#Parameters: self, integer parameters of rows and cols have a default of 3 if there is a lack of user input 
#Returns: None
    def __init__(self, rows=3, cols=3): #The constructor: initializes class or object instance
        self.board = [[EMPTY for col in range(cols)] for row in range(rows)] #creates rows x column array of list of lists
        
#Purpose: Determine the number of rows for playing. 
#Parameters: self
#Returns: Number of rows in the board from len(self.board)
    def rows(self):
        return len(self.board) #number of lists in the list represents the rows

#Purpose: Determine the number of columns for playing. 
#Parameters: self
#Returns: Number of columns in the board from len(self.board[0])  
    def cols(self): 
        return len(self.board[0]) #0th position in each list represents the columns

#Purpose: Checks if the game board location is open to allow for assignment of a game piece. 
#Parameters: self, row, col 
#Returns: Returns true if there is an empty non-played space. Returns false if the space is already occupied. 
    def canPlay(self, row, col):
        if self.board[row][col]== EMPTY: #Not yet played space. 
            return True
        else: 
            return False #The space is already occupied. Cannot play there again. 

#Purpose: Places the player's piece into the specified row and column location. 
#Parameters: self, row, col, piece
#Returns: None   
    def play(self, row, col, piece):
        self.board[row][col] = piece

#Purpose: To check if there are empty locations remaining. This is important to be able to stop the game and help identify winners.
#Parameters: self
#Returns: Returns true if there are no empty locations on the board. Returns false if there are empty locations on the board. Any non-empty location returns false. 
    def full(self):
        for row in self.board:
            for col in row:            
                if col == EMPTY:
                    return False
        return True

#Purpose: To determine if there are 3 consecutive pieces of one kind in a row. 
#Parameters: self,whatrowtolook, piecetype
#Returns: Returns true if there are 3 consecutive pieces of one kind in a row. Otherwise, the game returns false as there are not three consecutive of one kind yet
    def winInRow(self,whatrowtolook, piecetype):
        a_row = self.board[whatrowtolook]
        i = 0
        while i < len(a_row)-2: #i is the index of the 'start' of the 3 in a row and was told in tutorial this is an acceptable variable!! -2 index because this confines to the box where the winning rows start 
            if a_row[i] == piecetype and a_row[i+1] == piecetype and a_row[i+2] == piecetype: #checks to see if i, i+1, i+2 (consecutive positions) are all the same piece type 
                return True
            i+=1 #loop through the different positions by adding 1 
        return False

#Purpose: To determine if there are 3 consecutive pieces of one kind in a column.
#Parameters: self,whatcoltolook,piecetype
#Returns: Returns true if there are 3 consecutive pieces of one kind in a column. Otherwise, the game returns false as there are not three consecutive of one kind yet.
    def winInCol(self,whatcoltolook,piecetype):
        for i in range(0,len(self.board)-2): #i is the index of the 'start' of the 3 in a column, -2 index because this confines to the box where the 3 consecutive in a column start 
            if(self.board[i][whatcoltolook] == piecetype and self.board[i+1][whatcoltolook] == piecetype and self.board[i+2][whatcoltolook] == piecetype ):
                return True
        return False

#Purpose: To determine if there are three consecutive pieces of one kind in the forward slash or backward slash directions. 
#Parameters: self, piecetype
#Returns: Returns true if there are 3 consecutive pieces of one kind in a row in the forward slash and backward slash directions. Otherwise, the game returns false as there are not three consecutive of one kind yet. 
    def winInDiag(self,piecetype):
        for i in range(0, len(self.board)-2): #checking forward slash for 3 consecutive 
            for j in range(0,len(self.board[0])-2): #-2 index because this confines to the box where the 3 consecutive pieces can start 
                if(self.board[i][j] == piecetype and self.board[i+1][j+1] == piecetype and self.board[i+2][j+2] == piecetype ): 
                    return True
        for i in range(0,len(self.board)-2): #checking backward slash for 3 consecutive  
            for j in range(len(self.board[0])-2,len(self.board[0])): #-2 index because this confines to the box where the 3 consecutive pieces can start 
                if(self.board[i][j] == piecetype and self.board[i+1][j-1] == piecetype and self.board[i+2][j-2] == piecetype ): 
                    return True
        return False

        
#Purpose: To indicate the player who has got three pieces in a row has won the game. 
#Parameters: self, piece
#Returns: Returns True when there is a win in a row, column or diagonal. Otherwise, if there are no wins it returns false. 
    def won(self, piece):
        for row in range (0,len(self.board)):
            if (self.winInRow(row,piece)): #row wins 
                return True
        for column in range(0,len(self.board[0])):
            if (self.winInCol(column,piece)): #column wins 
                return True
        if (self.winInDiag(piece)): #diagonal wins 
            return True
        return False

#Purpose: Upon using -h as a system argument, then the tic tac toe board will suggest a strategic place for the player to place a piece.
#Parameters: self, piece
#Returns: -1, -1 as a default which indicates there is no hint.
    def hint(self, piece):             
        for row in range(len(self.board)):
        	for col in range(len(self.board[0])):
        		if self.canPlay(row,col):
        			self.play(row,col,piece)
        			if self.won(piece):
        				self.play(row,col,EMPTY) 
        				return row, col
        			else: 
        				self.play(row,col,EMPTY)         
        return -1, -1 #Returns this to indicate there is no hint jk
 
#Purpose: To end the game if X wins, O wins or if the board is full. 
#Parameters: self
#Returns: Returns true if one of these conditions are met: X wins, 0 wins, or the board is full. Otherwise, false is returned.
    def gameover(self):
        if self.won(X) or self.won(O) or self.full():
            return True
        return False



