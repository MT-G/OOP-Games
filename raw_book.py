import requests
import mathplotlib.pyplot as plt
import nltk

def get_raw_book(url):

    response = requests.get(url)

    raw = response.text

    return raw

url_book = 'https://gist.githubusercontent.com/phillipj/4944029/raw/75ba2243dd5ec2875f629bf5d79f6c1e4b5a8b46/alice_in_wonderland.txt'
book = get_raw_book(url_book)

def get_plot(book):
    tokens = nltk.word_tokenize(book)
    tokens = [token.lower() for token in tokens]
    text = nltk.Text(tokens)

    plt.figure(figsize=(8, 8))
    text.dispersion_plot(['forty-two'])
    