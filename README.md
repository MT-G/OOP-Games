# OOP in Lewis Carroll's Games

## Description

| Game     | Description | Code    |
| :---        |    :----:   |          ---: |
| 42 Riddle    | multilication table        | [lets_play.py](lets_play.py)   |
| Guess Number  | algo for guessing an integer      | [guess_number.py](guess_number.py)     |
| Find Day of the Week    | algo for finding the day of the week given the date       | [day_of_the_week.py](day_of_the_week.py)   |


| Code     | Description | 
| :---        |    :----:   |   
| [characters.py](characters.py)    | define characters        | 
| [raw_book.py](raw_book.py)  | get book from Project Gutenberg      | 
| [players.py](players.py)    | define players of the game       | 

## PyDayBCN 2020

Slide for presentation at PyDayBCN 2020 can be found [here](slides.ipynb)

## Installation

### Create an enviroment

How to create an enviroment:

```console
conda env create -n carrollgames -f environment.yml

```
where ```carrollgames``` is the name of the local enviroment.

How to activate the enviroment:

```console
conda activate carrollgames

```
### Install or remove packages from the environment

How to edit ```environment.yml```, add or remove packages:

```console
conda env update --file environment.yml  --prune

```
prune works also if you don't delite packages from your file ```environment.yml```

## Project Gutenberg License

The books used in this repository are in the Public Domain, see the [Project Gutenber License](project_gutenber_license.txt) for details.

### About Project Gutenberg

Project Gutenberg is a project to collect and archive public domain texts.
Please see [Projcet Gutenberg Site](https://www.gutenberg.org/)

## License

This repository is under [MIT License](licence.txt).