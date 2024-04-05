from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def create_pdf_from_list_of_strings(strings, filename):
    # Tạo một tệp PDF mới
    doc = SimpleDocTemplate(filename, pagesize=letter)

    # Tạo một bảng để chứa dữ liệu từ list of strings
    data = [strings]

    # Thiết lập style cho bảng
    style = TableStyle([('BACKGROUND', (0,0), (-1,0), colors.gray),
                        ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
                        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0,0), (-1,0), 12),
                        ('BACKGROUND', (0,1), (-1,-1), colors.beige),
                        ('GRID', (0,0), (-1,-1), 1, colors.black)])

    # Tạo bảng và áp dụng style
    table = Table(data)
    table.setStyle(style)

    # Thêm bảng vào tài liệu
    doc.build([table])

# Ví dụ list of strings
list_of_strings = [
    ["H", "E", "C", "L", "A", "S", "S", "I", "F", "I", "C", "A", "T", "I", "O", "N"],
    ["K", "O", "M", "M", "X", "D", "H", "E", "U", "R", "I", "S", "T", "I", "C", "S"],
    ["G", "B", "A", "C", "K", "P", "R", "O", "P", "A", "G", "A", "T", "I", "O", "N"],
    ["Y", "W", "I", "Q", "V", "K", "C", "F", "Z", "A", "M", "J", "A", "E", "C", "U"],
    ["K", "H", "A", "U", "X", "B", "Y", "Y", "J", "J", "I", "B", "C", "K", "L", "O"]
]

# Gọi hàm để tạo tập tin PDF từ list of strings
create_pdf_from_list_of_strings(list_of_strings, "output.pdf")