import os
import pandas as pd
import openpyxl
import numpy as np
from datetime import date, datetime, timedelta
from pandas.core.reshape.concat import concat
import glob2
import glob
import random
import ntpath

'''
import multiprocessing as mp
from multiprocessing import process

'''



#########################################
#Author: Otavio Geraldo               ###
#GitHub: Donbigode                    ###
#########################################

"""
###########################
## Para Ajustar os dados ##
## Belas artes           ##
###########################
"""

'''
#####################################################################################################
########################################## Caminhos #################################################
#####################################################################################################
'''
# Path leitura de arquivos
## Arquivos de Venda
path_Venda_produtos = "C://Users/otavi/OneDrive/Codes/OngoingDev/Parser_ETL/venda_produtos/"
path_Venda_produtos_tratados = "C://Users/otavi/OneDrive/Codes/OngoingDev/Parser_ETL/venda_produtos/tratados/"
## Arquivos de Inventário e Movimentação
path_Inventario_produtos = "C://Users/otavi/OneDrive/Codes/OngoingDev/Parser_ETL/movimentação_produtos/"
path_Inventario_produtos_tratados = "C://Users/otavi/OneDrive/Codes/OngoingDev/Parser_ETL/movimentação_produtos/tratados/"

#PATH para salvamento - Database 
#DB incremental
DB_DemandaPath = "C://Users/otavi/Codes/Parser_ETL/Tbl_fact/produto_venda_consolidado.xlsx"


DB_tratados = "C://Users/otavi/OneDrive/Codes/OngoingDev/PARSER_ETL/Consolidado/"

######################################################################################################
########################################  Functions  #################################################
######################################################################################################



####################### Append Treated Data ##########################################################
def append_dados_venda(path):
    df_consolidador = pd.DataFrame()
    now = datetime.now() 
    os.chdir(path)
    
    for base_ext in glob.glob("*.xlsx"):
        df_check = pd.read_excel(base_ext)
        df_consolidador = df_consolidador.append(df_check,ignore_index= True)
        
        print("Tabela Consolidada com tamanho {0}".format(len(df_consolidador)))
    df_consolidador.to_excel("{0}venda_produto_consolidado_{1}.xlsx" .format(DB_tratados,now.strftime("%d%m%Y")))
    print('Finalizada a consolidação.\n')   

def append_dados_movint(path):
    df_consolidador = pd.DataFrame()
    now = datetime.now()
    
    df_consolidador 
    
    os.chdir(path)
    
    for base_ext in glob.glob("*.xlsx"):
        df_check = pd.read_excel(base_ext)
        df_consolidador = df_consolidador.append(df_check,ignore_index= True)
        
        print("Tabela Consolidada com tamanho {0}".format(len(df_consolidador)))
    df_consolidador.to_excel("{0}movint_produto_consolidado_{1}.xlsx" .format(DB_tratados,now.strftime("%d%m%Y")))
    print('Finalizada a consolidação.\n')    
######################################################################################################

############## Tratamento ############################################################################
def trata_dados_movit_prod(path):
    os.chdir(path)
    for file in glob.glob("*.xls"):
        date_split = file.replace('xpt_tbl_','').replace('venda','').replace('produto','').replace('movint','').replace('_','').replace('.xls','').split("-")
        date_split2 = file.replace('xpt_tbl_','').replace('venda','').replace('produto','').replace('movint','').replace('.xls','').replace("_","")
        #Inclui o split dos meses no df a ser tratado    
        df = pd.read_excel(file)
        df['Mês'] = date_split[0]
        df['Ano'] = date_split[1]
        df['Mês/Ano'] = date_split2
        #Criando chave ''unica'
        df['insertion_id'] = [random.randint(1000000,10000000000) for k in df.index]
        df.to_excel("{0}/tratados/{1}_tratado.xlsx" .format(path,file.replace(".xls","")))
        
        print("Arquivos na Pasta: {0},{1}: tratamento bem sucedido!\n" .format(file,date_split))


################### TASKS ############################



##################################################################################################
#####################################    Main     ################################################
##################################################################################################


if __name__ == "__main__":
   # trata_dados_movit_prod(path_Venda_produtos)
   # trata_dados_movit_prod(path_Inventario_produtos)
    append_dados_venda(path_Venda_produtos_tratados)
    append_dados_movint(path_Inventario_produtos_tratados)
pass

