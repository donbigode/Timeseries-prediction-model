import pandas as pd
import numpy
import glob
import openpyxl
import os


####################
##     Caminhos
##     Arquivos
####################
path_Venda_produtos_tratados = "C://Users/otavi/OneDrive/Codes/Codes/Parser_ETL/Venda_produtos_tratados/"
caminho_DF = "C://Users/otavi/OneDrive/Codes/Codes/Parser_ETL/Merge/"
path_Inventario_produtos_tratados = "C://Users/otavi/OneDrive/Codes/Codes/Parser_ETL/inventario_produtos_tratados/"

#######################
#Analisador de dados
#
######################


def cria_dataframe(*kargs):
    os.chdir(*kargs)
    loct_doc = []
    df_final = pd.DataFrame()
    for doc in glob.glob("*.xls"):
        arquivo_lido = pd.read_excel(doc)
        #for x in arquivo_lido.rows():
          #  arquivo_lido = arquivo_lido.col[x].str()
        df_final.append(arquivo_lido)
    df_final = df_final.to_excel(caminho_DF)




######################
##       Main
##
######################



if __name__ == "__main__":
 
pass
