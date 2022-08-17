import sys
import pygame


class Connect4:
    def __init__(self, board):
        self.board = board
        self.ls4 = []
        self.turn = 0
        self.columns = 7
        self.rows = 6
        self.gameover = False
        self.gray = (169, 169, 169)
        self.sector = 100
        self.radius = int(self.sector / 2 - 5)
        self.width = 7 * self.sector
        self.height = (6 + 1) * self.sector
        self.dimensions = (self.width, self.height)
        self.monitor = pygame.display.set_mode(self.dimensions)

    def graphicalboard(self, col, ro):
        # initializes pygame
        pygame.init()
        # size in pixels of the circle?
        self.sector = 100
        # draws the board and the slots
        for v in range(7):
            for w in range(6):
                pygame.draw.rect(self.monitor, self.ls4[0],
                                 (v * self.sector, w * self.sector + self.sector, self.sector, self.sector))
                pygame.draw.circle(self.monitor, self.gray, (int(v * self.sector + self.sector / 2), int(w * self.sector + self.sector + self.sector / 2)), self.radius)
        # places the pieces in the board
        # columns
        for c in range(7):
            # rows
            for w in range(6):
                # if this position on the board contains an x or an o
                if self.board[w][c] == "x":
                    pygame.draw.circle(self.monitor, self.ls4[1], (int(c * self.sector + self.sector / 2), self.height - int((5 - w) * self.sector + self.sector / 2)), self.radius)
                elif self.board[w][c] == "o":
                    pygame.draw.circle(self.monitor, self.ls4[2], (int(c * self.sector + self.sector / 2), self.height - int((5 - w) * self.sector + self.sector / 2)), self.radius)
        pygame.display.update()

    # applies the users' board and player colors
    def color(self, pboard, player1, player2):
        orange = (255, 97, 3)
        green = (127, 255, 0)
        white = (240, 255, 255)
        pink = (219, 62, 177)
        black = (3, 3, 3)
        blue = (77, 77, 255)
        red = (210, 39, 48)
        ls = ["orange", "green", "white", "pink", "black", "blue", "red"]
        ls2 = [[orange], [green], [white], [pink], [black], [blue], [red]]
        ls3 = [pboard, player1, player2]
        # matches the users selected color, with the rgb value

        for o in range(len(ls3)):
            for k in range(len(ls)):
                if ls3[o] == ls[k]:
                    o += 1
                    self.ls4 += ls2[k]
                    break

        return self.ls4

    # determines whether the game is over
    def GameOver(self):
        style = pygame.font.SysFont("monospace", 75)
        for e in range(self.rows):
            for f in range(self.columns - 3):

                # checks for horizontal wins
                if self.board[e][f] == 'x' and self.board[e][f + 1] == 'x' and self.board[e][f + 2] == 'x' and self.board[e][f + 3] == 'x':
                    label = style.render("Player 1 wins!!", True, self.ls4[1])
                    self.monitor.blit(label, (40, 10))
                    self.gameover = True
                elif self.board[e][f] == 'o' and self.board[e][f + 1] == 'o' and self.board[e][f + 2] == '0' and self.board[e][f + 3] == 'o':
                    label = style.render("Player 2 wins!!", True, self.ls4[2])
                    self.monitor.blit(label, (40, 10))
                    self.gameover = True

            # checks for vertical wins
        for f in range(self.columns):
            for e in range(self.rows - 3):
                if self.board[e][f] == 'o' and self.board[e + 1][f] == 'o' and self.board[e + 2][f] == 'o' and self.board[e + 3][f] == 'o':
                    label = style.render("Player 2 wins!!", True, self.ls4[2])
                    self.monitor.blit(label, (40, 10))
                    self.gameover = True
                elif self.board[e][f] == 'x' and self.board[e + 1][f] == 'x' and self.board[e + 2][f] == 'x' and self.board[e + 3][f] == 'x':
                    label = style.render("Player 1 wins!!", True, self.ls4[1])
                    self.monitor.blit(label, (40, 10))
                    self.gameover = True
        # checks for negatively sloped diagonal wins
        for f in range(self.columns - 3):
            for e in range(self.rows - 3):
                if self.board[e][f] == 'x' and self.board[e + 1][f + 1] == 'x' and self.board[e + 2][f + 2] == 'x' and \
                        self.board[e + 3][f + 3] == 'x':
                    label = style.render("Player 1 wins!!", True, self.ls4[1])
                    self.monitor.blit(label, (40, 10))
                    self.gameover = True
                elif self.board[e][f] == 'o' and self.board[e + 1][f + 1] == 'o' and self.board[e + 2][f + 2] == 'o' and \
                        self.board[e + 3][f + 3] == 'o':
                    label = style.render("Player 2 wins!!", True, self.ls4[2])
                    self.monitor.blit(label, (40, 10))
                    self.gameover = True

            # Checks for positively sloped diagonal wins
        for c in range(self.columns - 3):
            for r in range(5, -1, -1):
                if self.board[r][c] == "x" and self.board[r - 1][c + 1] == "x" and self.board[r - 2][c + 2] == "x" and \
                        self.board[r - 3][c + 3] == "x":
                    label = style.render("Player 1 wins!!", True, self.ls4[1])
                    self.monitor.blit(label, (40, 10))
                    self.gameover = True
                elif self.board[r][c] == "o" and self.board[r - 1][c + 1] == "o" and self.board[r - 2][c + 2] == "o" and \
                        self.board[r - 3][c + 3] == "o":
                    label = style.render("Player 2 wins!!", True, self.ls4[2])
                    self.monitor.blit(label, (40, 10))
                    self.gameover = True

        return self.gameover

    # makes moves, based on user input
    def makemove(self, filledrows2):

        player1 = 'x'
        player2 = 'o'

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # creates the circle that hovers above top row, when user has not clicked the mouse
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(self.monitor, self.ls4[0], (0, 0, self.width, self.sector))
                position = event.pos[0]
                if self.turn == 0:
                    pygame.draw.circle(self.monitor, self.ls4[1], (position, int(self.sector / 2)), self.radius)
                else:
                    pygame.draw.circle(self.monitor, self.ls4[2], (position, int(self.sector / 2)), self.radius)
            # updates the board based on user input
            pygame.display.update()
            # makes move when user presses the button down
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(self.monitor, self.ls4[0], (0, 0, self.width, self.sector))
                # Asks for Player 1's input
                if self.turn == 0:
                    # gets the position of the users mouse
                    position = event.pos[0]
                    # specifically gets the column the users mouse is in
                    col = int(position / self.sector)

                    row1 = filledrows2[col]
                    # checks for column overflow
                    if 6 - row1 - 1 < 0:
                        yu = 8
                    else:
                        self.board[6 - row1 - 1][col] = player1
                        # ensures that the users piece goes where it should
                        filledrows2[col] = filledrows2[col] + 1
                    # makes it player 2's turn
                    self.turn = 1
                # Ask for Player 2 Input
                else:
                    # gets the position of the users mouse
                    position = event.pos[0]
                    # specifically gets the column the users mouse is in
                    col = int(position / self.sector)
                    row1 = filledrows2[col]
                    # checks for column overflow
                    if 6 - row1 - 1 < 0:
                        yu = 8
                    else:
                        self.board[6 - row1 - 1][col] = player2

                    # shows where the next piece will go
                    filledrows2[col] = filledrows2[col] + 1
                    # makes it player 1's turn
                    self.turn = 0
    # turn 0 = player 1


if __name__ == '__main__':
    # a visual representation of the board
    a = ([['-', '-', '-', '-', '-', '-', '-'],  # row 0
          ['-', '-', '-', '-', '-', '-', '-'],  # row 1
          ['-', '-', '-', '-', '-', '-', '-'],  # row 2
          ['-', '-', '-', '-', '-', '-', '-'],  # row 3
          ['-', '-', '-', '-', '-', '-', '-'],  # row 4
          ['-', '-', '-', '-', '-', '-', '-']])  # row 5

    # row you can't place a spot it
    filledrows = [0, 0, 0, 0, 0, 0, 0]
    column = 7
    row = 6
    # create an object
    c1 = Connect4(a)
    # print(x)
    # here ask the user about the color of the board and pieces
    z = 0
    ls7 = ["orange", "green", "white", "pink", "black", "blue", "red"]
    while z == 0:
        print("Welcome to Connect 4 with a twist!")
        print("For this game you will have a power up that will allow you to pop out one of your own pieces.")
        print("To drop a piece click the row above the board in the column you want the piece at.")
        print("To pop a piece click, click the bottom row of the column where you want to pop the piece.")
        boardcolor = input("What color board would you like (orange, white, pink, black, red, blue, green): ")
        player1color = input("What color piece for player 1 would you like: ")
        player2color = input("What color piece for player 2 would you like?: ")
        newls = [boardcolor, player1color, player2color]
        # makes sure the user doesn't choose the same color twice and types in a correct color
        if boardcolor != player1color and player1color != player2color and player2color != boardcolor:
            # if color selection is valid, we send the user colors to the color method
            c1.color(boardcolor, player1color, player2color)
            z += 1
            if z == 1:
                p = 0
                for i in range(len(newls)):
                    for j in range(len(ls7)):
                        if newls[i] == ls7[j]:
                            p += 1
                if p < 3:
                    z = 0
                    print("Please type your colors in correctly. Try again please!")
                else:
                    z = 1
        # will repeat until the user enters valid input
        else:
            print("Please do not select the same color more than once. Try again please!")

    # keeps the game going until someone has won
    while not c1.gameover:
        c1.graphicalboard(column, row)
        c1.makemove(filledrows)
        c1.graphicalboard(column, row)
        c1.GameOver()
        if c1.gameover:
            pygame.display.update()
            pygame.time.wait(5000)
