# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 14:34:50 2020

gera valor estatistico da lista ordenada pela ordem inventada

@author: thiag
"""


#lista = ['polvo', 'oculos', 'oculos', 'oculos', 'oculos', 'oculos', 'oculos', 'oculos', 'oculos', 'oculos', 'oculos', 'polvo', 'polvo', 'oculos', 'oculos', 'oculos', 'oculos', 'oculos', 'oculos', 'polvo', 'oculos', 'oculos', 'oculos', 'polvo', 'polvo', 'polvo', 'polvo', 'polvo', 'polvo', 'polvo', 'polvo', 'oculos', 'polvo', 'polvo', 'polvo', 'polvo', 'polvo', 'polvo', 'polvo', 'polvo']



def total_mesma_classe_mais_proximos(elemento, quantidade):
    """ retorna quantos objetos sao da mesma classe do objeto elemento na lista. 
    Sempre vai ter q retornar a quantidade desejada, entao se o elemento estiver nas pontas,
    pegara so de um lado.
    Usa uma lista auxiliar que remove toda vez q um objeto eh pegado e diminui o contador.
    Desse modo sempre devolvera uma razao em relacao ao total de quantidades.
    
    Quantidade eh o total de objetos a olhar diretamente pro lado direito ou esquerdo ao elemento 
    """
    lista_temp = ['polvo', 'oculos', 'oculos', 'oculos', 'oculos', 'oculos', 'oculos', 'oculos', 'oculos', 'oculos', 'oculos', 'polvo', 'polvo', 'oculos', 'oculos', 'oculos', 'oculos', 'oculos', 'oculos', 'polvo', 'oculos', 'oculos', 'oculos', 'polvo', 'polvo', 'polvo', 'polvo', 'polvo', 'polvo', 'polvo', 'polvo', 'oculos', 'polvo', 'polvo', 'polvo', 'polvo', 'polvo', 'polvo', 'polvo', 'polvo']
    mesma_classe = 0
  
    while quantidade > 0:
        #print('loop')
        # direita
        #print('tamanho lista: ', len(lista_temp))
        if elemento + 1 < len(lista_temp):
            #print('entrou direita')
            if lista_temp[elemento] == lista_temp[elemento + 1]:
                mesma_classe = mesma_classe + 1 
            lista_temp.pop(elemento + 1)
            quantidade = quantidade - 1
            if quantidade == 0: break

        # esquerda
#        print('elemento: ', elemento)
#        print('elemento - 1: ', elemento - 1)
        if elemento - 1 >= 0:
            #print('entrou esquerda')
            if lista_temp[elemento] == lista_temp[elemento - 1]:
                mesma_classe = mesma_classe + 1 
            lista_temp.pop(elemento - 1)
            elemento = elemento - 1 #se remover objeto a esquerda ele perde um indice
            quantidade = quantidade - 1
            if quantidade == 0: break
        
        
        if not elemento + 1 < len(lista_temp) and not elemento - 1 > -1:
            print('deu ruim')
            return -1
            
        #print('quantidade: ', quantidade)
            
        

    return mesma_classe


elem = 40
qtde = 10



for i in range(elem):    
      
        total = total_mesma_classe_mais_proximos(i, qtde)
        if total == -1: break
        print(total/qtde)


#total = total_mesma_classe_mais_proximos(2, qtde)
#print(total)

#esquerdo = total_mesma_classe(elem, qtde, 'esquerdo') 
#direito = total_mesma_classe(elem, qtde, 'direito')
#print(esquerdo)
#print(direito)
