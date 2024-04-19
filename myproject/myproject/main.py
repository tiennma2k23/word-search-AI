from word_search_generator import WordSearch
from .create_word import *


course = 'math'
lesson = 'plus'
grade = '5'
def createPuzzle(course, lesson, grade):
    words = generate_related_words(course, lesson, grade)
    puzzle = WordSearch(words)
    # puzzle.show()
    puzzle.save(path="D:/VSC/word-search-AI/myproject/myproject/puzzle.pdf")
    return puzzle

