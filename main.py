from random import randint
from game_data import data
from art import logo, vs


def higher_lower():
    print(logo)
    list_used_numbers = []
    score = 0
    print(f"You're score is {score}")
    end_game = True
    comparison_1 = 0
    comparison_2 = randint(0, 49)
    while end_game:
        print(f"Step {score+1}")
        persona_1 = data[comparison_1]
        print(f"Compare A: {persona_1['name']}, a {persona_1['description']}, from {persona_1['country']}")
        print(vs)
        persona_2 = data[comparison_2]
        print(f"Compare B: {persona_2['name']}, a {persona_2['description']}, from {persona_2['country']}")
        choice = input("Who has more followers? Type 'A' or 'B': ")
        if persona_1['follower_count'] > persona_2['follower_count'] and choice == 'A' or persona_1['follower_count'] < persona_2['follower_count'] and choice == 'B':
            score += 1
            print(f"You guessed! You score is: {score}")

        else:
            print(f"You lost with {score} score")
            end_game = False
        comparison_1 = comparison_2
        comparison_2 = randint(0, 49)

higher_lower()

