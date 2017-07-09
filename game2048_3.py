##2048 class.

import random

class game2048:
    def __init__(self):
        self.board = [[0 for i in range(4)] for i in range(4)]
        a = random.choice([0,1,2,3])
        b = random.choice([0,1,2,3])
        c = random.choice([0,1,2,3])
        d = random.choice([0,1,2,3])
        # To choose two units randomly as the initial board.
        # But we need to avoid duplicate units:
        while a == c and b == d:
            d = random.choice([0,1,2,3])
        # Give these two units value 2.
        self.board[a][b] = 2
        self.board[c][d] = 2
        # Initialize the score the player have.
        self.score = 0
        # To produce a useful var.
        self.lst = []

    # This method belongs to moveUnits, used to move all the units in a certain direction.
    def move(self,lst):
        temp = []
        for i in [0,1,2,3]:
            if lst[i] != 0:
                temp.append(lst[i])
            else:
                continue
        n = 4 - len(temp)
        for i in range(n):
            temp.append(0)
        lst = temp
        return lst

    # This method belongs to moveUnits, used to add the units available.
    def plus(self,lst):
        for i in range(3):
            if lst[i] ==lst[i+1]:
                lst[i],lst[i+1] = lst[i]+lst[i+1],0
                self.score += lst[i]
            else:
                lst = lst
        return lst

    # The core of the whole program:
    def moveUnits(self,direction):
        if direction == "upwards":
            for i in range(4):
                # It is used to record:
                self.lst = []
                # To copy a piece of information in self.board.
                for j in range(4):
                    self.lst.append(self.board[j][i])
                # Move-Add-Move model is our solution to inplement the unique movement of game 2048.
                self.lst = self.move(self.lst)
                self.lst = self.plus(self.lst)
                self.lst = self.move(self.lst)
                # Update the self.board is the goal of this method.
                for j in range(4):
                    self.board[j][i] = self.lst[j]
        # The same as the first one.
        elif direction == "downwards":
            for i in range(4):
                self.lst = []
                for j in range(4):
                    self.lst.append(self.board[3-j][i])
                self.lst = self.move(self.lst)
                self.lst = self.plus(self.lst)
                self.lst = self.move(self.lst)
                for j in range(4):
                    self.board[3-j][i] = self.lst[j]
        # The same as the first one.
        elif direction == "leftwards":
            for i in range(4):
                self.lst = []
                for j in range(4):
                    self.lst.append(self.board[i][j])
                self.lst = self.move(self.lst)
                self.lst = self.plus(self.lst)
                self.lst = self.move(self.lst)
                for j in range(4):
                    self.board[i][j] = self.lst[j]
        # The same as the first one.
        elif direction == "rightwards":
            for i in range(4):
                self.lst = []
                for j in range(4):
                    self.lst.append(self.board[i][3-j])
                self.lst = self.move(self.lst)
                self.lst = self.plus(self.lst)
                self.lst = self.move(self.lst)
                for j in range(4):
                    self.board[i][3-j] = self.lst[j]
        # To achieve a better rubustment:
        else:
            print "==========================RECLICK,PLEASE==========================="

    # Used to produce a new unit with value 2.                
    def newUnit(self):
        tempa = []
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 0:
                    tempa.append([i,j])
                else:
                    continue
        tempb = random.choice(tempa)
        self.board[tempb[0]][tempb[1]] = 2
        
    def judgeBool(self):
        temp = []
        #  To add up the differences of the neighbours in order to judge whether the game is available for the next round.
        #  But if there's a unit with a value 0, we can save time by this:
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 0:
                    return True
                else:
                    continue
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != self.board[i][j+1] and self.board[i][j] != self.board[i+1][j]:
                    a.append('False')
                else:
                    continue
        for j in range(3):
                i = 3
                if self.board[i][j] != self.board[i][j+1]:
                    a.append('False')
        for i in range(3):
                j = 3
                if self.board[i][j] != self.board[i+1][j]:
                    a.append('False')
        if temp.count('False') == 15:
            return False
        else:
            return True
    
    # some useful interfaces:
    def updateTtlScore(self):
        return self.score
    
    def getNumber(self,a,b):
        return self.board[a][b]

    def getBoard(self):
        return self.board
    
    def if2048(self):
        # This method is used to judge if there's a change in the board.
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 2048:
                    return True
        return False    
