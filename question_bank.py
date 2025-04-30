#---------------------------------------
#  Question Bank
#    Student B  Faiz Ahmad  281132217
#---------------------------------------

import random

# Simplified example with one category. Expand as needed.
questions = {
    "Science": [
        ("What is the chemical symbol for water?", "H2O"),("what gas do plants absorb from the air?","carbon dioxide"),("what force pulls object towards earth","gravity")
        # Add more questions as tuples (question, answer)
    ],"maths":[("what is 2+3,5")]
}

hints = {
    "Science": ["it is made up of 2 hydrogen atoms","it's the opposite of oxygen in photosynthesis","you experience this when you fall"
        # Pair each question with a corresponding hint.
    ],"maths":[("its the first odd prime no")]
    # Repeat for other categories as needed.
}

#---------------------------------------

def select_random_question(category):
    """
    Selects a random question from the specified category.

    Parameters:
    - category (str): The category from which to select a question.

    Returns:
    - tuple: A tuple containing the selected question (str) and its corresponding answer (str).
    """
    #------------------------
    # Add your code here
    return random.choice(questions[category])

    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def check_answer(player_answer, correct_answer):
    """
    Checks if the player's answer matches the correct answer.

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the answers match, False otherwise.
    """
    #------------------------
    # Add your code here
    player_lower = ""
    correct_lower = ""

    for char in player_answer:
        player_lower += char.lower()

    for char in correct_answer:
        correct_lower += char.lower()

    # Compare character by character
    if len(player_lower) != len(correct_lower):
        return False

    for i in range(len(player_lower)):
        if player_lower[i] != correct_lower[i]:
            return False
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def remove_question(category, question):
    """
    Removes a question from the list once it has been asked.

    Parameters:
    - category (str): The category from which to remove the question.
    - question (str): The question to be removed.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    if category not in questions:
        raise ValueError(f"Category '{category}' not found.")

    new_list = []
    for item in questions[category]:
        if item[0] != question:
            new_list.append(item)

    questions[category] = new_list
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_question_and_accept_answer(question):
    """
    Displays a question to the player and accepts their answer via input.

    Parameters:
    - question (str): The question to be displayed.

    Returns:
    - str: The player's answer to the question.
    """
    #------------------------
    # Add your code here
    print(question)
    player_answer=input("your answer:")
    return player_answer
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def provide_hint(category, question):
    """
    Provides a hint for the given question based on its category.

    Parameters:
    - category (str): The category of the question.
    - question (str): The question for which to provide a hint.

    Returns:
    - str: The hint for the given question.
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_correct_answer(correct_answer):
    """
    Displays the correct answer if the player's answer is incorrect.

    Parameters:
    - correct_answer (str): The correct answer to the question.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    print(f"the correct answer is {correct_answer}")
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------



