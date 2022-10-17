# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 13:44:02 2021

gera arquivos em dicionario comparando distancias Euclidianas entre objs spharm 

@author: kobashi
"""


import sys
import pickle
import spharm_1343


def gera_txt(obj):    
    '''
    gera .txt contendo distancias Euclidiana entre o obj parametro e os todos outros 380 objs 

    Parameters
    ----------
    obj : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
    
    
    dicti = {}
    vc_i = [0]
    vc_obj = spharm_1343.vetor_caract(obj)
    for i in(range(381)):
        if i != 0:            
            vc_i = spharm_1343.vetor_caract(i)
            if vc_i == [0]:
                print('opa, ', i)
            d = spharm_1343.distancia_euclidiana(vc_obj, vc_i)
            dicti[i] = d
            
    # #salvar dicionario em arquivo pickle 
    file = 'dist_euclidiana/' + str(obj) + '.txt'
    with open(file, 'wb') as handle:
      pickle.dump(dicti, handle)
    print(obj)


# para ler
# with open('1.txt', 'rb') as handle:
#   dict_pickle = pickle.loads(handle.read())
#   print(dict_pickle)
    
for i in(range(381)):
    if i > 0:
        gera_txt(i)
        
        