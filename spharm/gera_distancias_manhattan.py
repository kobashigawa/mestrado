# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 22:55:40 2021

@author: kobashi
"""



import sys
sys.path.append("..") # Adds higher directory to python modules path.
import pickle
import spharm


def gera_txt(obj):    
    '''
    gera .txt contendo distancias de Manhattan entre o obj parametro e os todos outros 381 objs 

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
    vc_obj = spharm.vetor_caract(obj)
    for i in(range(381)):
        if i != 0:            
            vc_i = spharm.vetor_caract(i)
            if vc_i == [0]:
                print('opa, ', i)
            d = spharm.distancia_manhattan(vc_obj, vc_i)
            dicti[i] = d
            
    # #salvar dicionario em arquivo pickle 
    file = 'dist_manhattan/' + str(obj) + '.txt'
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
        
        