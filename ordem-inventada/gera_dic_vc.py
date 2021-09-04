# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 17:56:34 2020

salva pickle contendo dicionario de objeto e seu VC

@author: thiag
"""
import sys
sys.path.append("..") # Adds higher directory to python modules path.
import automatizador
import pickle
   

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


    
dict_polvo = gera_dict(121, 20, 200) #polvo
dict_oculos = gera_dict(41, 20, 200) #oculos

dict_total = dict_polvo
dict_total.update(dict_oculos)
#
#salvar dicionario em arquivo pickle 
with open('dic_teste.txt', 'wb') as handle:
  pickle.dump(dict_total, handle)
#
print('pickle gerado')

#para ler: 
with open('dic.txt', 'rb') as handle:
  dict_total = pickle.loads(handle.read())

    