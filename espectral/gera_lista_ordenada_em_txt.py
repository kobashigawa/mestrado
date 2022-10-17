# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 23:14:40 2021

Gera lista ordenada em txt de acordo com ordem que quiser:
minha ordem
lex
revlex

A lista ordenada será a com base no arquivo 'dic.txt' ou outra especificada

@author: kobashi
"""


import sys
import pickle


with open('dic_coef_200.txt', 'rb') as handle:
  dict_pickle = pickle.loads(handle.read())
        




def ordem_lexicografica(v1, v2):
    """retorna se vetor 1 eh maior, -1 se menor ou 0 igual ao vetor 2 comparando posicao a posicao
    """        
            
    for p1, p2 in zip(v1, v2):
        if p1 > p2:    
            return 1
        if p1 < p2:
            return -1
  
    return 0
        


def ordem_completa_modulo(v1, v2):
    """retorna se vetor 1 eh maior, -1 se menor ou 0 igual ao vetor 2 comparando a somatoria de todas coordenadas dos vetores
    
    v1 > v2: 1
    v1 < v2: -1
    v1 = v2: 0
    """        
    
    
    # somar todos elementos do vetor e comparar a soma de u com a soma de v
    # se empatar usar a tecnica da balança 
    # se continuar empatando usar lexicografica 
   
    
    somav1 = sum(v1)
    somav2 = sum(v2)
     
    if somav1 > somav2:
        return 1
    if somav1 < somav2:        
        return -1
    
    
    if somav1 == somav2:       
        print('vetores iguais')
        maiordiferenca = 0
        maiorp1 = 0
        maiorp2 = 0
        variacao = 0
        
        for p1, p2 in zip(v1, v2):
            
            #calcula diferenca em modulo. A ideia eh ver qual coordenada tem maior diferenca e ai a balanca pesa para o lado dele
            #tem q verificar se no caso dos vetores (10,0) e (0,10) ele classifica o primeiro vetor como maior, igual na ordem lex 
            if abs(p1) > abs(p2):
                p1menosp2 = abs(p1) - abs(p2)
                if p1menosp2 > maiordiferenca:
                    maiordiferenca = p1menosp2
                    maiorp1 = p1               
                if p1menosp2 == maiordiferenca:
                    variacao = variacao + 1
                
            if abs(p1) < abs(p2):
                p2menosp1 = abs(p2) - abs(p1)
                if p2menosp1 > maiordiferenca:
                    maiordiferenca = p2menosp1
                    maiorp2 = p2
                if p2menosp1 == maiordiferenca:
                    variacao = variacao + 1
                    
        if variacao == len(v1) or variacao == len(v2):
            print('apelou para ordem lex')
            return ordem_lexicografica(v1, v2)
            
                
        if maiorp1 > maiorp2:
            return 1        
        if maiorp1 < maiorp2:
            return -1        
        if maiorp1 == maiorp2:
            print('apelou para ordem lex')
            return ordem_lexicografica(v1, v2)
        
        
        
   

        
#ordenacao nlogn
def mergeSort(alist):
#https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OMergeSort.html
    #print("Splitting ",alist)
    
    if len(alist)>1:
        
        # para monitoramento
        #print(len(alist))
        
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
           
            if ordem_completa_modulo(dict_pickle[lista[i]], dict_pickle[lista[j]]) == -1:                
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


       


def ordem_lexicografica_reversa(v1, v2):
    """retorna se vetor 1 eh maior, -1 se menor ou 0 igual ao vetor 2 comparando posicao a posicao
    """        
            
    for p1, p2 in zip(reversed(v1), reversed(v2)):
        if p1 > p2:    
            return 1
        if p1 < p2:
            return -1

    return 0
        

def ordena_dict():  
    
    lista = list(range(1, 381)) 

    #ORDENACAO    
    for passnum in range(len(lista)-1,0,-1):
        for i in range(passnum):

            if ordem_lexicografica(dict_pickle[lista[i]], dict_pickle[lista[i + 1]]) == 1:  
          
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
    
    #imprime lista ordenada pela ordem inventada 
    #print(lista)
    return lista


#usando mergesort 
lista = list(range(1, 381)) 
lista_ordenada = mergeSort(lista)
print(lista_ordenada)

##usando bubblesort 
#lista_ordenada = ordena_dict()

##salvar lista ordenada em arquivo pickle 
with open('lista_ordenada_ordemcompletamodulo_200.txt', 'wb') as handle:
  pickle.dump(lista_ordenada, handle)
print('pickle gerado')

### como abrir a lista
# with open('lista_ordenada_minhaordem_50.txt', 'rb') as handle:
#   lista_print = pickle.loads(handle.read())
#   print(lista_print)










