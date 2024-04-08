import random
import os
from math import sqrt
from myproject.create_word import *
import string

HORIZONTAL = 0
VERTICAL = 1

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def get_random_letter():
	return alphabet[random.randint(0, len(alphabet)-1)]

class WordGrid:
    def __init__(self, width):
        self.grid = []
        self.width = width
        self.area = width**2
        self.cheated = False

        for col in range(self.area):
            self.grid.append(get_random_letter())

        self.available_spots = []
        for spot in range(self.area):
            self.available_spots.append(True)

    def generate_with_words(self,words):
        if self.can_generate(words):
            for word in words:
                finded_place = False
                attempt = 0
                while not finded_place and attempt <=100:
                    random_direction = random.choice([HORIZONTAL, VERTICAL])
                    random_x = random.randint(0, self.width-1)
                    random_y = random.randint(0, self.width-1)

                    if random_x + len(word) > self.width and random_direction == HORIZONTAL:
                        random_x -= (random_x + len(word)) - self.width
                    if random_y + len(word) > self.width and random_direction == VERTICAL:
                        random_y -= (random_y + len(word)) - self.width
                    
                    if self.is_placeable(word, random_x, random_y, random_direction):
                        self.place_word(word, random_x, random_y, random_direction)
                        finded_place = True
                    
                    attempt +=1
        
            if attempt >= 100:
                exit()
            else:
                puzzle = self.print()
                return puzzle


    def place_word(self, word, x, y, direction):
        for l in range(len(word)):
            if direction == HORIZONTAL:
                # place horizontally
                self.grid[x+l + y * self.width] = "\033[32m" + word[l] + "\033[0m" if self.cheated else word[l]
                self.available_spots[x+l + y * self.width] = False # making the horizontal spot unavaliable
            elif direction == VERTICAL:
                # place vertically
                self.grid[x + (y+l) * self.width] = "\033[32m" + word[l] + "\033[0m" if self.cheated else word[l]
                self.available_spots[x + (y+l) * self.width] = False # making the vertical spot unavaliable
    
    def is_placeable(self, word, x, y, direction):
        for l in range(len(word)):

            # getting the current letter (cheated or not)
            letter = "\033[32m" + word[l] + "\033[0m" if self.cheated else word[l]

            # CHECKING FOR WORD CROSSING
            # checking if the letter is on the next spot, even if already with a letter from another word placed
            # that way we can make word crossings
            if direction == HORIZONTAL:
                if self.grid[x+l + y * self.width] == letter:
                # marks the available spot true again (possibly being false before, because of a letter from another word occupying it)
                # then the current letter on this loop will overlap the same letter from the other word
                    self.available_spots[x+l + y * self.width] = True
            else:
                if self.grid[x + (y+l) * self.width] == letter:
                    self.available_spots[x + (y+l) * self.width] = True

            # at the end, check if the spot is available or not
            spot_available = self.available_spots[x+l + y * self.width] if direction == HORIZONTAL else self.available_spots[x + (y+l) * self.width]

            if spot_available:
                continue
            # if a spot is unavaliable, then is not placeable, returns false 
            else:
                return False
    # if the loop finishes without returning false, it means that is placeable, returns true
        return True
    
    def can_generate(self, words):
        letter_count = 0
        for word in words:
            for letter in word:
                letter_count += 1
                # if there are much more letters than the grid area
                if letter_count > self.area:
                    return False
            if len(word) > self.width:
                return False
        return True
        
    def print(self):
        board = []
        board.append("┌" + ("─"*(2*(self.width)+1)) + "  ┐") # just a nice little line
        for y in range(self.width):
            row = "│" + " "# |
            for x in range(self.width):
                row = row + " " + self.grid[x + y * self.width] + " "
            row  = row + "│" # |
            board.append(row)
        board.append("└" + ("─"*(2*(self.width)+1)) + "  ┘" )
        return board


print('Hello world')

