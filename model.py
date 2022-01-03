import os
os.system("clear")

class Board():
    def __init__(self):
        self.cells = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


    def display(self):
        print(" %s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3]))
        print("-----------")
        print(" %s | %s | %s " %(self.cells[4], self.cells[5], self.cells[6]))
        print("-----------")
        print(" %s | %s | %s " %(self.cells[7], self.cells[8], self.cells[9]))


    def update_cell(cell_no, mark):
        board.cells[cell_no] = mark
        board.display()       
        
board = Board()


class Player():
    def __init__(self, name, mark, score = 0):
        self.name = name
        self.score = score
        self.mark = mark


player1 = Player(input("What is your name, Player 1 ?\n"), mark = "X")
player2 = Player(input("What is your name, Player 2 ?\n"), mark = "O")
print(player1.name + " VS " + player2.name + "! FIGHT !!!!")
# print(player1.name + "'s" " score is " + str(player1.score) + " while " + player2.name + "'s score is " + str(player2.score))


class Game():

    def __init__(self):
        self.turn = 0

    def turn_player1():
        cell_no = int(input(player1.mark + ") " + player1.name + " ,please choose between 1-9\n"))
        if board.cells[cell_no] != "X" and board.cells[cell_no] != "O":
            Board.update_cell(cell_no, player1.mark)
        else:
            print("Someone already played here ! Choose another cell")
            return Game.turn_player1()
        game.turn += 1


    def turn_player2():
        cell_no = int(input(player2.mark + ") " + player2.name + " ,please choose between 1-9\n"))
        if board.cells[cell_no] != "X" and board.cells[cell_no] != "O":
            Board.update_cell(cell_no, player2.mark)
        else:
            print("Someone already played here ! Choose another cell")
            return Game.turn_player2()
        game.turn += 1
        
    def victory():
        if (board.cells[1] == player1.mark and board.cells[2] == player1.mark and board.cells[3] == player1.mark):
            return (True, player1)
        if (board.cells[1] == player2.mark and board.cells[2] == player2.mark and board.cells[3] == player2.mark):
            return (True, player2)
        if (board.cells[4] == player1.mark and board.cells[5] == player1.mark and board.cells[6] == player1.mark):
            return (True, player1)
        if (board.cells[4] == player2.mark and board.cells[5] == player2.mark and board.cells[6] == player2.mark):
            return (True, player2)
        if (board.cells[7] == player1.mark and board.cells[8] == player1.mark and board.cells[9] == player1.mark):
            return (True, player1)
        if (board.cells[7] == player2.mark and board.cells[8] == player2.mark and board.cells[9] == player2.mark):
            return (True, player2)
        if (board.cells[1] == player1.mark and board.cells[4] == player1.mark and board.cells[7] == player1.mark):
            return (True, player1)
        if (board.cells[1] == player2.mark and board.cells[4] == player2.mark and board.cells[7] == player2.mark):
            return (True, player2)
        if (board.cells[2] == player1.mark and board.cells[5] == player1.mark and board.cells[8] == player1.mark):
            return (True, player1)
        if (board.cells[2] == player2.mark and board.cells[5] == player2.mark and board.cells[8] == player2.mark):
            return (True, player2)
        if (board.cells[3] == player1.mark and board.cells[6] == player1.mark and board.cells[9] == player1.mark):
            return (True, player1)
        if (board.cells[3] == player2.mark and board.cells[6] == player2.mark and board.cells[9] == player2.mark):
            return (True, player2)
        if (board.cells[1] == player1.mark and board.cells[5] == player1.mark and board.cells[9] == player1.mark):
            return (True, player1)
        if (board.cells[1] == player2.mark and board.cells[5] == player2.mark and board.cells[9] == player2.mark):
            return (True, player2)
        if (board.cells[3] == player1.mark and board.cells[5] == player1.mark and board.cells[7] == player1.mark):
            return (True, player1)
        if (board.cells[3] == player2.mark and board.cells[5] == player2.mark and board.cells[7] == player2.mark):
            return (True, player2)
        if (game.turn > 1 and board.cells[1] != "1" and board.cells[2] != "2" and board.cells[3] != "3" and board.cells[4] != "4" and board.cells[5] != "5" and board.cells[6] != "6" and board.cells[7] != "7" and board.cells[8] != "8" and board.cells[9] != "9" ):
            return (True, "No one wins")
        else:
            return False
    
game = Game()

board.display()

while Game.victory() == False:
    Game.turn_player1()
    if Game.victory() == False:
        Game.turn_player2()

winner = Game.victory()[1]
if isinstance(winner, str):
    print("Egalité !")
else:
    print(winner.name + " a gagné la partie !")