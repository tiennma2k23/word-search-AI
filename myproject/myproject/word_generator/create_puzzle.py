from myproject.word_generator.word_search import WordSearch
from myproject.word_generator.create_word import *
import os

# createPuzzle function to generate word search board
def createPuzzle(course, lesson, grade, ans):
    # create puzzle
    words = generate_related_words(course, lesson, grade)
    puzzle = WordSearch(words)
    return puzzle

# Eg
'''
course = 'math'
lesson = 'plus'
grade = '5'
answer = False
test = createPuzzle(course, lesson, grade, answer)
print(test)
'''