from create_puzzle import *
from create_word import *
import fpdf

size = 16

def convert_2_pdf(course, lesson, grade):
    words = generate_related_words(course, lesson, grade)
    puzzle = WordGrid(size)
    board = puzzle.generate_with_words(words)
    pdf = fpdf.FPDF(format='A4')
    pdf.add_font("DejaVu", "", "D:\VSC\word-search-AI\env\myproject\DejaVuSans.ttf", uni=True)
    pdf.add_page()
    pdf.set_font("DejaVu", size=12)
    

    for i in range(0, len(words), 5):
        pdf.write(5,' '.join(words[i:i+5]))
        pdf.ln()
        
    for i in board:
        pdf.write(5,i)
        pdf.ln()

    pdf.output("testing.pdf")
    
