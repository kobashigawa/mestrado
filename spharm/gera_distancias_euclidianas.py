# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 13:44:02 2021

gera arquivos em dicionario comparando distancias Euclidianas entre objs spharm 

@author: kobashi
"""


import sys
sys.path.append("..") # Adds higher directory to python modules path.
import pickle
import spharm


def gera_txt(obj):    
    
    dicti = {}
    vc_i = [0]
    vc_obj = spharm.vetor_caract(obj)
    for i in(range(381)):
        if i != 0:            
            vc_i = spharm.vetor_caract(i)
            if vc_i == [0]:
                print('opa, ', i)
            d = spharm.distancia_euclidiana(vc_obj, vc_i)
            dicti[i] = d
            
    # #salvar dicionario em arquivo pickle 
    file = str(obj) + '.txt'
    with open(file, 'wb') as handle:
      pickle.dump(dicti, handle)
    print('pickle', obj)
            


# para ler
# with open('1.txt', 'rb') as handle:
#   dict_pickle = pickle.loads(handle.read())
#   print(dict_pickle)
    
for i in(range(381)):
    if i > 335:
        gera_txt(i)
        
        