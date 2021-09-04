# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 13:09:33 2021

versao que compara VCs com ordem inventada de todos objetos do banco de dados

@author: thiag
"""



import sys
sys.path.append("..") # Adds higher directory to python modules path.
import automatizador
import matplotlib.pyplot as plt
import pickle

#comparando os dois vetores


#retorna vetor de caracteristicas 
def gera_vetor_caract(file, coef):   
  
    temp_file = 'C:/Users/thiag/Google Drive/cbir3d_kobashi/CSDescriptor/temp.txt'
    
    ma = automatizador.gera_matriz_caracteristicas(file, coef, temp_file)
    
    vetor = automatizador.eixo('X', ma) + automatizador.eixo('Y', ma) + automatizador.eixo('Z', ma)
    return vetor


def gera_dict(obj_inicial, objs, coef):       
    ''' gera dicionario com objeto (numero da malha) e seu VC. 
    objs = quantidade de elementos para gerar o dicionario, sendo q se for 20, pega ate o 19
    380: array([-1.90298375e-02,  3.43923593e+01, -4.42146253e+00, -4.21029093e+00,'''
    
    thisdict = {}
    repo = 'C:/Users/thiag/Google Drive/cbir3d_kobashi/off/'

    for x in range(objs):
    
        obj = obj_inicial + x        
        file = repo + str(obj) + '.off'
    
        d = gera_vetor_caract(file, coef)
        thisdict[obj] = d
        print(obj)
    return thisdict



#gera dict de todos objetos. 40min pra gerar 
#dict_tudo = gera_dict(1, 380, 200)
#
#salvar dicionario em arquivo pickle 
#with open('dic.txt', 'wb') as handle:
#  pickle.dump(dict_tudo, handle)
#print('pickle gerado')
        
#with open('dic.txt', 'rb') as handle:
#  dict_pickle = pickle.loads(handle.read())

#print(dict_pickle)
        


def ordem_inventada(v1, v2):
    """retorna se vetor 1 eh maior, -1 se menor ou 0 igual ao vetor 2 comparando posicao a posicao
    
    v1 > v2: 1
    v1 < v2: -1
    v1 = v2: 0
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
        

# v1 = [1, 2, 3, 4, 5] 
# v2 = [2, 50]
# print(ordem_inventada(v1, v2))


#obj1 = 'C:/Users/thiag/Google Drive/cbir3d_kobashi/off/121.off' #polvo
#temp_file = 'C:/Users/thiag/Google Drive/cbir3d_kobashi/CSDescriptor/temp1.txt'


#nro_polvo = 121
#nro_oculos = 41
#
#objs = 20

#oculos 41 a 60 (19 oculos)
#polvo 121 a 140
 



def ordena_dict():  
    
    lista = list(range(1, 381)) 

    #ORDENACAO    
    for passnum in range(len(lista)-1,0,-1):
        for i in range(passnum):

            if ordem_inventada(dict_pickle[lista[i]], dict_pickle[lista[i + 1]]) == 1:  
          
                temp = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp
    
    #print(lista)
    return lista
    

#def str_list_to_int_list(str_list):
#    n = 0
#    while n < len(str_list):
#        str_list[n] = int(str_list[n])
#        n += 1
#    return str_list
    

def troca_numero_classe(lista):
    ''' recebe uma lista com os numeros dos objetos e substitui pela respectivo
    nome da classe, vai ter q ser na mao, nao tem jeito'''
    
    lista = [int(i) for i in lista]
    index = 0

    for a in lista:
        if type(a) == int:            
            if a >= 1 and a <= 20:          
                lista[index] =  'humano'
            if a >= 21 and a <= 40:               
                lista[index] =  'copo'
            if a >= 41 and a <= 60:           
                lista[index] =  'oculos'
            if a >= 61 and a <= 80:              
                lista[index] =  'aviao'
            if a >= 81 and a <= 100:            
                lista[index] =  'formiga'
            if a >= 101 and a <= 120:              
                lista[index] =  'cadeira'
            if a >= 121 and a <= 140:             
                lista[index] =  'polvo'
            if a >= 141 and a <= 160:             
                lista[index] =  'mesa'
            if a >= 161 and a <= 180:            
                lista[index] =  'ursinho'
            if a >= 181 and a <= 200:            
                lista[index] =  'mao'
            if a >= 201 and a <= 220:           
                lista[index] =  'alicate'
            if a >= 221 and a <= 240:
                  lista[index] =  'peixe'
            if a >= 241 and a <= 260:            
                lista[index] =  'passaro'
            if a >= 261 and a <= 280:              
                lista[index] =  'tatu'
            if a >= 281 and a <= 300:               
                lista[index] =  'dorso'
            if a >= 301 and a <= 320:             
                lista[index] =  'mecha'
            if a >= 321 and a <= 340:          
                lista[index] =  'rolamento'
            if a >= 341 and a <= 360:            
                lista[index] =  'vaso'
            if a >= 361 and a <= 380:              
                lista[index] =  'quadrupede'
                
            index = index + 1
        
    
    return lista


#lista_ordenada = ordena_dict()
#salvar lista ordenada em arquivo pickle 
#with open('lista_ordenada.txt', 'wb') as handle:
#  pickle.dump(lista_ordenada, handle)
#print('pickle gerado')
#        
#with open('lista_ordenada.txt', 'rb') as handle:
#  lista_ordenada = pickle.loads(handle.read())
#
##lista_ordenada = [24, 4, 1, 5, 8, 12, 3, 2, 11]
#
#lista_nome = troca_numero_classe(lista_ordenada)

#salvar lista ordenada e com nome das classes em arquivo pickle 
#with open('lista_ordenada_classes.txt', 'wb') as handle:
#  pickle.dump(lista_nome, handle)
#print('pickle gerado')

#print(lista_nome)
#
##print(lista_nome)
#print(len(lista_nome))



def total_mesma_classe_mais_proximos(elemento, quantidade):
    """ retorna quantos objetos sao da mesma classe do objeto elemento na lista. 
    Sempre vai ter q retornar a quantidade desejada, entao se o elemento estiver nas pontas,
    pegara so de um lado.
    Usa uma lista auxiliar que remove toda vez q um objeto eh pegado e diminui o contador.
    Desse modo sempre devolvera uma razao em relacao ao total de quantidades.
    
    Quantidade eh o total de objetos a olhar diretamente pro lado direito ou esquerdo ao elemento 
    """
    #lista_temp = ['polvo', 'oculos', 'oculos', 'oculos', 'oculos', 'oculos', 'oculos', 'oculos', 'oculos', 'oculos', 'oculos', 'polvo', 'polvo', 'oculos', 'oculos', 'oculos', 'oculos', 'oculos', 'oculos', 'polvo', 'oculos', 'oculos', 'oculos', 'polvo', 'polvo', 'polvo', 'polvo', 'polvo', 'polvo', 'polvo', 'polvo', 'oculos', 'polvo', 'polvo', 'polvo', 'polvo', 'polvo', 'polvo', 'polvo', 'polvo']
    
    with open('lista_ordenada_classes.txt', 'rb') as handle:
        lista_temp = pickle.loads(handle.read())
    
    #lista_temp = troca_numero_classe(lista_ordenada)
    mesma_classe = 0
    #print(lista_temp[elemento])
    
    while quantidade > 0:
   
        # direita
        if elemento + 1 < len(lista_temp):
            
            #print(lista_temp[elemento] + ' ' + lista_temp[elemento + 1])
            if lista_temp[elemento] == lista_temp[elemento + 1]:
                mesma_classe = mesma_classe + 1 
            lista_temp.pop(elemento + 1)
            quantidade = quantidade - 1
            if quantidade == 0: break

        # esquerda
        if elemento - 1 >= 0:            
           # print(lista_temp[elemento] + ' ' + lista_temp[elemento - 1])
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






#testa a lista elemento a elemento
#elem = 380
#qtde = 10
#for i in range(elem):          
#
#    total = total_mesma_classe_mais_proximos(i, qtde)
#    if total == -1: break
#    print(total/qtde)


def testa_classe(classe, qtde, metrica):
    '''testa a lista de acordo com a classe. Se for 'humano', vai procurar
    todos humanos e comparar com os elementos q estiverem no lado dele,
    de acordo com a quantidade. Retorna a precisao, revocacao e acuracia media de todos obj da classe'''
  

    with open('lista_ordenada_classes.txt', 'rb') as handle:
        lista = pickle.loads(handle.read())
  
    index = 0
    precisoes = []
    revocacoes = []
    acuracias = []
     #comparar com os elementos ao lado dele
    for obj in lista:
        if obj == classe:
            p = total_mesma_classe_mais_proximos(index, qtde)            
            precisoes.append(p/qtde)
            #colocando 19 pq o elemento em si nao faz parte da conta 
            revocacoes.append(p/19)            
            acuracias.append((p + (360 - (qtde - p)))/380)
        index = index + 1
            
    
    if metrica == 'precisao':
        precisao = sum(precisoes) / len(precisoes)  
        return(round(precisao, 2))
    if metrica == 'revocacao':
        revocacao = sum(revocacoes) / len(revocacoes) 
        return(round(revocacao, 2))
    if metrica == 'acuracia':
        acuracia = sum(acuracias) / len(acuracias) 
        return(round(acuracia, 2))
    


quantidade = 10
#print(testa_classe('humano', quantidade))
#print(testa_classe('copo', quantidade))
#print(testa_classe('oculos', quantidade))
#print(testa_classe('aviao', quantidade))
#print(testa_classe('formiga', quantidade))
#print(testa_classe('cadeira', quantidade))
#print(testa_classe('polvo', quantidade))
#print(testa_classe('mesa', quantidade))
#print(testa_classe('ursinho', quantidade))
#print(testa_classe('mao', quantidade))
#print(testa_classe('alicate', quantidade))
#print(testa_classe('peixe', quantidade))
#print(testa_classe('passaro', quantidade))
#print(testa_classe('tatu', quantidade))
#print(testa_classe('dorso', quantidade))
#print(testa_classe('mecha', quantidade))
#print(testa_classe('rolamento', quantidade))
#print(testa_classe('vaso', quantidade))
#print(testa_classe('quadrupede', quantidade))

m = 'acuracia'

# print(testa_classe('quadrupede', quantidade, m))
# print(testa_classe('humano', quantidade, m))
# print(testa_classe('passaro', quantidade, m))
# print(testa_classe('oculos', quantidade, m))
# print(testa_classe('aviao', quantidade, m))
# print(testa_classe('ursinho', quantidade, m))
# print(testa_classe('peixe', quantidade, m))
# print(testa_classe('vaso', quantidade, m))
# print(testa_classe('polvo', quantidade, m))
# print(testa_classe('alicate', quantidade, m))
# print(testa_classe('cadeira', quantidade, m))
# print(testa_classe('tatu', quantidade, m))
# print(testa_classe('mao', quantidade, m))
# print(testa_classe('formiga', quantidade, m))
# print(testa_classe('mesa', quantidade, m))
# print(testa_classe('copo', quantidade, m))
# print(testa_classe('rolamento', quantidade, m))
# print(testa_classe('dorso', quantidade, m))
# print(testa_classe('mecha', quantidade, m))

    








