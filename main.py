import math as m
import time
import random as r
import curses as c
import sys
## Other Files ##
import variables as var

## -- Operations -- ##
def subtraction(A,B):
    answer = A - B
    return answer

def addition(A,B):
    answer = A + B
    return answer

def multiplication(A,B):
    answer = A*B
    return answer

def division(A,B):
    answer = A/B
    return answer

def exponent(A,B):
    answer = pow(A,B)
    return answer

def logarithm(A,B):
    answer = log(B,A)
    return answer
## -- Operations -- ##

def determine(A,B,operator): #Operation LOGIC
    if operator == "x":
        C = multiplication(A,B)
    elif operator == "/":
        C = division(A,B)
    elif operator == "+":
        C = addition(A,B)
    elif operator == "-":
        C = subtraction(A,B)
    elif operator == "^":
        C = exponent(A,B)
    elif operator == "log":
        C = logarithm(A,B)
    else:
        print("Something went wrong")
    print(f"Output: {C} = {A} {operator} {B}")
    return C

def OP_query(): # Ask for Operator
    while True:
        OP = input("Add, Subtract, Multipy, Divide, Exponent or Log?\nInput: ")
        if OP in ["x","*","multiply"] :
            OP = "x"
            return OP
        elif OP in["/","divide"]:
            OP = "/"
            return OP
        elif OP in ["+","add","plus"]:
            OP = "+"
            return OP
        elif OP in ["-","subtract","minus"]:
            OP = "-"
            return OP
        elif OP in ["^","exponent","power"]:
            OP = "^"
            return OP
        elif OP in ["log","Log"]:
            OP = "log"
            return OP
        else:
            print("NOT AN OPERATION\r",end="")
            time.sleep(0.25)

def NUM_query(): # Ask for Number
    while True:
        NUM = input("Provide a number within (-10 <= X <= 10)\nInput: ")
        try:
            NUM = round(float(NUM),2)
            if NUM < 11 and NUM > -11 and NUM != 0:
                return NUM
            else:
                print("DIGIT OUT OF RANGE\r",end="")
                time.sleep(0.25)
                NUM = 0
        except ValueError:
            print("NOT A NUMBER\r",end="")
            time.sleep(0.25)
            NUM = 0

def question(mult,bound,tries,lives): # Ask a SIMPLE question
    X = r.randint(-bound,bound)
    A = r.randint(-abs(round(X*mult)),abs(round(X*mult)))
    steps = tries
    while X == 0:
        print("Whoops it landed on ZERO! Do you know what the ODDS are?\n")
        X = r.randint(-bound,bound)
    print(f"Solve for {X} in only {steps} tries! Lives: {lives}")
    while lives > 0:
        print(f"\nAttempt: 1  Lives: {lives}\nInput: {A}")
        OP = OP_query()
        B = NUM_query()
        C = determine(A,B,OP)
        for I in range(1,steps):
            if C == X:
                print("On your FIRST ATTEMPT? Truly immaculate!")
                return
            print(f"\nAttempt: {I}  Lives: {lives}\nInput: {C}")
            OP = OP_query()
            B = NUM_query()
            A = C
            C = determine(A,B,OP)
            if C == X:
                print(f"Congrats on getting {X} with {steps-I} spare!")
                return
        if C == X:
            print("On your FIRST ATTEMPT? Truly immaculate!")
            return
        else:
            lives = lives - 1
            A = C
            if lives == 0:
                Loss = True
                return Loss
            else:
                print(f"Truly disappointing. Lives Remaining: {lives}")

def DIFF_query(stdscr): # Ask for difficulty
    c.curs_set(0) # Turn off the default terminal blinking text cursor
    options = ["Simple","Easy","Medium","Standard","Hard","Extreme","IMPOSSIBLE"]
    current_selection = 3  # Default to Standard
    while True:
        stdscr.clear() # Clear the terminal screen buffer every frame refresh
        stdscr.addstr(2, 2, "Use LEFT and RIGHT arrow keys to navigate. Press ENTER to select.\n\n") # Draw the instructions label text
        stdscr.addstr(4,16, "Select your difficulty of choice!")
        stdscr.addstr(6, 2, "Your Choices:  ")
        for index, option in enumerate(options): # Display the selectable options side-by-side
            if index == current_selection: # Highlight the currently selected choice using inverse display colors
                stdscr.addstr(f" [ {option} ] ", c.A_REVERSE)
            else:
                stdscr.addstr(f"   {option}   ")
        stdscr.refresh()
        key = stdscr.getch() #Detects key presses

        # Handle Navigation Array Mapping Logic
        if key == c.KEY_LEFT:
            current_selection = (current_selection - 1) % len(options) # Move index left, wrap around to the end if out-of-bounds lower
        elif key == c.KEY_RIGHT:
            current_selection = (current_selection + 1) % len(options) # Move index right, wrap around to start if out-of-bounds upper
        elif key in [10, 13, c.KEY_ENTER]:
            return options[current_selection] # Break input monitoring state if Enter key is verified

def Try_Again(stdscr):
    c.curs_set(0)
    options = ["Yes","No"]
    current_selection = 0
    while True:
        stdscr.clear() # Clear the terminal screen buffer every frame refresh
        stdscr.addstr(2,16, "GAME OVER\n\n") # Draw the instructions label text
        stdscr.addstr(4,16, "Try Again?")
        stdscr.addstr(6, 2, "Your Choices:  ")
        for index, option in enumerate(options): # Display the selectable options side-by-side
            if index == current_selection: # Highlight the currently selected choice using inverse display colors
                stdscr.addstr(f" [ {option} ] ", c.A_REVERSE)
            else:
                stdscr.addstr(f"   {option}   ")
        stdscr.refresh()
        key = stdscr.getch() #Detects key presses

        # Handle Navigation Array Mapping Logic
        if key == c.KEY_LEFT:
            current_selection = (current_selection - 1) % len(options) # Move index left, wrap around to the end if out-of-bounds lower
        elif key == c.KEY_RIGHT:
            current_selection = (current_selection + 1) % len(options) # Move index right, wrap around to start if out-of-bounds upper
        elif key in [10, 13, c.KEY_ENTER]:
            return options[current_selection] # Break input monitoring state if Enter key is verified

def shop(stdscr,difficulty):
    pass






def DIFF_determine(): # Retreives DIFF from query responses
    difficulty = c.wrapper(DIFF_query)
    if difficulty == "Simple":
        print("How very simplistic of you.")
    elif difficulty == "Easy":
        print("Easy huh, math must be hard.")
    elif difficulty == "Medium":
        print("Still below average.")
    elif difficulty == "Standard":
        print("Keepin it standard?")
    elif difficulty == "Hard":
        print("Stepping it up are we?")
    elif difficulty == "Extreme":
        print("The peak of difficulty!")
    elif difficulty == "IMPOSSIBLE":
        print("ARE YOU INSANE?!")
    if difficulty in var.DIFF_LIST:
        diff = var.DIFF_LIST[difficulty]
        return diff

def main(Loss=False):
    balance = 0
    diff = DIFF_determine()
    while Loss == False:
        result = question(diff.mult,diff.bound,diff.tries,diff.lives)
        if result == True:
            Loss = True
            yes_or_no = c.wrapper(Try_Again)
            if yes_or_no == "yes":
                Loss = False
                wallet = 0
                diff = DIFF_determine()
            else:
                print("")
        else:
            balance = balance + diff.reward
            print(f"Congrats! Money earned: ${diff.reward} Total: ${balance}")



main()
