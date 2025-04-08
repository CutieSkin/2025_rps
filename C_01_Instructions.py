
# print error if user does not enter something that is valid
print(error)
print()

# displays instructions
def instructions():
        print("""
            *** instructions ****
            to begin, choose the number of rounds (or press <enter> for
            infinite mode).
            then play against the computer. you need to choose R (rock)
            p (paper) s (scissors).
            the rules are as follow:
            o paper beats rock
            o rock beats scissors
            o scissors beats paper
            press <xxx> to end the game at anytime
            Good luck
        """)

# main routine
print()
print("💎📄✂️ rock / paper / scissors game 💎📄✂️")
print()

# ask the user if they want instructions (check they say yes / no)
want_instructions = string_checker("do you want to see the instructions")

# display the instructions if the user wants to see them...
if want_instructions == "yes":
        instructions()
        print()
        print("program continues")