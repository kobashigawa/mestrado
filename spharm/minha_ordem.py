# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 19:21:29 2021

gera lista ordenada com base em minha ordem nos VCs do Spharm

@author: kobashi
"""


#pegar VCs do Spharm, ordenar, gerar lista ordenada

import sys
sys.path.append("..") # Adds higher directory to python modules path.
import spharm
sys.path.append('D:/Google Drive/cbir3d_kobashi/Python/ordem-inventada')
import ordem_invent_todos_objetos
import pickle


def ordena_dict(lista):  
#https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OBubbleSort.html    
    

    #ORDENACAO    
    for passnum in range(len(lista)-1,0,-1):
      
        for i in range(passnum):
                       
                #if lista[i]>lista[i+1]:

                if ordem_invent_todos_objetos.ordem_inventada(spharm.vetor_caract(lista[i]), spharm.vetor_caract(lista[i + 1])) == 1:  
              
                    temp = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = temp
        
    #print(lista)
    return lista




# lista_numeros = list(range(1, 11)) 
# print('lista_numeros:', lista_numeros)
# lista_ordenada = ordena_dict(lista_numeros)
# print('bubble:', lista_ordenada)

#salvar lista ordenada em arquivo pickle 
# with open('lista_spharm_minhaordem.txt', 'wb') as handle:
#   pickle.dump(lista_ordenada, handle)
# print('pickle gerado')
#        
#with open('lista_ordenada.txt', 'rb') as handle:
#  lista_ordenada = pickle.loads(handle.read())

# for i in range(381):
#     if i > 0:
#         v = spharm.vetor_caract(i)
        
        
        
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



# lista_numeros = list(range(1, 381)) 
# #lista_numeros = [5,8,3,2,9,7,10,1,4,6]
# #lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# temp_lista_numeros = lista_numeros
# # print('lista_numeros:', lista_numeros)
# lista_ordenada_mergesort = mergeSort(temp_lista_numeros)
# print('merge:', lista_ordenada_mergesort)


##salvar lista ordenada em arquivo pickle 
# with open('lista_spharm_minhaordem.txt', 'wb') as handle:
#   pickle.dump(lista_ordenada_mergesort, handle)
# print('pickle gerado')
        


# #print('lista_numeros:', lista_numeros)
# lista_ordenada_bubble = ordena_dict(lista_numeros)
# print('bubble:', lista_ordenada_bubble)

        
# with open('lista_spharm_minhaordem.txt', 'rb') as handle:
#   w = pickle.loads(handle.read())




    