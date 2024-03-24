from create_puzzle import *
from create_word import *

size = 16
course_name = "Artificial Intelligence"
lesson_name = "Introduction to Neural Networks"
grade = "Grade 10"
words = generate_related_words(course_name, lesson_name, grade)
puzzle = WordGrid(size)
puzzle.generate_with_words(words)


print("Words:")
for i in range(0, len(words), 5):
    print(' '.join(words[i:i+5]))

