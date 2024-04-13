from word_search_generator import WordSearch

from create_word import *

course = 'math'
lesson = 'plus'
grade = 'grade 5'
words = generate_related_words(course, lesson, grade)
puzzle = WordSearch(words)
puzzle.show()
puzzle.save(path="D:\word-search-AI\env\myproject\myproject\puzzle.pdf")