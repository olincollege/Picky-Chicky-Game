# Picky-Chicky-Game

### Summary

Welcome to Picky Chicky! In this game, you will help Chicky - who is quite picky - to obtain the worm and avoid the spider. Catching each worm will get you a point, but beware: catching a single spider will end the game, as you have disappointed Chicky.


### Installation

To play *Picky Chicky*, you will need to installation the Pygame library in Python. You can install Python [here](https://www.python.org/downloads/) and Pygame [here](https://www.pygame.org/wiki/GettingStarted).

### Usage

Download the files in the Picky Chicky Game repository from Github [here](https://github.com/olincollege/Picky-Chicky-Game/), and navigate to the Picky Chicky folder in the terminal. Run `python game.py` to start the game.

### Instructions:

Use the left and right arrow keys to move Chicky. Collecting each worm will get you a point, but colliding with a spider will end the game, so make sure you avoid them!

### Linting with Pylint

When linting this code with pylint, use the `--unsafe-load-any-extension=y` argument. This is because pylint does not load the C extensions from `pygame` by default, and will throw errors around methods imported from pygame. 

For example, to run pylint on game.py, run the following in your command line: `pylint --unsafe-load-any-extension=y game.py`.

### Contributors

*Kei Chua, Olin College of Engineering
*Sreednidhi Chalimadugu, Olin College of Engineering
