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
import json

##
###config = {"path_Venda_produtos": "Venda_source",
###          "path_Venda_produtos_tratados ": "Venda_target",
###          "path_Inventario_produtos": "Inv_source",
###          "path_Inventario_produtos_tratados": "Inv_target"}

###
###with open('../paths/path_config.json', 'w') as f:
###    json.dump(config, f)


'''
import multiprocessing as mp
from multiprocessing import process

'''


#########################################
#Author: Otavio Geraldo               ###
#GitHub: Donbigode                    ###
#########################################

"""
##########################################
## Para Ajustar os dados                ##
## Belas artes - Dados Diários          ##
##########################################
"""

'''
#####################################################################################################
########################################## Caminhos #################################################
#####################################################################################################
'''
# Path leitura de arquivos
## Arquivos de Venda

path_Venda_produtos = "C://Users//otavi//clone_repo//Belas Artes Dados//Belas Artes Dados//Extrato_Mov_prod"
path_Venda_produtos_tratados = "C://Users//otavi//clone_repo//Belas Artes Dados//Belas Artes Dados//Extrato_Mov_prod//Tratados"
## Arquivos de Inventário e Movimentação
path_Inventario_produtos = "C://Users/otavi/OneDrive/Codes/OngoingDev/Parser_ETL/movimentação_produtos/"
path_Inventario_produtos_tratados = "C://Users/otavi/OneDrive/Codes/OngoingDev/Parser_ETL/movimentação_produtos/tratados/"

#PATH para salvamento - Database
#DB incremental
##DB_DemandaPath = "C://Users/otavi/Codes/Parser_ETL/Tbl_fact/produto_venda_consolidado.xlsx"


DB_tratados = "C://Users//otavi//clone_repo//Belas Artes Dados//Dados//Extrato_Mov_prod//consolidados"

######################################################################################################
########################################  Functions  #################################################
######################################################################################################


####################### Append Treated Data ##########################################################
def append_dados_venda(path):
    df_consolidador = pd.DataFrame()
    now = datetime.now()
    os.chdir(path)

    for base_ext in glob.glob("*.csv"):
        df_check = pd.read_csv(base_ext)
        df_consolidador = df_consolidador.append(df_check, ignore_index=True)

        print("Tabela Consolidada com tamanho {0}".format(
            len(df_consolidador)))
    df_consolidador.to_excel("{0}venda_produto_consolidado_{1}.xlsx" .format(
        DB_tratados, now.strftime("%d%m%Y")))
    print('Finalizada a consolidação.\n')


def append_dados_movint(path):
    df_consolidador = pd.DataFrame()
    now = datetime.now()

    df_consolidador

    os.chdir(path)

    for base_ext in glob.glob("*.csv"):
        df_check = pd.read_csv(base_ext)
        df_consolidador = df_consolidador.append(df_check, ignore_index=True)

        print("Tabela Consolidada com tamanho {0}".format(
            len(df_consolidador)))
    df_consolidador.to_csv("{0}mov_prod_consolidado_{1}.csv" .format(
        DB_tratados, now.strftime("%d%m%Y")))
    print('Finalizada a consolidação.\n')
######################################################################################################

############## Tratamento ############################################################################



#     os.chdir(path)
#     for file in glob.glob("*.xls"):
#         date_split = file.replace('MP-', '').replace('venda', '').replace(
#             'produto', '').replace('movint', '').replace('_', '').replace('.xls', '')
#         #date_split2 = file.replace('xpt_tbl_','').replace('venda','').replace('produto','').replace('movint','').replace('.xls','').replace("_","")
#         #Inclui o split dos meses no df a ser tratado
#         df = pd.read_excel(file)
#         df['Data'] = date_split
#         #df['Mês'] = date_split[0]
#         #df['Ano'] = date_split[1]
#         #df['Mês/Ano'] = date_split2
#         #Criando chave ''unica'
#         df['insertion_id'] = [random.randint(
#             1000000, 10000000000) for k in df.index]
#         df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')
#         df['Data_Mov'] = pd.to_datetime(df['Data_Mov'], format='%d/%m/%Y')
#         df['Data_Mov'] = df['Data_Mov'].dt.strftime('%Y-%m-%d')
def trata_dados_movit_prod(path):
    os.chdir(path)
    for file in glob.glob("*.xls"):
        date_split = file.replace('MP-', '').replace('venda', '').replace(
            'produto', '').replace('movint', '').replace('_', '').replace('.xls', '')
        date_split2 = file.replace('xpt_tbl_','').replace('venda','').replace('produto','').replace('movint','').replace('.xls','').replace("_","")
        #Inclui o split dos meses no df a ser tratado
        df = pd.read_excel(file)
        df['Data'] = date_split
        df['Mês'] = date_split[0]
        df['Ano'] = date_split[1]
        df['Mês/Ano'] = date_split2
        #Criando chave ''unica'
        df['insertion_id'] = [random.randint(
            1000000, 10000000000) for k in df.index]
        df['Data'] = pd.to_datetime(df['Data'], format='%d-%m-%Y')
    
        df.to_csv("{0}/tratados/{1}_tratado.csv" .format(path,
                  file.replace(".xls", "")))

        print("Arquivos na Pasta: {0}, Mês referência: {1}: tratamento bem sucedido!\n" .format(
            file, date_split))


################### TASKS ############################


##################################################################################################
#####################################    Main     ################################################
##################################################################################################

if __name__ == "__main__":
    trata_dados_movit_prod(path_Venda_produtos)
    #trata_dados_movit_prod(path_Inventario_produtos)
    append_dados_venda(path_Venda_produtos_tratados)
    #append_dados_movint(path_Inventario_produtos_tratados)
pass
