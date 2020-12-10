"""
File: lets_play.py
Author: MTG
Topic: Maths riddle
This module implements a Carrollian treatment of the base of a number system as it appears in Alice in Wonderland.
F. Abeles, Multiplication in changing bases: A note on Lewis Carroll,  Historia Mathematica, vol. 3, 1976
"""

import numpy as np
import string
import random
import math
import functools
from random import randrange
from typing import NamedTuple, ClassVar
from dataclasses import dataclass, field
import requests
from bs4 import BeautifulSoup
from characters import *
from players import Player



class RollingBaseMultiplicationTable:
    def __init__(self, size):
        self.size = size

    @staticmethod
    def rolling_base(row: int = None, column: int = None, default: int = 6) -> int:
        return default + (column - 1) * (row - 1)

    @staticmethod
    def custom_base_repr(number, base=2, padding=0):

        digits_till_36 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        random.seed(42)
        digits_from_36_till_127 = "".join(
            random.choices(string.ascii_lowercase +
                           string.punctuation, k=127 - 36)
        )
        digits = digits_till_36 + digits_from_36_till_127

        if base > len(digits):
            raise ValueError(
                "Bases greater than 126 not handled in custom_base_repr.")
        elif base < 2:
            raise ValueError("Bases less than 2 not handled in base_repr.")

        num = abs(number)
        res = []
        while num:
            res.append(digits[num % base])
            num //= base
        if padding:
            res.append("0" * padding)
        if number < 0:
            res.append("-")
        return "".join(reversed(res or "0"))

    def change_base_table(self):

        M = [[0] * self.size for i in range(self.size)]

        for i in range(self.size):
            for j in range(i + 1):
                M[i][j] = RollingBaseMultiplicationTable.custom_base_repr(
                    (i + 1) * (j + 1),
                    RollingBaseMultiplicationTable.rolling_base(i + 1, j + 1),
                )

        return M



class WriteTxt:
    def __init__(self, paragraph_name):
        self.paragraph_name = paragraph_name

    def __enter__(self):
        self.paragraph = open(self.paragraph_name, "w")
        return self.paragraph

    def __exit__(self, exc_type, exc_value, traceback):
        if self.paragraph:
            self.paragraph.close()


class ReadTxt:
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        self.paragraph = open(self.file_name, "r")
        return self.paragraph

    def __exit__(self, exc_type, exc_value, traceback):
        if self.paragraph:
            self.paragraph.close()


class Game(RollingBaseMultiplicationTable):
    def __init__(self, player_1: Player, player_2: Player, size=12):
        super().__init__(size)
        self.player_1 = player_1
        self.player_2 = player_2

    def write_paragraph(self, chapter, content):
        paragraph_name = f"{chapter}.txt"
        with WriteTxt(paragraph_name) as w:
            w.write(content)


    def read_withclass(self, file):
        with ReadTxt(file) as r:
            paragraph = r.read()
        par_list = paragraph.split("\n\n")
        return par_list[0], par_list[1]

    def talk_and_play(self, chapter_name, paragraph_content):
        paragraph = self.write_paragraph(chapter_name, paragraph_content)
        first_sentence, second_sentence = self.read_withclass(
            chapter_name + ".txt")

        M = self.change_base_table()

        print(f"{self.player_2.name} says:You are in the Rabbit Hole!")
        print(f"{self.player_1.name} says:{first_sentence}")
        print(f"{self.player_2.name} says:Your world is changed!")
        print(f"{self.player_1.name} says:{second_sentence}")
        print(f"{self.player_2.name} says:Let us stat play!How much 4 x 5 is?")
        print(f"{self.player_1.name} says:{M[4][3]}")
        print(f"{self.player_2.name} says: And 4 x 6 is?")
        print(f"{self.player_1.name} says:{M[5][3]}")
        print(f"{self.player_2.name} says:...4 x 7 is?")
        print(f"{self.player_1.name} says:{M[6][3]}")
        print(f"{self.player_2.name} says:...4 x 9 is?")
        print(f"{self.player_1.name} says:{M[8][3]}")
        print(f"{self.player_2.name} says:...4 x 11 is?")
        print(f"{self.player_1.name} says:{M[10][3]}")
        print(f"{self.player_2.name} says:...4 x 12 is?")
        print(f"{self.player_1.name} says:{M[11][3]}")
        print(
            f"{self.player_1.name} says:Oh dear!I shall never get to twenty at that rate!"
        )
        print(f"{self.player_2.name} says:You are right!4 x 13 is not equal to 20!")
        print(
            f"{self.player_2.name} says:Ahahah! See, Wonderland is not a decimal-based universe."
        )
        print(f"{self.player_2.name} says:The only way to get 20 is multiplying 4 x 13 = 1X")




if __name__ == "__main__":

    alice = WonderlandMember.hero()
    rabbit = StrangeAnimal.white_rabbit()
    player_1 = Player(alice.name)
    player_2 = Player(rabbit.name)
    print(player_1)
    print(player_2)
    paragraph_content = "I wonder if I've been changed in the night?\nLet me think:  was I the same when I got up this morning?\nI almost think I can remember feeling a little different.\nBut if I am not the same, the next question is, Who inthe world am I?\nAh, that is the great puzzle!\n\nI will try if I know all the things I used to know."
    chapter_name = "CHAPTER II: The Pool of Tears"
    print()
    game = Game(player_1, player_2)
    game.talk_and_play(chapter_name, paragraph_content)
