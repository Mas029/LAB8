#---------------------------------------
#  Game Mechanics
#    Student A (team lead) Muhammad Ali Sajid
#---------------------------------------

def welcome_message():
    """
    Display the game's welcome message to the player.

    Parameters: None
    Returns: None
    """
    #------------------------
    print("Welcome to the game")
    print("Answer these question")
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------
#---------------------------------------
    
def choose_category(categories):
    """
    Ask the player to choose a quiz category from a list of categories.

    Parameters:
    - categories (list of str): A list of category names.

    Returns:
    - str: The chosen category.
    """
    #------------------------
    print(categories)
    x=input()
    if x in categories:
        return x
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_score(score, round_number):
    """
    Display the current score and round number to the player.

    Parameters:
    - score (int): The player's current score.
    - round_number (int): The current round number.

    Returns: None
    """
    #------------------------
    print("Round :", round_number)
    print("Score is :", score)
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------
    
def game_over_message(final_score):
    """
    Display a "game over" message along with the player's final score.

    Parameters:
    - final_score (int): The player's final score at the end of the game.

    Returns: None
    """
    #------------------------
    print("game over")
    print("final score :", final_score)
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------
    
def run_game_rounds(categories):
    """
    Implement a basic loop to run the game for 5 rounds.

    Parameters:
    - categories (list of str): A list of quiz categories.

    Returns: None
    """
    #------------------------
    for i in range(5):
        run_game_rounds(categories)
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------
        
def validate_answer(player_answer, correct_answer):
    """
    Validate the player's answer (correct or incorrect).

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the player's answer is correct, False otherwise.
    """
    #------------------------
    return player_answer== correct_answer
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def update_score(score, correct):
    """
    Implement a scoring system, where each correct answer awards points.

    Parameters:
    - score (int): The current score of the player.
    - correct (bool): Whether the player's answer was correct.

    Returns:
    - int: The updated score.
    """
    #------------------------
    if correct:
        score=score+1
    return score
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def next_round(round_number):
    """
    Increase the round number after each question.

    Parameters:
    - round_number (int): The current round number.

    Returns:
    - int: The next round number.
    """
    #------------------------
    return round_number+1
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def check_game_over(incorrect_answers):
    """
    Implement a "game over" condition if the player makes 3 incorrect answers.

    Parameters:
    - incorrect_answers (int): The number of incorrect answers given by the player.

    Returns:
    - bool: True if the game should be over, False otherwise.
    """
    #------------------------
    return incorrect_answer>=3
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def restart_or_exit():
    """
    Restart the game or exit after the game is over.

    Parameters: None
    Returns: None
    """
    #------------------------
    option = input()
    if option == "restart":
        print("restarting the game")
    elif option== "exit":
        print("exiting the game")
    else:
        print("invalid input")
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------





