# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 15:06:12 2020

Ordena VCs por uma ordem que eu criei, baseada na lexicografica, mas que conta todos os pontos.
Se tiver mais pontos maiores, é classificado como um vetor maior etc.

@author: thiag
"""

import sys
sys.path.append("..") # Adds higher directory to python modules path.
import automatizador
import matplotlib.pyplot as plt
import pickle

#comparando os dois vetores

        
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
        

#retorna vetor de caracteristicas 
def gera_vetor_caract(file, coef):   
  
    temp_file = 'C:/Users/thiag/Google Drive/cbir3d_kobashi/CSDescriptor/temp.txt'
    
    ma = automatizador.gera_matriz_caracteristicas(file, coef, temp_file)
    
    vetor = automatizador.eixo('X', ma) + automatizador.eixo('Y', ma) + automatizador.eixo('Z', ma)
    return vetor



obj1 = 'C:/Users/thiag/Google Drive/cbir3d_kobashi/off/121.off' #polvo
repo = 'C:/Users/thiag/Google Drive/cbir3d_kobashi/off/'

temp_file = 'C:/Users/thiag/Google Drive/cbir3d_kobashi/CSDescriptor/temp1.txt'
temp_file2 = 'C:/Users/thiag/Google Drive/cbir3d_kobashi/CSDescriptor/temp2.txt'
saida = 'C:/Users/thiag/Google Drive/cbir3d_kobashi/CSDescriptor/off_testes/teste.off'  
#coef = 200
#
#nro_polvo = 121
#nro_oculos = 41
#
#objs = 20

#oculos 41 a 60 (19 oculos)
#polvo 121 a 140

#gerar vetor de caracteristicas de todas as duas classes
#comparar uma com a outra (?) tenho q comparar uma com todas? 
#ordenar 

#gerar vetor de caract
#comparar

#fazer um bublle sort usando o metodo de ordem_lexicografica()
#gerar um dicionario de vetores de caract
#ter q ser um dicionario pra saber qual objeto eh cada vetor

#fazer um dicionario apartado so pra guardar os valores de chave (objeto e VC respectivo)
#o bubble sort fica numa lista apartada 
    
    
#https://panda.ime.usp.br/pythonds/static/pythonds_pt/05-OrdenacaoBusca/OBubbleSort.html    
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return alist 
    
       

def gera_dict(obj_inicial, objs, coef):       
    thisdict = {}

    for x in range(objs):
    
        obj = obj_inicial + x        
        file = repo + str(obj) + '.off'
    
        d = gera_vetor_caract(file, coef)
        thisdict[obj] = d
    return thisdict
        


#oculos 41 a 60 (19 oculos)
#polvo 121 a 140

    
##### metodo pra rodar um por vez pra plotar grafico ####

def plota_lista_ordenada_pivo():
    #sort da lista e plotar pra ver onde o pivo cai

    #criar uma lista do 41 ao 60 e do 121 ao 140
    lista = list(range(41, 61)) + list(range(121, 141))

    #ORDENACAO    
    for passnum in range(len(lista)-1,0,-1):
        for i in range(passnum):

            if ordem_inventada(dict_total[lista[i]], dict_total[lista[i + 1]]) == 1:  
          
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
    
    #imprime lista ordenada pela ordem inventada 
    print(lista)
    
    
#    lista_nome = []
#    for e in lista:
#        if e > 100:
#            polvo = 'polvo ' + str(e) 
#            lista_nome.append(polvo)
#        else:
#            oculos = 'oculos ' + str(e)
#            lista_nome.append(oculos)
#    plt.plot(lista_nome, 'bo', color = 'blue')
#    plt.show()
    
    #gera lista com nome das classes e plota 
    lista_nome = []
    for e in lista:
        if e > 100:
            lista_nome.append('polvo')
        else:
            lista_nome.append('oculos')
        
    print(lista_nome)
    
    #mudar cores
    
    plt.plot(lista_nome, 'bo', color = 'blue')
    plt.show()

    
#dict_polvo = gera_dict(121, 20, 200) #polvo
#dict_oculos = gera_dict(41, 20, 200) #oculos
#
#dict_total = dict_polvo
#dict_total.update(dict_oculos)
#
##salvar dicionario em arquivo pickle 
#with open('dic.txt', 'wb') as handle:
#  pickle.dump(dict_total, handle)
#
#print('pickle gerado')

with open('dic.txt', 'rb') as handle:
  dict_total = pickle.loads(handle.read())
  
  
plota_lista_ordenada_pivo()

    
                
    
#gera lista com nome das classes e plota 
#lista_nome = []
#for e in lista:
#    if e > 100:
#        lista_nome.append('polvo')
#    else:
#        lista_nome.append('oculos')
#    
#print(lista_nome)
#
#plt.plot(lista_nome, 'bo', color = 'blue')
#plt.show()
#

#bubbleSort(lista)

#['oculos', 'oculos', 'oculos', 'oculos', 'oculos', 'oculos', 
# 'polvo', 'oculos', 'oculos', 'oculos', 'polvo', 'oculos', 
# 'oculos', 'polvo', 'polvo', 'polvo', 'polvo', 'polvo', 
# 'polvo', 'polvo', 'oculos', 'oculos', 'oculos', 'polvo', 
# 'polvo', 'polvo', 'polvo', 'oculos', 'polvo', 'polvo', 
# 'polvo', 'polvo', 'polvo', 'polvo', 'oculos', 'oculos', 
# 'oculos', 'oculos', 'oculos', 'polvo']








