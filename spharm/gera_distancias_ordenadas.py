# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 15:06:49 2021

AUC de distância spharm

@author: kobashi
"""



from sklearn.metrics import auc
from matplotlib import pyplot
import pickle
import numpy as np


def ordena_dict(dict_distancia):  
    '''
    funcao auxiliar q ordena dicionario e devolve a lista dos objs ordenados em ordem crescente

    Parameters
    ----------
    dict_distancia : TYPE
        dicionario com numero do obj e seu VC.

    Returns
    -------
    lista : TYPE
        DESCRIPTION.

    '''
      
    lista = list(range(1, 381)) 
    
    #print('lista = ', lista)
    
    #ORDENACAO    
    for passnum in range(len(lista)-1,0,-1):
        for i in range(passnum):
    
            # print('dict_distancia[lista[i]] = ', dict_distancia[lista[i]])
            # print('dict_distancia[lista[i + 1]] = ', dict_distancia[lista[i + 1]])
            if dict_distancia[lista[i]] > dict_distancia[lista[i + 1]]:  
          
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
    
    #imprime lista ordenada pela ordem inventada 
    #print(lista)
    return lista


#ordenacao nlogn
def mergeSort(alist):
#https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OMergeSort.html
    #print("Splitting ",alist)
    
    if len(alist)>1:
        
        # para monitoramento
        print(len(alist))
        
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            #if lefthalf[i] > righthalf[j]:           
           
            if ordem_invent_todos_objetos.ordem_inventada(spharm.vetor_caract(lefthalf[i]), spharm.vetor_caract(righthalf[j])) == -1:                
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    #print("Merging ",alist)
    return alist



# rotina para gerar listas de distancias em ordem crescente
for i in(range(381)):
    if i > 0:        

        #pega arquivo de distancias do objeto i
        file = 'dist_manhattan/' + str(i) + '.txt'        
        with open(file, 'rb') as handle:
            dic = pickle.loads(handle.read())   
            #print(dic)          
            #devolve uma lista ordenada com o numero de objs em ordem crescente
            lista_ordenada = ordena_dict(dic)            
            #print(lista_ordenada)
            
            #salvar lista ordenada em arquivo pickle 
            #file = 'dist_eucli_ordenadas/' + str(i) + '.txt'
            file = 'dist_manhattan_ordenadas/' + str(i) + '.txt'
            with open(file, 'wb') as handle:
              pickle.dump(lista_ordenada, handle)
              print(i)
              #print(lista_ordenada)





