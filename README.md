# PyDayBCN 

All generous trips & tricks, courtesy of Dj Pato

(Put the music on!)



Quotes to remember:
Lewis Carroll was a Victorian nerd, we can easily think of him as a python user :)



Roadmap:
- Itroduction (Who)
    - github profile
    - likedin profile (just to be sure to be caught up on the internet)
- Motivation (Why)
    - Alice in Wonderland books, on reading recreational maths (is it really funny?)
    - How and why 42 is the geek's number?
        - Adams....maybe
        - ...Carroll for sure
    - Learning OOP 
- Topic Presentation (What)
    - game hidden in Alice
- Slide presentation (How)
    - class
      initialize Wonderland characters
    - repr and/or string
      why is important to use repr and str and differences
    - instance method, static method, class method
      define some methods for reading quotes and find the number 42 in the book
    - property decorator
      assign the author to the class
    - getter/setter
      dobouts
    - inheritance
      initialize Rules class, child class of Wonderland
      initialize Dialog class, child class of Moltiplication Table class
    - decorator, functool.wrapper
    - data class
      define players and check that the first player is always Alice
    - nametuple, typing
      #ToDo
    - if name === main
    - annotation and docstring (google version)
- Extra
    - drawing with my supercool unused wacom
        - skeches of stickmans with laptops
        - quotes 
        - stickers, meme (ask Miguel), jokes 

## Description

This repo contains:
- slide for the PyDayBCN 
- module

## Installation

### Create an enviroment

How to create and enviroment:

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