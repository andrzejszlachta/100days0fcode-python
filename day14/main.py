import random

from day14 import art
from day14 import game_data

def init():
    print("\n"*20)
    print(art.logo)

    def new_question(prev=None, score=0):
        def get_correct_answer(obj_a, obj_b):
            if obj_a['follower_count'] > obj_b['follower_count']:
                return "a"
            else:
                return "b"

        if prev is None:
            object_a = random.choice(game_data.data)
        else:
            object_a = prev
        object_b = random.choice(game_data.data)

        print(f"Compare A: {object_a['name']}, {object_a['description']}, from {object_a['country']}")
        print(art.vs)
        print(f"Compare B: {object_b['name']}, {object_b['description']}, from {object_b['country']}")
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        correct_answer = get_correct_answer(object_a, object_b)
        print("\n" * 20)
        print(art.logo)
        if answer == correct_answer:
            new_score = score + 1
            print(f"You're right! Current score: {new_score}")
            if correct_answer == "a":
                new_question(object_a, new_score)
            else:
                new_question(object_b, new_score)
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
    new_question()

init()
