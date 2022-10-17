# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 15:01:19 2021

varre todos VCs do Spharm, encontra o menor e trunca todo BD, gerando novo arquivo de VCs.

@author: kobashi
"""

import csv
import pickle

def vetor_caract(o):
    '''
    retorna VC do obj inputado

 
    -------


    '''
    
    file = 'vetores.txt'       
    
    with open(file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')    
        
        lista = []
        obj = 1
        for row in spamreader:
            if obj == o:                
                for e in row:
                    if e != '':
                        lista.append(float(e))
                return lista
            obj = obj + 1
            

def calcula_menor_vetor():
    menor = 999999999999 
    tamanhos = []
    for i in(range(381)):  
        if i > 0:        
            tamanhos.append(len(vetor_caract(i)))
    return min(tamanhos)
            
            
            # temp = len(vetor_caract(i))    
            # if temp < menor:
            #     menor = temp 
            #     vetor = i
    
    # print(vetor)
    # print(temp)            

#print(calcula_menor_vetor())

# resultado 
# 125
# 3703

# tem 1343


def trunca(tamanho):
    vetores = []
    file = 'vetores_1343.txt'
    for i in(range(381)):  
      if i > 0:        
          v = vetor_caract(i)
          v = v[:tamanho]
          vetores.append(v)    
    with open(file, 'wb') as handle:
      pickle.dump(vetores, handle)
    print('pickle gerado')
          

# menorvetor = 1343
# trunca(menorvetor)
  
    
    
    
    
    
    
    
    
    


