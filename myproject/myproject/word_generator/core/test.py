from word_search import WordSearch
from myproject.myproject.create_word import *

'''
from create_word import *
course = 'math'
lesson = 'plus'
grade = '5'
answer = False
words = generate_related_words(course, lesson, grade)
puzzle = WordSearch(words)
puzzle.save("puzzle.pdf", solution=answer)
'''

# createPuzzle function to generate word search board
def createPuzzle(course, lesson, grade):
    words = generate_related_words(course, lesson, grade)
    puzzle = WordSearch(words)
    puzzle.show(solution=True)
    puzzle.save("puzzle.pdf", solution=True)

# Eg
course = 'math'
lesson = 'plus'
grade = '5'
# test createPuzzle function
# createPuzzle(course, lesson, grade)