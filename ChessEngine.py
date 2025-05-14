import chess as ch

class Engine:

    def __init__(self, board, maxDepth, color):
        self.board = board
        self.maxDepth = maxDepth
        self.color = color

    #If no legal moves, someone has lost
    def checkMate(self):
        if(self.board.legal_moves.count()==0):
            #Engine losing
            if (self.board.turn == self.color):
                return -99999
            else:
                return 99999
        else:
            return 0

    #Takes a square as an input and reutnrs piece value
    def sqaurePoints(self, square):
        pieceValue = 0
        if(self.board.piece_type_at(square) == ch.PAWN):
            pieceValue = 1
        if(self.board.piece_type_at(square) == ch.ROOK):
            pieceValue = 5.1
        if(self.board.piece_type_at(square) == ch.BISHOP):
            pieceValue = 3.33
        if(self.board.piece_type_at(square) == ch.KNIGHT):
            pieceValue = 3.2
        if(self.board.piece_type_at(square) == ch.QUEEN):
            pieceValue = 8.8

    def engine(self, candidate, depth):
        if( depth == self.maxDepth or self.legal_moves.count() == 0):
            return self.evalFunc()
        else:
            #List of moves in current position
            movesList = list(self.board.legal_moves)

            #Initialise newCandidate
            newCandidate = None

            if(depth % 2 != 0):
                newCandidate = float("-inf")
            else:
                newCandidate = float("inf")

            for i in moveList:
                #Play the move i
                self.board.push(i)

                #Get the value of move i
                value = self.engine(newCandidate, depth + 1)

                #Basic algorithm
                #Engine's turn (maximizing)
                if(value > newCandidate and depth % 2 != 0):
                    newCandidate = value
                    if(depth == 1):
                        move = i
                
                #Players turn (minimizing)
                elif(value < newCandidate and depth % 2 == 0):
                    newCandidate = value

                #Alpha Beta pruning cuts
                #if previous move was made by the engine
                if (candidate != None and value < candidate and depth % 2 == 0):
                    self.board.pop()
                    break
                #if previous move was made by the player
                if (candidate != None and value > candidate and depth % 2 != 0):
                    self.board.pop()
                    break
        
        if (depth > 1):
            #Return the value of a node in a tree
            return newCandidate
        else:
            return move

