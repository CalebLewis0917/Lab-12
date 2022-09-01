# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Ashley McAlister
#               Sarah Smeltzer
#               Caleb Lewis
#               Botao Zeng
# Section:      521
# Assignment:   Lab12_Act1
# Date:         12 06 2021

from turtle import *
import random
import sys

# Set's speed of turtle to instant
speed(0)

# Creates a regular triangle at a specified size and location
def insertRectangle(x, y, length = 225, width = 50):
    moveTurtle(x, y)
    pensize(4)
    forward(length)
    right(90)
    forward(width)
    right(90)
    forward(length)
    right(90)
    forward(width)
    right(90)

# Moves turtle to a specific x and y value while orientating it towards the right
def moveTurtle(x, y):
    penup()
    goto(x, y)
    setheading(0)
    pendown()

# Inserts text at the position the turtle is at
def insertText(text, alignment, size = 30, font_type = "normal", text_color = "black", style = "Ariel"):
    '''Inserts text with the following parameters: string of text, alignment (center, left or right from turtle), size, font type (normal, bold, italics), text color adn style'''
    color(text_color)
    style = (style, size, font_type)
    write(text, font = style, align = alignment)

# Displays a title at the top of the screen
def gameTitle(title):
    moveTurtle(0, 225)
    insertText(title, "Center", 50, "bold")
    pensize(5)
    moveTurtle(-350, 215)
    forward(700)

# Creates Text surrounded by a rectangle
def menuBoxes(x, y, text, instructions):
    '''Creates a rectangle at specified (x, y) with text inside of it and smaller text right under the box to be menu options'''
    insertRectangle(x, y)
    moveTurtle(x + 225 / 2, y - 50)
    insertText(text, "Center")
    moveTurtle(x + 225 / 2, y - 75)
    insertText(instructions, "Center", 15, "italic")

# Adds .gif image of dice to represent the Pig dice game
def insertImage():
    moveTurtle(0, 75)
    showturtle()
    screen = Screen()
    screen.addshape("dice.gif")
    shape("dice.gif")

# Creates layout for menu, displaying the "buttons" and title
def menu():
    gameTitle("Pig Dice Game!")
    pensize(3)
    insertRectangle(-350, 325, 700, 650)
    menuBoxes(-275, -100, "Start Game", "Enter '1' to Start the Game")
    menuBoxes(50, -100, "Exit Game", "Enter '2' to Exit Game")
    menuBoxes(-115, -200, "Instructions", "Enter '3' to Learn to Play")

# Displaying text for instruction page
def instructions():
    hideturtle()
    gameTitle("How to Play!")
    moveTurtle(-370, 125)
    insertText("1) Chose which player goes first", "Left", 20)
    moveTurtle(-370, 75)
    insertText("2) Each Player takes a turn to roll a dice", "Left", 20)
    moveTurtle(-370, 0)
    insertText("3) If the player roles a 1, they score nothing and \n  the next player goes", "Left", 20)
    moveTurtle(-370, -40)
    insertText("4) Otherwise, the number rolled is added to their turn total", "Left", 20)
    moveTurtle(-370, -80)
    insertText("5) The player continues to role until the decide to 'hold'", "Left", 20)
    moveTurtle(-370, -155)
    insertText("6) Their turn total is then added to the player's score and \n  it's the next player's turn ", "Left", 20)
    moveTurtle(-370, -195)
    insertText("7) The player who reaches 100 points or more first wins!", "Left", 20)

# Displays instructions text and let's user exit back to main menu
def displayInstructions():
    clear()
    instructions()
    menuBoxes(-115, -250, "Main Menu", "Enter '1' to return to Main Menu")

    user_input = int(input("Enter '1' to return to main menu: "))
    while user_input != 1:
        user_input = int(input("Enter '1' to return to main menu: "))

    if user_input == 1:
        clear()
        startGame()

# Checks if the number the user enters can be casted to an int and is a 1, 2 or 3
def validNumber(num):
    try:
        num = int(num)

        if num == 1 or num == 2 or num == 3:
            return True
        else:
            return False
    except:
        return False

# Resets screen for actual game
def playDisplay():
    reset()
    hideturtle()
    gameTitle("Pig Dice Game!")
    moveTurtle(0, 0)

# Begins game by displaying menu and allowing for user to start or end the game or view instructions
def startGame():
    '''Creates Menu GUI for game and allows for user to navigate differen't opention using console inputs'''
    title("Pig Dice Game!")
    menu()
    insertImage()
    
    user_input = input("Enter a number to either Start or Exit the game or view Instructions: ")
    while validNumber(user_input) == False:     # asks user until they input a correct number
        user_input = input("Enter a number to either Start or Exit the game or view Instructions: ")

    user_input = int(user_input)
    if user_input == 1:
        playDisplay()
        playGame()
    elif user_input == 2:   # Ends program and closes turtle
        bye()
        sys.exit()
    elif user_input == 3:   # displays instructions
        hideturtle()
        displayInstructions()


def turtlee(diceResult,turtle):
  turtle.reset()
  if diceResult == 1:
      turtle.lt(90)
      turtle.forward(100)
  elif diceResult == 2:
      turtle.fd(100)
      turtle.rt(90)
      turtle.fd(100)
      turtle.rt(90)
      turtle.fd(100)
      turtle.lt(90)
      turtle.fd(100)
      turtle.lt(90)
      turtle.fd(100)
  elif diceResult == 3:
      turtle.fd(100)
      turtle.right(90)
      turtle.fd(100)
      turtle.rt(90)
      turtle.fd(100)
      turtle.bk(100)
      turtle.left(90)
      turtle.fd(100)
      turtle.right(90)
      turtle.fd(100)
  elif diceResult == 4:
      turtle.lt(90)
      turtle.bk(100)
      turtle.rt(90)
      turtle.fd(100)
      turtle.lt(90)
      turtle.fd(100)
      turtle.bk(200)
  elif diceResult == 5:
      turtle.lt(90)
      turtle.lt(90)
      turtle.fd(100)
      turtle.lt(90)
      turtle.fd(100)
      turtle.lt(90)
      turtle.fd(100)
      turtle.rt(90)
      turtle.fd(100)
      turtle.rt(90)
      turtle.fd(100)
  elif diceResult == 6:
      turtle.lt(90)
      turtle.lt(90)
      turtle.fd(100)
      turtle.lt(90)
      turtle.fd(100)
      turtle.lt(90)
      turtle.fd(100)
      turtle.rt(90)
      turtle.fd(100)
      turtle.rt(90)
      turtle.fd(100)
      turtle.rt(90)
      turtle.fd(100)
  
  
def endGame(p1, p2):
    if(p1>=100):
        print("Congrats Player 1! You won!")
    elif(p2>=100):
        print("Congrats Player 2! You won!")
    print("Final Score:")
    print("Player 1: " + str(p1))
    print("Player 2: " + str(p2))
    menu()

def playGame():
    turtle = Turtle()
    player = 1
    die = 0
    p1_score = 0
    p2_score = 0
    temp_score = 0
    file1 = open("rolls.txt",'w')
    file1.write("Roll:     Player:\n")
    while(p1_score<100 and p2_score<100):
        print("Player " + str(player) + ":")
        print("(1) Roll Die")
        print("(2) Hold")
        user_input = int(input("----> "))
        while(user_input!=2):
            if(user_input==1):
                die = random.randint(1,6)
                turtlee(die,turtle)
                if(die==1):
                    print("Sorry! Your turn is over and your score remains the same.")
                    temp_score = 0
                    break
                else:
                    temp_score += die
                    file1.write(str(die) + "          " + str(player) + "\n")
                    print("Turn Score: " + str(temp_score))
                    print()
                    print("(1) Roll Die")
                    print("(2) Hold")
                    user_input = int(input("----> "))
        if(player==1):
            p1_score += temp_score
            temp_score = 0
            player = 2
            print("Turn Over. Current Player 1 Score: " + str(p1_score))
            file1.write("Turn Total: " + str(temp_score) + "Total Score: " + str(p1_score))
        elif(player==2):
            p2_score += temp_score
            temp_score = 0
            player = 1
            print("Turn Over. Current Player 2 Score: " + str(p2_score))
            file1.write("Turn Total: " + str(temp_score) + "Total Score: " + str(p2_score))
        print()
    file1.close()
    endGame(p1_score, p2_score)
        
startGame()
playGame()

done()  # ends turtle