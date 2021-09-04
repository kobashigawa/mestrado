# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 23:22:15 

gera .txt de dicionario com objeto (numero dele) e VC.
Para usar quando quiser criar uma lista com coeficiente diferente do que ja existe.

@author: kobashi
"""

import sys
sys.path.append("..") # Adds higher directory to python modules path.
import automatizador
import matplotlib.pyplot as plt
import pickle


#retorna vetor de caracteristicas 
def gera_vetor_caract(file, coef):   
  
    temp_file = 'C:/Users/thiag/Google Drive/cbir3d_kobashi/CSDescriptor/temp.txt'
    
    ma = automatizador.gera_matriz_caracteristicas(file, coef, temp_file)
    
    vetor = automatizador.eixo('X', ma) + automatizador.eixo('Y', ma) + automatizador.eixo('Z', ma)
    return vetor


def gera_dict(obj_inicial, objs, coef):       
    ''' gera dicionario com objeto (numero da malha) e seu VC. 
    objs = quantidade de elementos para gerar o dicionario, sendo q se for 20, pega ate o 19
    380: array([-1.90298375e-02,  3.43923593e+01, -4.42146253e+00, -4.21029093e+00,'''
    
    thisdict = {}
    repo = 'C:/Users/thiag/Google Drive/cbir3d_kobashi/off/'

    for x in range(objs):
    
        obj = obj_inicial + x        
        file = repo + str(obj) + '.off'
    
        d = gera_vetor_caract(file, coef)
        thisdict[obj] = d
        print(obj)
    return thisdict



#gera dict de todos objetos. 40min pra gerar 
# dict_tudo = gera_dict(1, 380, 50)

# #salvar dicionario em arquivo pickle 
# with open('dic_coef_100.txt', 'wb') as handle:
#   pickle.dump(dict_tudo, handle)
# print('pickle gerado')
        
# with open('dic.txt', 'rb') as handle:
#   dict_pickle = pickle.loads(handle.read())

# print(dict_pickle)
        
