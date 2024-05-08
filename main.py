
import random
from art import logo, vs
from game_data import data


# Format the account data into printable format
def format_account(account):
    """format the account data into printable format"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}."


## use if statement to check if user is correct
def check_answer(guess, a_follower, b_follower):
    """Checks followers against user's guess
    and returns True if they got it right.
    Or False if they got it wrong."""
    if a_follower > b_follower:
        return guess == "a"
    else:
        return guess == "b"


# Display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

# Make the game repeatable
while game_should_continue:
    # generate a game account from the game data

    # Making account at position B become the next account at position A
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        """Question:  
          What if the new random account is still the same account?:
          How can we get the code to continue checking untill 
          it found a different account?
    
        solution: we should replace if statement to while loop, then the code will keep checking untill they are no longer equal """
        account_b = random.choice(data)

    print(f"Compare A: {format_account(account_a)}.")
    print(vs)
    print(f"Against B: {format_account(account_b)}.")

    # Ask users for a guess
    guess = input("Who has more followers? type A or B?: ").lower()

    # check if user is correct
    ## Get follower count from the account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Clear the screen between rounds
    # clear()
    print(logo)

    # Give user feedback for their guess
    # score keeping
    if is_correct:
        score += 1
        print(f"You are Correct!. Current score {score} ")
    else:
        game_should_continue = False
        print(f"Sorry!, You are wrong!. Final score: {score}")






