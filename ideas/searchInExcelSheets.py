import pandas as pd
import os

def search_in_excel(folder_path, keyword):
    for file in os.listdir(folder_path):
        if file.endswith(".xlsx") or file.endswith(".xls"):
            file_path = os.path.join(folder_path, file)
            try:
                excel_data = pd.read_excel(file_path, sheet_name=None)
                for sheet_name, data in excel_data.items():
                    if data.astype(str).apply(lambda x: keyword in x.values, axis=1).any():
                        print(f'\033[91mKeyword "{keyword}" found in file: {file}, sheet: {sheet_name}\033[0m')

                else:
                    print(f'Keyword "{keyword}" not found in file: {file}') 
            except Exception as e:
                print(f"Error reading {file}: {e}")

folder_path = input(r'Enter the path you want to search in: ')
the_keyword = input('Enter the keyword you want to search for: ')

search_in_excel(folder_path, the_keyword)
