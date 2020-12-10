"""
File: guess_number.py
Author: MTG
Topic: Game

This module implements a number guess game from Lewis Carroll 
Richard F. McCoart, Lewis Carroll’s Amazing Number-Guessing Game, College Mathematics Journal, 2002

Algorithm steps:

Think of a number (a positive integer).

Multiply by 3.

If the result is odd, then add either 5 or 9 (whichever you like), then divide by 2, then add 1.
If the result is even, then subtract either 2 or 6 (whichever you like), then divide by 2, then add 29 or 33 or 37 (whichever you like).
Multiply by 3.

If the result is odd, then add either 5 or 9 (whichever you like), then divide by 2, then add 1.
If the result is even, then subtract either 2 or 6 (whichever you like), then divide by 2, then add 29 or 33 or 37 (whichever you like).
Add 19 to original number you chose and append any digit, 0-9, to this number.

Add the previous result.

Divide by 7 and drop any remainder.

Divide by 7 again and drop any remainder, and tell me what result you get. (“How often does it go?”)

Here’s how to derive the number that was chosen originally:

Multiply the final answer by 4 and subtract 15. If the first answer was “even,” subtract 3 more, and if the second answer was “even,” subtract 2 more.

"""


import math
import functools
from random import randrange
from typing import NamedTuple, ClassVar
from dataclasses import dataclass, field
from characters import *
from players import Player



class Number:
    def __init__(self, number=None):
        self.number = number


class GuessNumber:
    """Create a number game
    """

    def __init__(self, number=None):
        self.number = number

    @property
    def game_type(self) -> str:
        return f"Guess a Number"

    @staticmethod
    def odd_even_routine(number) -> float:

        if number % 2 == 0:
            new_number = ((number - 2) / 2) + 29
        else:
            new_number = ((number + 5) / 2) + 1
        return new_number

    @staticmethod
    def check_odd_even(number) -> bool:
        if number % 2 == 0:
            return True
        else:
            return False

    def first_answer(self) -> tuple:

        n = 3 * self.number
        return (n, GuessNumber.check_odd_even(n))

    def second_answer(self, n: int) -> tuple:

        first_routine_num = GuessNumber.odd_even_routine(n)
        n_2 = 3 * first_routine_num
        return (n_2, GuessNumber.check_odd_even(n))

    def third_answer(self, n_2: int) -> int:

        second_routine_num = GuessNumber.odd_even_routine(n_2)

        number_add_19 = self.number + 19
        random_int = randrange(10)
        number_append = int(str(number_add_19) + str(random_int))

        n_3 = second_routine_num + number_append
        return n_3 // 49

    def answer(self, ans_1, ans_2, n_3) -> int:
        n_temp = (n_3 * 4) - 15

        if (ans_1 == True) and (ans_2 == False):
            return int(n_temp - 3)
        elif (ans_1 == False) and (ans_2 == True):
            return int(n_temp - 2)
        elif (ans_1 == True) and (ans_2 == True):
            return int(n_temp - 5)
        else:
            return int(n_temp)


class Game(GuessNumber):
    def __init__(self, player_1: Player, player_2: Player, number=None):
        super().__init__(number)
        self.player_1 = player_1
        self.player_2 = player_2

    def print_even_odd(self, answer):
        if answer is True:
            return (
                f"{self.player_1.name} says: Is your number even?\n"
                f"{self.player_2.name} says: The number is even."
            )
        else:
            return (
                f"{self.player_1.name} says: Is your number even?\n"
                f"{self.player_2.name} says: No,the number is odd."
            )

    def pick_number(self) -> int:
        return int(input(f"{self.player_2.name} says: Picked!"))

    def set_number(self, number: int):
        self.number = number

    def pick_set(self):
        number = self.pick_number()
        self.set_number(number)

    def talk_and_play(self):
        print(
            f"{self.player_1.name} says:- {self.player_2.name}, pick a number and dont say it to me!"
        )

        print(f"{self.player_2.name} says:- Okay!Lets us start!")
        self.pick_set()
        print(
            f"{self.player_1.name} says:- {self.player_2.name}, multiply your number by 3."
        )
        first_number, check_1 = self.first_answer()
        print(self.print_even_odd(check_1))
        print(
            f"{self.player_1.name} says:- Now {self.player_2.name}, do some calculations and multiply your number by 3."
        )
        second_number, check_2 = self.second_answer(first_number)
        print(self.print_even_odd(check_2))
        print(
            f"{self.player_1.name} says:- Do those other calculations and tell me the final number!"
        )
        third_number = self.third_answer(second_number)
        print(f"{self.player_2.name} says:- The final number is {third_number}")
        final_number = self.answer(check_1, check_2, third_number)
        print(
            f"{self.player_1.name} says:- The number you have been choosing is {final_number}\n"
            f"{self.player_2.name} says:- Oh!How have you made it?\n"
            f"{self.player_1.name} says:- It is maths non magic!\n"
        )


if __name__ == "__main__":

    alice = WonderlandMember.hero()
    rabbit = StrangeAnimal.white_rabbit()
    player_1 = Player(rabbit.name)
    player_2 = Player(alice.name)

    game = Game(player_1, player_2)
    game.talk_and_play()
