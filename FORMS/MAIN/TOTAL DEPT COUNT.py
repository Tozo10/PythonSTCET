import pandas as pd

def count_elements(file_name,  column_name):
    df = pd.read_excel(file_name)
    return df[column_name].value_counts()

file_name = 'students.xlsx'
column_name = 'Department'

element_counts = count_elements(file_name, column_name)
for element, count in element_counts.items():
    print(f"{element}: {count}")
