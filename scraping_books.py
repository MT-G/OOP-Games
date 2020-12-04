"""
File: scraping_books.py
Author: MTG 
Topic: web scarping

This module implements classmethods 
defining the main characters for each class, and staticmethods for adding funtionalities
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
import nltk
import re
from nltk import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from collections import defaultdict


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

    @classmethod
    def hero(cls) -> "WonderlandMember":
        return cls("Alice", "human", False, 12)

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

    def get_raw_book(self, url):
        #url = 'http://www.gutenberg.org/files/11/11-0.txt'

        response = requests.get(url)

        # from projectgutenber u have to use the decoder
        #raw = response.read().decode('utf-8')
        raw = response.text
        raw_capitalized = raw.capitalize()

        return raw_capitalized

    def get_42_inbooks(self, book, book_title):
        """Divide the book in chapters, find the word forty-two
           return a tuple or dictionary (or even a table) with chapter number, chapter name, 
           word forty-two, charcaters involved, and the formatted dialog
        """
        pattern = ("(chapter (?:[a-z]{1,}))\s+" +
                   "([a-z', .-]+)\\b(?![a-z]+(?=\.)\\b)"+"(?![a-z']|[A-Z.])"+"(.*?)")

        hp = defaultdict(dict)
        chapters = re.findall(pattern, book, re.DOTALL)
        chap = 0

        for chapter in chapters:
            chap += 1
            chap_title = chapter[1].replace('\n', '')
            chap_text = chapter[2][3:]
            print(chap_title)

            hp[book_title]['Chapter ' + str(chap)] = (chap_title, chap_text)

        hp = dict(hp)
        for chapter in hp[book]:
            print('   ', chapter, hp[book][chapter][0])


if __name__ == "__main__":

    alice = WonderlandMember.hero()
    url_first_book = 'https://gist.githubusercontent.com/phillipj/4944029/raw/75ba2243dd5ec2875f629bf5d79f6c1e4b5a8b46/alice_in_wonderland.txt'
    first_book = alice.get_raw_book(url_first_book)
    url_second_book = 'https://raw.githubusercontent.com/GITenberg/Through-the-Looking-Glass_12/master/12-0.txt'
    second_book = alice.get_raw_book(url_second_book)
    # print(first_book)
    alice.get_42_inbooks(first_book, 'Alice')
