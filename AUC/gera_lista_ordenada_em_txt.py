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
sys.path.append("..") # Adds higher directory to python modules path.
import automatizador
import matplotlib.pyplot as plt
import pickle


with open('dic_coef_200.txt', 'rb') as handle:
  dict_pickle = pickle.loads(handle.read())
        

def ordem_inventada(v1, v2):
    """retorna se vetor 1 eh maior, -1 se menor ou 0 igual ao vetor 2 comparando posicao a posicao
    """        
    maior = 0
    menor = 0
    igual = 0
    
    for p1, p2 in zip(v1, v2):
        if p1 > p2:    
            maior = maior + 1
        if p1 < p2:
            menor = menor + 1
        if p1 == p2:
            igual = igual + 1
            
    if (maior > menor) and (maior > igual):
       #largest = maior
        return 1
       
    elif (menor > maior) and (menor > igual):
        return -1
#       largest = menor
    else:        
       #largest = igual
       return 0 
       

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



lista_ordenada = ordena_dict()

print(lista_ordenada)

#salvar lista ordenada em arquivo pickle 
# with open('lista_ordenada_lexicografica_100.txt', 'wb') as handle:
#   pickle.dump(lista_ordenada, handle)
# print('pickle gerado')

# como abrir a lista
#with open('lista_ordenada.txt', 'rb') as handle:
#  lista_ordenada = pickle.loads(handle.read())
#









