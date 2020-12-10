"""
File: dayoftheweek_game.py
Author: MTG
Topic: Game
This module implements a method for retrieving the day of the week from a date.
Lewis Carroll, To Find the Day of the Week for any Given Date, Nature, Nature, 1887
Steps for the algoritm:
Take the given date in 4 portions, viz. the number of centuries, the number of years over, the month, the day of the month.
Compute the following 4 items, adding each, when found, to the total of the previous items. When an item or total exceeds 7, divide by 7, and keep the remainder only.
Century-item: For 'Old Style' (which ended 2 September 1752) subtract from 18. For 'New Style' (which began 14 September 1752) divide by 4, take overplus from 3, multiply remainder by 2.
Year-item: Add together the number of dozens, the overplus, and the number of 4s in the overplus.
Month-item: If it begins or ends with a vowel, subtract the number, denoting its place in the year, from 10. This, plus its number of days, gives the item for the following month. The item for January is "0"; for February or March, "3"; for December, "12".
Day-item: The total, thus reached, must be corrected, by deducting "1" (first adding 7, if the total be "0"), if the date be January or February in a leap year, remembering that every year, divisible by 4, is a Leap Year, excepting only the century-years, in `New Style', when the number of centuries is not so divisible (e.g. 1800).
The final result gives the day of the week, "0" meaning Sunday, "1" Monday, and so on.
"""


import math
import functools
from random import randrange
from typing import NamedTuple, ClassVar
from dataclasses import dataclass, field
from characters import *
from players import Player


class Date(NamedTuple):
    year: str
    month: str
    day: str


class ParsedDate(NamedTuple):
    day: int
    month: str
    year: int
    century: int
    full_year: int


class DayOfTheWeek:
    """Calculate the Day of the Week 
    without python libraries!!
    """

    number_of_games_created = 0

    def __init__(self, date: Date):
        self.date = DayOfTheWeek.parse_items(date)
        DayOfTheWeek.update_counter()

    def check_less_that_seven(function):
        @functools.wraps(function)
        def wrapper(self):
            n = function(self)
            if n >= 7:
                _, rem = divmod(n, 7)

                return rem
            else:
                return n

        return wrapper

    @property
    def game_type(self) -> str:
        return f"Find the day of the week"

    @classmethod
    def update_counter(cls):
        cls.number_of_games_created += 1

    @staticmethod
    def parse_items(date: Date) -> ParsedDate:
        century = date.year[:2]
        year = date.year[2:]

        return ParsedDate(
            full_year=int(date.year),
            century=int(century),
            year=int(year),
            month=date.month,
            day=int(date.day),
        )

    @check_less_that_seven
    def century_item(self):
        _, reminder = divmod(self.date.century, 4)
        reminder = abs(reminder - 3) * 2
        return reminder

    @check_less_that_seven
    def year_item(self):
        # find number of dozen
        dozen, reminder = divmod(self.date.year, 12)
        n_1 = dozen + reminder
        # find number of 4 in reminder
        q_1, r_1 = divmod(reminder, 4)
        n_3 = n_1 + q_1
        return n_3

    @check_less_that_seven
    def day_item(self):
        return self.date.day

    @staticmethod
    def month_converter(month):
        months = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]
        return months.index(month) + 1

    @staticmethod
    def is_leap(n: int):
        if n % 400 == 0:
            return True
        if n % 100 == 0:
            return False
        if n % 4 == 0:
            return True
        else:
            return False

    @staticmethod
    def number_days_month(full_year, month):
        # month_number = month_converter(month)
        temp_list = [1, 3, 5, 7, 8, 10, 12]
        if month == 2:
            if DayOfTheWeek.is_leap(full_year) == True:
                return 28 + 1
        else:
            if month in temp_list:
                return 31
            else:
                return 30

    @check_less_that_seven
    def month_item(self):

        # check if the month starts and end with vowels
        vowels = tuple("aeiouyAEIOUY")
        month_number = DayOfTheWeek.month_converter(self.date.month)

        if self.date.month.startswith(vowels) or self.date.month.endswith(vowels):
            m_1 = 10 - month_number

        else:
            m_1 = 10 - (month_number - 1)

        num_day = DayOfTheWeek.number_days_month(self.date.full_year, month_number - 1)

        m_2 = num_day + m_1

        return m_2

    @check_less_that_seven
    def do_calculation(self):
        return (
            self.century_item() + self.year_item() + self.month_item() + self.day_item()
        )

    def answer(self):

        weekdays_dic = {
            0: "Sunday",
            1: "Monday",
            2: "Tuesday",
            3: "Wedsday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
        }

        return weekdays_dic[self.do_calculation()]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(data='{self.data}')"


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


class Dialog(DayOfTheWeek):
    def __init__(self, date, player_1: Player, player_2: Player):
        super().__init__(date)
        self.player_1 = player_1
        self.player_2 = player_2
        print(date)

    def talk_and_play(self):

        print(f"{self.player_1.name} says: What day of the week was {self.date}?")
        print(f"{self.player_2.name} says: I dont know!")
        print(f"{self.player_1.name} says: It was {self.answer()}")
        print(f"{self.player_2.name} says: Wow, how have you make it!")
        print(f"{self.player_1.name} says: Just counting around!")


if __name__ == "__main__":
    alice = WonderlandMember.hero()
    rabbit = StrangeAnimal.white_rabbit()
    player_1 = Player(rabbit.name)
    player_2 = Player(alice.name)
    # print(player_1.check_who_plays())
    date = Date("2020", "November", "9")
    game = Dialog(date, player_1, player_2)
    game.talk_and_play()
