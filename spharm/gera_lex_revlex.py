# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 19:37:24 2021

gera lista ordenada com base em ordem lex e revlex nos VCs do spharm_1343

@author: kobashi
"""



#pegar VCs do spharm_1343, ordenar, gerar lista ordenada

import pickle
import spharm_1343 



def ordem_lexicografica(v1, v2):
    """retorna se vetor 1 eh maior, -1 se menor ou 0 igual ao vetor 2 comparando posicao a posicao
    """        
            
    for p1, p2 in zip(v1, v2):
        if p1 > p2:    
            return 1
        if p1 < p2:
            return -1
  
    return 0
        
def ordem_lexicografica_reversa(v1, v2):
    """retorna se vetor 1 eh maior, -1 se menor ou 0 igual ao vetor 2 comparando posicao a posicao
    """        
            
    for p1, p2 in zip(reversed(v1), reversed(v2)):
        if p1 > p2:    
            return 1
        if p1 < p2:
            return -1

    return 0


# lista_numeros = list(range(1, 11)) 
# print('lista_numeros:', lista_numeros)
# lista_ordenada = ordena_dict(lista_numeros)
# print('bubble:', lista_ordenada)

#salvar lista ordenada em arquivo pickle 
# with open('lista_spharm_1343_minhaordem.txt', 'wb') as handle:
#   pickle.dump(lista_ordenada, handle)
# print('pickle gerado')
#        
#with open('lista_ordenada.txt', 'rb') as handle:
#  lista_ordenada = pickle.loads(handle.read())

# for i in range(381):
#     if i > 0:
#         v = spharm_1343.vetor_caract(i)
        
        
        
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
           
            if ordem_lexicografica(spharm_1343.vetor_caract(lefthalf[i]), spharm_1343.vetor_caract(righthalf[j])) == -1:                
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



lista_numeros = list(range(1, 381)) 
lista_ordenada_mergesort = mergeSort(lista_numeros)


###salvar lista ordenada em arquivo pickle 
with open('lista_spharm_1343_lex.txt', 'wb') as handle:
  pickle.dump(lista_ordenada_mergesort, handle)
print('pickle gerado')
        


# #print('lista_numeros:', lista_numeros)
# lista_ordenada_bubble = ordena_dict(lista_numeros)
# print('bubble:', lista_ordenada_bubble)

        
# with open('lista_spharm_1343_minhaordem.txt', 'rb') as handle:
#   w = pickle.loads(handle.read())




    