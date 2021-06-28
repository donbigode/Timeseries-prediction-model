import os
import pandas as pd
import openpyxl
import numpy as np
from datetime import date, datetime, timedelta

from pandas.core.reshape.concat import concat
from pyxlsb import open_workbook as open_xlsb
import glob2
import glob
import random

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
path_Venda_produtos = "C://Users/otavi/OneDrive/Codes/Codes/Parser_ETL/venda_produtos/"
path_Venda_produtos_tratados = "C://Users/otavi/OneDrive/Codes/Codes/Parser_ETL/venda_produtos_tratados/"
## Arquivos de Inventário e Movimentação
path_Inventario_produtos = "C://Users/otavi/OneDrive/Codes/Codes/Parser_ETL/movimentação_produtos/"
path_Inventario_produtos_tratados = "C://Users/otavi/OneDrive/Codes/Codes/Parser_ETL/inventario_produtos_tratados/"

#PATH para salvamento - Database 
#DB incremental
DB_DemandaPath = "C://Users/otavi/Codes/Parser_ETL/Tbl_fact/produto_venda_consolidado.xlsx"

######################################################################################################
########################################  Functions  #################################################
######################################################################################################

############## Multi Threading #######################################################################



######################################################################################################

############## Venda Produtos ########################################################################
def trata_dados_venda_prod():
    os.chdir(path_Venda_produtos)
    for file in glob.glob("*.xls"):
        date_split = file.replace(".xls","").replace('xpt',"").replace('tbl',"").replace('venda',"").replace('produto',"").replace("_","").split("-")
        date_split2 = file.replace(".xls","").replace('xpt',"").replace('tbl',"").replace('venda',"").replace('produto',"").replace("_","")
        #Inclui o split dos meses no df a ser tratado    
        df = pd.read_excel(file)
        df['Mês'] = date_split[0]
        df['Ano'] = date_split[1]
        df['Mês/Ano'] = date_split2
        #Criando chave ''unica'
        df['insertion_id'] = [random.randint(1000000,10000000000) for k in df.index]

       # df = new_func(df)
        #Salva o arquivo tratado    
        df.to_excel("{0}{1}_tratado.xlsx" .format(path_Venda_produtos_tratados,file.replace(".xls","")))
        
        print("Arquivos na Pasta: {0},{1}: tratamento bem sucedido!\n" .format(file,date_split))

def new_func(df):
    datatypes_per_column = {
        "Descrição" : "object",
        "Código" : "object",
        "Fornecedor" : "object",
        "Unidade" : "object",
        "Estoque Atual" : "int64",
        "Preço de Venda" : "float64",
        "Custo Unitário" : "float64",
        "Custo Total" : "float64",
        "Preço Total" : "float64",
        "Quant.Venda" : "int64",
        "Descontos"  : "float64",
        "Valor Pago" : "float64",
        "Total Vendas" : "float64",
        "Comissão" : "float64",
        "NCM" : "int64",
        "CEST" : "int64"
        }

    df = df.astype(datatypes_per_column)
    return df




def append_dados():
    df_consolidador = pd.read_excel(DB_DemandaPath)
    
    df_consolidador 
    
    os.chdir(path_Venda_produtos_tratados)
    
    for base_ext in glob.glob("*.xlsx"):
        df_consolidador = df_consolidador.append(str.base_ext,ignore_index= True)
        df_consolidador.to_excel("{0}_atualizado.date.strftime('%d/%m/%Y').xlsx".format(DB_DemandaPath)) 
        print("Tabela Consolidada com tamanho {0}".format(len(df_consolidador)))
######################################################################################################

############## Movimentação Estoque - Produtos #######################################################
def trata_dados_movit_prod():
    os.chdir(path_Inventario_produtos)
    for file in glob.glob("*.xls"):
        date_split = file.replace(".xls","").replace('xpt',"").replace('tbl',"").replace('movint',"").replace('produto',"").replace("_","").split("-")
        date_split2 = file.replace(".xls","").replace('xpt',"").replace('tbl',"").replace('movint',"").replace('produto',"").replace("_","")
        #Inclui o split dos meses no df a ser tratado    
        df = pd.read_excel(file)
        df['Mês'] = date_split[0]
        df['Ano'] = date_split[1]
        df['Mês/Ano'] = date_split2
        #Criando chave ''unica'
        df['insertion_id'] = [random.randint(1000000,10000000000) for k in df.index]

        df.to_excel("{0}{1}_tratado.xlsx" .format(path_Inventario_produtos_tratados,file.replace(".xls","")))
        
        print("Arquivos na Pasta: {0},{1}: tratamento bem sucedido!\n" .format(file,date_split))

def new_func2(df):
    datatypes_per_column = {
        "Produto" : "object",
        "Saldo Inicial" : "object",
        "Entradas" : "object",
        "Devoluções" : "object",
        "Compras" : "int64",
        "Saídas" : "float64",
        "Prêmio" : "float64",
        "Quant. Vendas" : "float64",
        "Valor Vendas" : "float64",
        "Lucro Bruto" : "int64",
        "Estoque Final"  : "float64"
        }

    df = df.astype(datatypes_per_column)
    return df


################### TASKS ############################




##################################################################################################
#####################################    Main     ################################################
##################################################################################################


if __name__ == "__main__":
    Task1 = trata_dados_movit_prod()
    Task2 = trata_dados_venda_prod()
    Vs = [Task1,Task2]
    run_io_tasks_in_parallel(tasks=Vs)
pass


#if __name__ == "__main__":
#    
#    trata_dados_venda_prod()
#    trata_dados_movit_prod()
#    #append_dados()
#pass

