from myproject.word_generator.word_search import WordSearch
from myproject.word_generator.create_word import *
from myproject.word_generator.shapes import *
import os

# createPuzzle function to generate word search board
def createPuzzle(course, lesson, grade, shape, level):
    # create puzzle
    words = generate_related_words(course, lesson, grade)
    puzzle = WordSearch(words, level = level)
    puzzle.apply_mask(shape())
    puzzle.show
    return puzzle


# Eg
'''
course = 'math'
lesson = 'plus'
grade = '5'
answer = False
shape = Heart
level = 4
test = createPuzzle(course, lesson, grade, shape, level)
'''