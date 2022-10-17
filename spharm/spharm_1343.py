# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 20:27:11 2021

ler .txt com VCs gerados pelo SPHARM 

Fazer ordenacao por distancia Euclidiana 

vai ser um processo mto lento, tenho q ir salvando em arquivo
calcular 1 obj em a relacao de distancia entre todos outros 
salvar em arquivo



@author: kobashi
"""


import sys
sys.path.append("..") # Adds higher directory to python modules path.
import matplotlib.pyplot as plt
import pickle
import csv
from scipy.spatial import distance
#import automatizador
import json

def gera_dicionario():
    file = 'vetores_1343.txt'
    
    print('começando')
    
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')    
        
        lista = []
        dicti = {}
        obj = 1
        for row in spamreader:
            for e in row:
                if e != '':
                    lista.append(float(e))
            #print(lista)
            dicti[obj] = lista 
            obj = obj + 1
        
        
    #salvar em file readable - deu 29gb de json    
    # a_file = open("dictionary_spharm.json", "w")
    # json.dump(dicti, a_file)
    # a_file.close()
    # print('cabou')
            
    # #salvar dicionario em arquivo pickle 
    # with open('dict_spharm.txt', 'wb') as handle:
    #   pickle.dump(dicti, handle)
    #   print('pickle gerado')
            
            #print(', '.join(row)) 
            
    
#gera_dicionario()
    
# a_file = open("dictionary_spharm.json", "r")
# output = a_file.read()

# print(output.get(1))

# #print(output)
# a_file.close()        
        

def vetor_caract(o):
    '''
    retorna VC do obj inputado

    ''' 
      
    with open('vetores_1343.txt', 'rb') as handle:
        vetores = pickle.loads(handle.read())       
        return vetores[o - 1]

       
        
# for v in(range(381)):
#     if v > 0:
#         print(len(vetor_caract(v)))
            
# v = vetor_caract(100)
# print(v)

 

def iguala_dimensao(v1, v2):
    ''' o spharm gera VCs de tamanhos diferentes dependendo dos objs. 
    Esta funcao faz 2 vetores terem mesmo tamanho, acrescentando zeros. 
    Feito para calcular medidas de distancia, que precisam de dois vetores de mesma dimensao
    '''
    
    while len(v1) != len(v2):
        if len(v1) < len(v2):
            v1.append(0)
        if len(v1) > len(v2):
            v2.append(0)
    return v1, v2 


def distancia_euclidiana(v1, v2):
    
    #v1, v2 = iguala_dimensao(v1, v2)    
    #d = automatizador.dist_euclidiana(v1, v2)    
    d = distance.euclidean(v1, v2)
    return d


def distancia_manhattan(v1, v2):
    
    #v1, v2 = iguala_dimensao(v1, v2)    
    #d = automatizador.dist_manhattan(v1, v2)  
    d = distance.cityblock(v1, v2)
    return d


# testar dist_Euclidiana
# v1 = vetor_caract(1)
# v2 = vetor_caract(380)
# d = distancia_euclidiana(v1, v2)
# print(d)





# with open('dict_spharm.txt', 'rb') as handle:
#     dict_pickle = pickle.loads(handle.read())      
#     valor = dict_pickle.get(380)    
#     # print(len(valor))
    
#     #d = automatizador.dist_euclidiana(dict_pickle.get(1), dict_pickle.get(300))    
#     #print(d)
    
#     Sum = sum(valor)
#     print(Sum)
    
    # with open('teste.txt', 'wb') as handle:
    #     pickle.dump(valor, handle)
    #     print('pickle gerado')




# def gera_dict(obj_inicial, objs, coef):       
#     ''' gera dicionario com objeto (numero da malha) e seu VC. 
#     objs = quantidade de elementos para gerar o dicionario, sendo q se for 20, pega ate o 19
#     380: array([-1.90298375e-02,  3.43923593e+01, -4.42146253e+00, -4.21029093e+00,'''
    
#     thisdict = {}
#     repo = 'C:/Users/thiag/Google Drive/cbir3d_kobashi/off/'

#     for x in range(objs):
    
#         obj = obj_inicial + x        
#         file = repo + str(obj) + '.off'
    
#         d = gera_vetor_caract(file, coef)
#         thisdict[obj] = d
#         print(obj)
#     return thisdict






# #salvar dicionario em arquivo pickle 
# with open('dic_coef_100.txt', 'wb') as handle:
#   pickle.dump(dict_tudo, handle)
# print('pickle gerado')
        

# with open('dic.txt', 'rb') as handle:
#   dict_pickle = pickle.loads(handle.read())

# print(dict_pickle)
        
