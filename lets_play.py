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

# create test
# create property size


class WonderlandMember:
    """
    Creates a member of Wonderland
    """

    def __init__(
        self, name: str, species: str, fantastic: bool = False, age: int = None
    ):
        self.name = name
        self.species = species
        self._localfantastic = None
        self.age = age

    @property
    def fantastic(self):
        return self._localfantastic

    @fantastic.setter
    def fantastic(self):

        if self.fantastic is None:
            return f"Here you are! The only human in Wonderland: {self.name}"
        else:
            return f"This is fantastic character: {self.name}"

    @staticmethod
    def get_quotes(url):
        """Get all the quotes of a webpage and return a list

        Args:
            url ([type]): webpage 

        Returns:
            list: list of quotes in the webpage
        """
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        quotes = []
        for row in soup.find_all("div", attrs={"class": "quoteText"}):
            quote = row.text.split("―\n")[0]
            quotes.append(quote)
        return quotes

    @staticmethod
    def print_random_quote(quotes):
        n = random.randrange(len(quotes))
        print(quotes[n])

    # here u can add an initial phrase to introcude the chacrter
    # But u have to pick the frase from another file with something
    def words_play(self, words) -> str:
        return f"{self.name} says:- {words}-"

    # I wonder if I've been changed in
    # the night?  Let me think:  was I the same when I got up this
    # morning?  I almost think I can remember feeling a little
    # different.  But if I'm not the same, the next question is, Who in
    # the world am I?  Ah, THAT'S the great puzzle!'

    # I'll try if I know all the
    # things I used to know.  Let me see:  four times five is twelve,
    # and four times six is thirteen, and four times seven is--oh dear!
    # I shall never get to twenty at that rate!  However, the
    # Multiplication Table doesn't signify

    # “I’m sure I ’m not Ada,” she said, “for her hair goes in such long ringlets, and mine doesn’t go in ringlets at all;
    # and I ’m sure I can ’t be Mabel, for I know all sorts of things, and she, oh! she knows such a very little!
    # Besides, she’s she,
    # and I’m I, and—oh dear, how puzzling it all is! I ’ll try if I know all the things I used to know.

    # Let me see: four times five is twelve, and four times six is thirteen, and four times seven is—oh dear!
    # I shall never get to twenty at that rate! However, the Multiplication Table don’t signify..

    @classmethod
    def hero(cls) -> "WonderlandMember":
        return cls("Alice", "human", False, 12)


class Rulers(WonderlandMember):

    """
    Creates the Rulers Member in Wonderland
    """

    def __init__(self, name, species, peerage, sport, fantastic=True, age=None):
        super().__init__(name, species, fantastic, age)
        self.peerage = peerage
        self.sport = sport

    @classmethod
    def queen_of_hearts(cls):
        return cls("Queen of hearths", "human", "Queen", "criquet")


@dataclass
class Player:
    """Create Player Dataclass
    """

    name: str
    count_player: ClassVar[int] = 0
    player_number: int = field(init=False)

    def __post_init__(self):
        self.player_number = Player.update_counter()

    @classmethod
    def update_counter(cls):
        cls.count_player += 1
        return cls.count_player

    def check_who_plays(self):
        if (self.player_number == 1) and (self.name == "Alice"):
            raise ValueError("The first player cannot be Alice")
        elif (self.player_number == 2) and (self.name != "Alice"):
            raise ValueError("The second player has to be Alice")
        else:
            print("Let us play")


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


class Dialog(RollingBaseMultiplicationTable):
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
            rr = r.read()
        return rr.split("\n\n")

    def read_withclass2(self, file):
        with ReadTxt(file) as r:
            paragraph = r.read()
        par_list = paragraph.split("\n\n")
        return par_list[0], par_list[1]

    def talk_and_play(self, chapter_name, paragraph_content):
        paragraph = self.write_paragraph(chapter_name, paragraph_content)
        first_sentence, second_sentence = self.read_withclass2(
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
        print(f"{self.player_2.name} says:The game fails becuse .")


# devo cambiarlo fino a 13

if __name__ == "__main__":

    # alice = WonderlandMember.hero()
    # paragraph_content = "I wonder if I've been changed in the night?\nLet me think:  was I the same when I got up this morning?\nI almost think I can remember feeling a little different.\nBut if I am not the same, the next question is, Who inthe world am I?\nAh, that is the great puzzle!\n\nI will try if I know all the things I used to know."
    # par = alice.write_paragraph("CHAPTER II: The Pool of Tears", paragraph_content)
    # print(alice.read_withclass("CHAPTER II: The Pool of Tears.txt"))
    # print()
    # a, b = alice.read_withclass2("CHAPTER II: The Pool of Tears.txt")
    # print(a)

    alice = WonderlandMember.hero()
    queen = Rulers.queen_of_hearts()
    player_1 = Player(alice.name)
    player_2 = Player(queen.name)
    paragraph_content = "I wonder if I've been changed in the night?\nLet me think:  was I the same when I got up this morning?\nI almost think I can remember feeling a little different.\nBut if I am not the same, the next question is, Who inthe world am I?\nAh, that is the great puzzle!\n\nI will try if I know all the things I used to know."
    chapter_name = "CHAPTER II: The Pool of Tears"
    # print(player_1.check_who_plays())

    # date = Date(*input().split())
    game = Dialog(player_1, player_2)
    game.talk_and_play(chapter_name, paragraph_content)
