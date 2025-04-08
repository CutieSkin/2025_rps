# CHeck that users have entered a valid
# option based on list
def string_checker(question, valid_ans=("yes","no")):

    error = f"please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure its lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

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


# checks for an integer more than 0 (allows <enter>
def int_check(question):
    while True:
        error = "please enter an intergar that is 1 or more. "

        to_check = input(question)

        # checks for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            #checks that the number is more than / equal to 13
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Main Routine starts here

# Intialise game variables
mode = "regular"
rounds_played = 0

rps_list = ["rock", "paper", "scissors", "xxx"]


print("🪨📄✂️Rock / Paper / Scissors Game✂️📄")
print()

# Instructions
# ask the user if they want instructions (check they say yes / no)
want_instructions = string_checker("do you want to see the instructions")

# display the instructions if the user wants to see them...
if want_instructions == "yes":
        instructions()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5

# Game loop starts here
while rounds_played < num_rounds:

    # Rounds headings
    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️ Round {rounds_played + 1} (Infinite Mode) ♾️♾️♾️"
    else:
        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1} of {num_rounds} 💿💿💿"

    print(rounds_heading)
    print()

    # get user choice
    user_choice = string_checker("Choose: ", rps_list)
    print("You chose ", user_choice)
    if user_choice == "xxx":
        break

    rounds_played += 1


    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1



# Games loop ends here

# Game History / Statistics Area