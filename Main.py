import ChessEngine as ce
import chess as ch

class Main:
    def __init__(self, board = ch.Board):
        self.board = board

    #Player Move
    def playerMove(self):
        try:
            print(self.board.legal_moves)
            print("""To undo your last move, type "undo".""")
            play = input("Your move: ").lower()
            if (play == "undo"):
                self.board.pop()
                self.board.pop()
                self.playerMove()
                return
            self.board.push_san(play)
        except:
            self.playerMove()
    
    #Engine's Move
    def engineMove(self, maxDepth, color):
        engine = ch.Engine(self.board, maxDepth, color)
        self.board.push(engine.getBestMove())
    
    def startGame(self):
        #Allocate Color's
        color = None
        while (color != "b" or color != "w"):
            color = (input("""Play as (type "b" for black or "w" for white): """))[0].lower()

        maxDepth = None
        while (isinstance (maxDepth, int) == false):
            maxDepth = int(input("Choose Depth: "))
        
        #If player chooses black, engine plays first
        if color == "b":
            while(self.boar.is_checmate()== False):
                print("The engine is thinking....")
                self.engineMove(maxDepth, ch.WHITE)
                print(self.board)
                self.playerMove()
                print(self.board)
            print(self.board())
            print(self.board.outcome())
        
        #If player chooses white, he plays first
        elif color == "w":
            while(self.boar.is_checmate()== False):
                print(self.board)
                self.playerMove()
                print(self.board)
                print("The engine is thinking....")
                self.engineMove(maxDepth, ch.BLACK)
               
            print(self.board())
            print(self.board.outcome())
        
        #Reset the board once there is a checkmate
        self.board.reset
        #Start another game
        self.startGame()

#Create an instance and start the game
newBoard = ch.Board()
game = Main(newBoard)
game.startGame()
                