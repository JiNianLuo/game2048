##The entrance of our game.
##  entrance_2048.py
##    The game 2048 is about moving and adding units, in which only units with identical value can be added.
##      And to win the game, you have to move all the units in four directions named "upwards", "downwards", "leftwards" and "rightwards" until there is no less than one unit with the value 2048.
##        But be careful, if there are no more than one unit available to move or add, the game comes to an end and you lose.

from graphics import *
from game2048_3 import *

def game():
    print "The game 2048 is about moving and adding units, in which only units with identical value can be added."
    print "And to win the game, you have to move all the units in four directions named 'upwards', 'downwards', 'leftwards' and 'rightwards' until there is no less than one unit with the value 2048."
    print "But be careful, if there are no more than one unit available to move or add, the game comes to an end and you lose."
    print "The score will be the sum of added units."
    print "==================================================================="
    # The starting of the program, firstly draw a GUI window.
    board = game2048()
    win = GraphWin("game2048",600,700)
    # The shape of the units.
    num = [[0 for i in range(4)]for i in range (4)]
    Rectangle(Point(260,0),Point(340,80)).draw(win)
    Rectangle(Point(0,260),Point(80,340)).draw(win)
    Rectangle(Point(520,260),Point(600,340)).draw(win)
    Rectangle(Point(260,520),Point(340,600)).draw(win)
    # The buttons of four directions.
    Text(Point(300,40),'upwards').draw(win)
    Text(Point(40,300),'leftwards').draw(win)
    Text(Point(560,300),'rightwards').draw(win)
    Text(Point(300,560),'dowmwards').draw(win)
    # Newest score.
    score = Text(Point(300,650),'SCORE : ' + str(board.updateTtlScore()))
    score.draw(win)
    # Write the values of all the units.
    for i in [1,2,3,4]:
        for j in [1,2,3,4]:
            rec = Rectangle(Point(100*i,100*j),Point(100*i+100,100*j+100))
            rec.draw(win)
            num[i-1][j-1] = Text(Point(100*i+50,100*j+50),board.getNumber(i-1,j-1))
            if board.getNumber(i-1,j-1) != 0:
                num[i-1][j-1].draw(win)
            else:
                continue
    # Now is player's turn: the program will wait for a instruction, click a button accordingly.
    p = win.getMouse()
    x = p.getX()
    y = p.getY()
    judgelose = True
    findchanges = False
    while judgelose == True and findchanges == False:
        if 260<x<340 and y<80:
            # Record previous table.
            pre = [[],[],[],[]]
            for i in range(4):
                for j in range(4):
                    pre[i].append(board.board[i][j])
            # Update the table.
            board.moveUnits("leftwards")
            # To judge if the table has changed already, if yes, we need produce a new unit from the zero-value-units with the value 2; and if not, there'll be no changes.
            if pre != board.getBoard():
                # To call a method to move the units.
                board.newUnit()
            # Update the values of GUI so that it can output the latest value all the time.
            for i in [1,2,3,4]:
                for j in [1,2,3,4]:
                    # Undraw & Draw is a procedure of updating.
                    num[i-1][j-1].undraw()
                    num[i-1][j-1] = Text(Point(100*i+50,100*j+50),board.getNumber(i-1,j-1))
                    # Update the score.
                    score.undraw()
                    score = Text(Point(300,650),board.updateTtlScore())
                    score.draw(win)
                    # Zero-value-units should not be printed out in order not to distract the player.
                    if board.getNumber(i-1,j-1) != 0:
                        num[i-1][j-1].draw(win)
                    else:
                        continue
        # The same as the first condition.
        elif 260<x<340 and 520<y<600:
            pre = [[],[],[],[]]
            for i in range(4):
                for j in range(4):
                    pre[i].append(board.board[i][j])
            board.moveUnits("rightwards")
            if pre != board.getBoard():
                board.newUnit()
            for i in [1,2,3,4]:
                for j in [1,2,3,4]:
                    num[i-1][j-1].undraw()
                    num[i-1][j-1] = Text(Point(100*i+50,100*j+50),board.getNumber(i-1,j-1))
                    score.undraw()
                    score = Text(Point(300,650),board.updateTtlScore())
                    score.draw(win) 
                    if board.getNumber(i-1,j-1) != 0:
                        num[i-1][j-1].draw(win)
                    else:
                        continue
        # The same as the first condition.
        elif x<80 and 260<y<340:
            pre = [[],[],[],[]]
            for i in range(4):
                for j in range(4):
                    pre[i].append(board.board[i][j])
            board.moveUnits("upwards")
            if pre != board.getBoard():
                board.newUnit()
            for i in [1,2,3,4]:
                for j in [1,2,3,4]:
                    num[i-1][j-1].undraw()
                    num[i-1][j-1] = Text(Point(100*i+50,100*j+50),board.getNumber(i-1,j-1))
                    score.undraw()
                    score = Text(Point(300,650),board.updateTtlScore())
                    score.draw(win) 
                    if board.getNumber(i-1,j-1) != 0:
                        num[i-1][j-1].draw(win)
                    else:
                        continue
        # The same as the first condition.
        elif 520<x<600 and 260<y<340:
            pre = [[],[],[],[]]
            for i in range(4):
                for j in range(4):
                    pre[i].append(board.board[i][j])
            board.moveUnits("downwards")
            if pre != board.getBoard():
                board.newUnit()
            for i in [1,2,3,4]:
                for j in [1,2,3,4]:
                    num[i-1][j-1].undraw()
                    num[i-1][j-1] = Text(Point(100*i+50,100*j+50),board.getNumber(i-1,j-1))
                    score.undraw()
                    score = Text(Point(300,650),board.updateTtlScore())
                    score.draw(win) 
                    if board.getNumber(i-1,j-1) != 0:
                        num[i-1][j-1].draw(win)
                    else:
                        continue
        # If there's a click out of buttons: it will ask for a new click.
        else:
            board.moveUnits("lala")
        # To judge whether or not you lose the game after a round.
        judgelose = board.judgeBool()
        findchanges = board.if2048()
        # Only for testing:
        print judgelose,findchanges,board.getBoard()
        p = win.getMouse()
        x = p.getX()
        y = p.getY()

    # To give you a final result according to the previous records:
    
    if board.judgeBool() == False :
        print "You fail!"
        Text(Point(300,680),'YOU FAIL!').draw(win)
        p = win.getMouse()
        # Close the window.
        win.close()
        
    if board.judgeBool() == True :
        print "You win!"
        Text(Point(300,780),'YOU WIN!').draw(win)
        p = win.getMouse()
        # Close the window.
        win.close() 

if "__name__" == "game()":
    game()
