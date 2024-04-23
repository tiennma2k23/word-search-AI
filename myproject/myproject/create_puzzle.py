from word_search_generator import WordSearch
from .create_word import *

# createPuzzle function to generate word search board
def createPuzzle(course, lesson, grade, withAns):
    words = generate_related_words(course, lesson, grade)
    puzzle = None
    if withAns == False:
        puzzle = WordSearch(secret_words=words)
    else:
        puzzle = WordSearch(words)
    return puzzle

# Eg
course = 'math'
lesson = 'plus'
grade = '5'
# test createPuzzle function
test = createPuzzle(course, lesson, grade, withAns=True)
print(test)