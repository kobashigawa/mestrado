# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 16:48:18 2021

pegar arquivos de dist_eucli_ordenadas/ ou dist_manhattan_ordenadas/
e gerar AUCs de acordo com n 

@author: kobashi
"""

from sklearn.metrics import auc
from matplotlib import pyplot
import pickle
import numpy as np


def classe(obj):
    ''' 
    devolve qual classe eh o obj 
    '''
    if obj >= 1 and obj <= 20:          
        return  'humano'
    if obj >= 21 and obj <= 40:               
        return  'copo'
    if obj >= 41 and obj <= 60:           
        return  'oculos'
    if obj >= 61 and obj <= 80:              
        return  'aviao'
    if obj >= 81 and obj <= 100:            
        return  'formiga'
    if obj >= 101 and obj <= 120:              
        return  'cadeira'
    if obj >= 121 and obj <= 140:             
        return  'polvo'
    if obj >= 141 and obj <= 160:             
        return  'mesa'
    if obj >= 161 and obj <= 180:            
        return  'ursinho'
    if obj >= 181 and obj <= 200:            
        return  'mao'
    if obj >= 201 and obj <= 220:           
        return  'alicate'
    if obj >= 221 and obj <= 240:
          return  'peixe'
    if obj >= 241 and obj <= 260:            
        return  'passaro'
    if obj >= 261 and obj <= 280:              
        return  'tatu'
    if obj >= 281 and obj <= 300:               
        return  'dorso'
    if obj >= 301 and obj <= 320:             
        return  'mecha'
    if obj >= 321 and obj <= 340:          
        return  'rolamento'
    if obj >= 341 and obj <= 360:            
        return  'vaso'
    if obj >= 361 and obj <= 380:              
        return  'quadrupede'



    
#print(lista_proximos(319, 10)) 

def gera_AUC(obj, qtde, plot):
    '''
    gera AUC e plot de um objeto 
    obj = numero do obj
    qtde = quantos objs semelhantes quer mais proximos do obj 
    plot = se quer que plote, True ou False 
    
    '''  
    
    #pega arquivo de distancias do objeto i
    #file = 'dist_eucli_ordenadas/' + str(obj) + '.txt'      
    file = 'dist_manhattan_ordenadas/' + str(obj) + '.txt'     
       
    
    
    with open(file, 'rb') as handle:
        lista = pickle.loads(handle.read())           
    
        classe_obj = classe(obj)
      
        #dropa o primeiro elemento q sempre sera o proprio obj (menor distancia = 0)
        lista.pop(0)
        #corta lista para o numero de n 
        proximos = lista[:qtde]  
        #print(proximos)
        
        precisoes = []
        revocacoes = []
        
        relevantes = 0
        recuperados = 0        
        
        for i in proximos:        
            
            #print('i = ', i)
            recuperados = recuperados + 1
            if classe_obj == classe(i):
                
                relevantes = relevantes + 1           
            
                #print('Logistic: f1=%.3f auc=%.3f' % (lr_f1, lr_auc))
                # print('precisao: %i / %i ' % (relevantes, recuperados))
                # print('revocacao: %i / %i  ' % (recuperados, qtde))
                
                precisoes.append(relevantes/recuperados)
                revocacoes.append(recuperados/qtde)    
                
         
    #    print(precisoes)
    #    print(revocacoes)   
    
        if len(revocacoes) < 2:
            return 0 
    
        auc1 = auc(revocacoes, precisoes)  
        
        if plot and len(revocacoes) > 2:
            #plot the precision-recall curves
            pyplot.plot(revocacoes, precisoes, marker='.', label=str(obj))
            # axis labels
            pyplot.xlabel('Revocação')
            pyplot.ylabel('Precisão')
            # show the legend
            pyplot.legend()
            # show the plot
            pyplot.show()
    
        
        return auc1 
    
#print(gera_AUC(1, 30, False))
#print(gera_AUC(377, 15, False))



##DADOS DE INPUT 
n = 15
dado = 'var'
plot = False

# dado = 'min'
# dado = 'max'
# dado = 'med'
# dado = 'var'
##DADOS DE INPUT 


humanos = []
copos = []
oculos = []
aviaos = []
formigas = []
cadeiras = []
polvos = []
mesas = []
ursinhos = []
maos = []
alicates = []
peixes = []
passaros = []
tatus = []
dorsos = []
mechas = []
rolamentos = []
vasos = []
quadrupedes = []


# ##popula listas com AUCs de objetos por classe
for i in range(381):
  
    if i >= 1 and i <= 20:    
        humanos.append(gera_AUC(i, n, plot))
    if i >= 21 and i <= 40:          
        copos.append(gera_AUC(i, n, plot))
    if i >= 41 and i <= 60:         
        oculos.append(gera_AUC(i, n, plot))
    if i >= 61 and i <= 80:          
        aviaos.append(gera_AUC(i, n, plot))
    if i >= 81 and i <= 100:     
        formigas.append(gera_AUC(i, n, plot))
    if i >= 101 and i <= 120:          
        cadeiras.append(gera_AUC(i, n, plot))
    if i >= 121 and i <= 140:       
        polvos.append(gera_AUC(i, n, plot))
    if i >= 141 and i <= 160:        
        mesas.append(gera_AUC(i, n, plot))
    if i >= 161 and i <= 180:            
        ursinhos.append(gera_AUC(i, n, plot))
    if i >= 181 and i <= 200:            
        maos.append(gera_AUC(i, n, plot))
    if i >= 201 and i <= 220:           
        alicates.append(gera_AUC(i, n, plot))
    if i >= 221 and i <= 240:
        peixes.append(gera_AUC(i, n, plot))
    if i >= 241 and i <= 260:            
        passaros.append(gera_AUC(i, n, plot))
    if i >= 261 and i <= 280:           
        tatus.append(gera_AUC(i, n, plot))
    if i >= 281 and i <= 300:             
        dorsos.append(gera_AUC(i, n, plot))
    if i >= 301 and i <= 320:    
        mechas.append(gera_AUC(i, n, plot))
    if i >= 321 and i <= 340:   
        rolamentos.append(gera_AUC(i, n, plot))
    if i >= 341 and i <= 360:  
        vasos.append(gera_AUC(i, n, plot))
    if i >= 361 and i <= 380:   
        quadrupedes.append(gera_AUC(i, n, plot))
    

classes = [quadrupedes,  humanos,  passaros,  oculos,  aviaos,  ursinhos,  peixes,  vasos,  polvos,  alicates,  cadeiras,  tatus,  maos,  formigas,  mesas,  copos,  rolamentos,  dorsos,  mechas]


for lista in classes:    
    
    if dado == 'min':
        print(min(lista))
    elif dado == 'max':
        print(max(lista))
    elif dado == 'med':
        med = sum(lista) / len(lista)
        print(med)
    elif dado == 'var':
        var_100 = np.var(lista) * 100
        print(var_100)
  