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
If the result is even, then subtract either 2 or 6 (whichever you like), then divide by 2, 
then add 29 or 33 or 37 (whichever you like).
Multiply by 3.

If the result is odd, then add either 5 or 9 (whichever you like), then divide by 2, then add 1.
If the result is even, then subtract either 2 or 6 (whichever you like), then divide by 2, 
then add 29 or 33 or 37 (whichever you like).
Add 19 to original number you chose and append any digit, 0-9, to this number.

Add the previous result.

Divide by 7 and drop any remainder.

Divide by 7 again and drop any remainder, and tell me what result you get. (“How often does it go?”)

Here’s how to derive the number that was chosen originally:

Multiply the final answer by 4 and subtract 15. If the first answer was “even,” subtract 3 more, 
and if the second answer was “even,” subtract 2 more.

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
    def check_odd_even(number):
        if number % 2 == 0:
            return True
        else:
            return False

    def first_answer(self):
        # print("Is the number even or odd? ")
        n = 3 * self.number
        return (n, GuessNumber.check_odd_even(n))

    def second_answer(self):
        first_new_number, _ = self.first_answer()
        first_routine_num = GuessNumber.odd_even_routine(first_new_number)
        n = 3 * first_routine_num
        return (n, GuessNumber.check_odd_even(n))

    def third_answer(self):
        second_new_number, _ = self.second_answer()
        second_routine_num = GuessNumber.odd_even_routine(second_new_number)

        number_add_19 = self.number + 19
        random_int = randrange(10)
        number_append = int(str(number_add_19) + str(random_int))

        number_sum = second_routine_num + number_append
        return number_sum // 49

    def answer(self, ans_1, ans_2, ans_3):
        n_1, odd_even_1 = ans_1
        n_2, odd_even_2 = ans_2

        n_temp = (ans_3 * 4) - 15

        if (odd_even_1 == True) and (odd_even_2 == False):
            return int(n_temp - 3)
        elif (odd_even_1 == False) and (odd_even_2 == True):
            return int(n_temp - 2)
        elif (odd_even_1 == True) and (odd_even_2 == True):
            return int(n_temp - 5)
        else:
            return int(n_temp)


class Game(GuessNumber):
    def __init__(self, player_1: Player, player_2: Player, number=None):
        super().__init__(number)
        self.player_1 = player_1
        self.player_2 = player_2

    # def print_even_odd(self, answer):
    #     if answer is True:
    #         return (
    #             f"{self.player_1.name} says: Is your number even?\n"
    #             f"{self.player_2.name} says: The number is even."
    #         )
    #     else:
    #         return (
    #             f"{self.player_1.name} says: Is your number even?\n"
    #             f"{self.player_2.name} says: No,the number is odd."
    #         )

    def pick_number(self) -> int:
        return int(input())

    def set_number(self, number: int):
        self.number = number

    def pick_set(self):
        number = self.pick_number()
        self.set_number(number)

    def print_even_odd(self, answer):
        return (
            f"{self.player_1.name} says: Is your new number even or odd?\n"
            f"{self.player_2.name} says:{answer}"
        )

    def talk_and_play(self):
        print(
            f"{self.player_1.name} says:- {self.player_2.name}, pick a number and dont say it to me!"
        )
        print(f"{self.player_2.name} says:- Okay!Picked")
        self.pick_set()
        check_1 = Game.check_odd_even(self.number)
        print(self.print_even_odd(check_1))
        print(
            f"{self.player_1.name} says:- {self.player_2.name}, multiply your number by 3."
        )
        first_number, check_2 = self.first_answer()
        print(self.print_even_odd(check_2))
        print(
            f"{self.player_1.name} says:- Now {self.player_2.name}, do some calculations and multiply your number by 3."
        )
        second_number, check_3 = self.second_answer()
        print(self.print_even_odd(check_3))
        print(
            f"{self.player_1.name} says:- Do those other calculations and tell me the final number!"
        )
        third_number = self.third_answer()
        print(f"{self.player_2.name} says:- The final number is {third_number}")
        final_number = self.answer(
            self.first_answer(), self.second_answer(), third_number,
        )
        print(
            f"{self.player_1.name} says:- The number you have been choosing is {final_number}\n"
            f"{self.player_2.name} says:- Oh!How have you make it?\n"
            f"{self.player_1.name} says:- The is maths non magic!\n"
        )


if __name__ == "__main__":

    alice = WonderlandMember.hero()
    rabbit = StrangeAnimal.white_rabbit()
    player_1 = Player(rabbit.name)
    player_2 = Player(alice.name)
    #initial_number = 3
    #game = Game(player_1, player_2, initial_number)
    game = Game(player_1, player_2)
    game.talk_and_play()
