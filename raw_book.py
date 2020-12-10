"""
File: raw_book.py
Author: MTG
Topic: request
This module implements get a book from Project Gutenber and plot the frequency of a word that apper in the book.
"""

import requests
import matplotlib.pyplot as plt
import nltk

def get_raw_book(url):
    """Request a book from url

    Args:
        url ([type]): website

    Returns:
        txt: text file of the book
    """
    response = requests.get(url)
    raw = response.text
    return raw

def get_plot(book, word):
    """Plot frequency of one word

    Args:
        book ([type]): [description]
    """
    tokens = nltk.word_tokenize(book)
    tokens = [token.lower() for token in tokens]
    text = nltk.Text(tokens)

    plt.figure(figsize=(8, 8))
    text.dispersion_plot([word])

if __name__ == "__main__":
    url_book = 'https://gist.githubusercontent.com/phillipj/4944029/raw/75ba2243dd5ec2875f629bf5d79f6c1e4b5a8b46/alice_in_wonderland.txt'
    book = get_raw_book(url_book)
    get_plot(book, 'forty-two')
    