import pandas as pd
import ntpath
import os
import unicodedata

## Classe para criação de dataframes 
## Classe para criação de dataframes 
class read_file():
    def __init__(self, file_name):
        self.file_name = file_name
        self.df = pd.read_excel(self.file_name,engine='openpyxl', index_col = 0)
        self.df.columns = [label.replace(' ', '_') for label in self.df.columns]
        self.df.columns = [label.replace('/', '_') for label in self.df.columns]
        self.df.columns = [label.replace('-', '_') for label in self.df.columns]
        self.df.columns = [label.replace('(', '_') for label in self.df.columns]
        self.df.columns = [label.replace(')', '_') for label in self.df.columns]
        self.df.columns = [label.replace('.', '_') for label in self.df.columns]
        self.df.columns = [label.replace(',', '_') for label in self.df.columns]
        self.df.columns = [label.replace(';', '_') for label in self.df.columns]
        self.df.columns = [label.replace(':', '_') for label in self.df.columns]
        self.df.columns = [label.replace('?', '_') for label in self.df.columns]
        self.df.columns = [label.replace('!', '_') for label in self.df.columns]
        self.df.columns = [label.replace('#', '_') for label in self.df.columns]
        self.df.columns = [label.replace('$', '_') for label in self.df.columns]
        self.df.columns = [label.replace('%', '_') for label in self.df.columns]
        self.df.columns = [label.replace('^', '_') for label in self.df.columns]
        self.df.columns = [label.replace('&', '_') for label in self.df.columns]
        self.df.columns = [label.replace('*', '_') for label in self.df.columns]
        self.df.columns = [label.replace('(', '_') for label in self.df.columns]
        self.df.columns = [label.replace(')', '_') for label in self.df.columns]
        self.df.columns = [label.replace('+', '_') for label in self.df.columns]
        self.df.columns = [label.replace('=', '_') for label in self.df.columns]
        self.df.columns = [label.lower() for label in self.df.columns]
        self.df.columns = [label.replace('á', 'a') for label in self.df.columns]
        self.df.columns = [label.replace('é', 'e') for label in self.df.columns]
        self.df.columns = [label.replace('í', 'i') for label in self.df.columns]
        self.df.columns = [label.replace('ó', 'o') for label in self.df.columns]
        self.df.columns = [label.replace('ú', 'u') for label in self.df.columns]
        self.df.columns = [label.replace('ç', 'c') for label in self.df.columns]
        self.df.columns = [label.replace('ã', 'a') for label in self.df.columns]
        self.df.columns = [label.replace('õ', 'o') for label in self.df.columns]
        self.df.columns = [label.replace('â', 'a') for label in self.df.columns]
        self.df.columns = [label.replace('ê', 'e') for label in self.df.columns]
        self.df.columns = [label.replace('ô', 'o') for label in self.df.columns]
        self.df.columns = [label.replace('ì', 'i') for label in self.df.columns]
        self.df.columns = [label.replace('ù', 'u') for label in self.df.columns]
        self.df.columns = [label.replace('à', 'a') for label in self.df.columns]
        self.df.columns = [label.replace('è', 'e') for label in self.df.columns]
        self.df.columns = [label.replace('ì', 'i') for label in self.df.columns]
        self.df.columns = [label.replace('ò', 'o') for label in self.df.columns]
        self.df.columns = [label.replace('ù', 'u') for label in self.df.columns]

    def get_df(self):
        return self.df

    def get_file_name(self):
        return self.file_name
    
    def clean_df(self):
        self.df.dropna(inplace=True)
        self.df.drop_duplicates(inplace=True)
        self.df.reset_index(drop=True, inplace=True)
        return self.df
    
    def get_df_columns(self):
        return self.df.columns
    

    def get_file_path(self):
        return os.path.dirname(self.file_name)

    def get_file_name_without_extension(self):
        return ntpath.basename(self.file_name).split('.')[0]

    def get_file_name_with_extension(self):
        return ntpath.basename(self.file_name)

    def get_file_name_extension(self):
        return ntpath.basename(self.file_name).split('.')[1]

    def get_file_name_without_extension_and_path(self):
        return ntpath.basename(self.file_name).split('.')[0]

    def get_file_name_with_extension_and_path(self):
        return self.file_name

    def get_file_name_extension_and_path(self):
        return ntpath.basename(self.file_name).split('.')[1]

    def get_file_name_without_extension_and_path_and_separator(self):
        return ntpath.basename(self.file_name).split('.')[0].replace('\\', '/')

    def get_file_name_with_extension_and_path_and_separator(self):
        return self.file_name.replace('\\', '/')

    def get_file_name_extension_and_path_and_separator(self):
        return ntpath.basename(self.file_name).split('.')[1].replace('\\', '/')

    def get_file_name_without_extension_and_path_and_separator_and_dot(self):
        return ntpath
