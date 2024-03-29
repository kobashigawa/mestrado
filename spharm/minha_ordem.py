# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 19:21:29 2021

gera lista ordenada com base em minha ordem nos VCs do spharm_1343

@author: kobashi
"""

import spharm_1343
import pickle



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
    """retorna se vetor 1 eh maior, -1 se menor ou 0 igual ao vetor 2 comparando posicao a posicao
    
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
        
        
        
# u = (0,3,5,7) 
# v = (1,2,8,6)
# u = (2,2) 
# v = (1,3)
# print(ordem_completa_modulo(u, v))
        
        
        
   

       
#se somar os elementos de cada vetor e comparar? 


#inves de aumentar o contador, incrementar em modulo da diferenca
#se empatar, usar lexicografica
       




        
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
           
            if ordem_completa_modulo(spharm_1343.vetor_caract(lefthalf[i]), spharm_1343.vetor_caract(righthalf[j])) == -1:                
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
# lista_ordenada_mergesort = mergeSort(lista_numeros)
# ##salvar lista ordenada em arquivo pickle 
# with open('lista_spharm_1343_ordem_completa_modulo.txt', 'wb') as handle:
#   pickle.dump(lista_ordenada_mergesort, handle)
# print('pickle gerado')
        

# para printar as listas    
# with open('lista_spharm_1343_minhaordem.txt', 'rb') as handle:
#   w = pickle.loads(handle.read())
#   print(w)

# with open('lista_spharm_1343_ordem_completa_modulo.txt', 'rb') as handle:
#   w = pickle.loads(handle.read())
#   print(w)



    