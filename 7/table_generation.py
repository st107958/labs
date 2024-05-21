import pandas as pd
from docx import Document


def format_number(value):
    try:
        return f"{float(value):.5f}"
    except ValueError:
        return str(value)


df = pd.read_csv('result1.csv', header=None)

doc = Document()

table = doc.add_table(rows=1, cols=len(df.columns))
column_names = ['№', 'U_eb', 'U_kb', 'I_k', 'ln_I_k']

header_cells = table.rows[0].cells
for i, column_name in enumerate(column_names):
    header_cells[i].text = column_name

for index, row in df.iterrows():
    row_cells = table.add_row().cells
    for i, cell_value in enumerate(row):
        row_cells[i].text = format_number(cell_value)

doc_file = 'output.docx'
doc.save(doc_file)

