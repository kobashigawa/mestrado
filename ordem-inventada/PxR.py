# -*- coding: utf-8 -*-
"""
Created on Wed May 12 13:19:58 2021

gera grafico PxR 

@author: kobashi
"""



# precision-recall curve and f1
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import f1_score
from sklearn.metrics import auc
from matplotlib import pyplot
import ordem_invent_todos_objetos
import pickle



# https://panda.ime.usp.br/pythonds/static/pythonds_pt/05-OrdenacaoBusca/OBubbleSort.html
def bubbleSort(alist, blist):
    '''
    metodo criado para ordenar o vetor de precisoes e revocacoes junto

    Parameters
    ----------
    alist : lista
        vetor de precisao.
    blist : lista
        vetor de revocacao.

    Returns
    -------
    lista com duas listas: precisao e revocacao.

    '''
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]<alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                
                temp2 = blist[i]
                blist[i] = blist[i+1]
                blist[i+1] = temp2

    return [alist, blist]

# alist = [54,26,93,17,77,31,44,55,20]
# blist = [6, 3, 9, 1, 8, 4, 5, 7, 2]
# t = bubbleSort(alist, blist)
# print(t)






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
            p = ordem_invent_todos_objetos.total_mesma_classe_mais_proximos(index, qtde)            
            precisoes.append(p/qtde)
            revocacoes.append(p/19)            
            acuracias.append((p + (360 - (qtde - p)))/380)
        index = index + 1
            
    
    if metrica == 'precisao':             
        precisoes.sort()  
        # print(precisoes)
        # print(len(precisoes))
        return precisoes
    if metrica == 'revocacao':    
        revocacoes.sort(reverse=True)      
        # print(revocacoes)
        # print(len(revocacoes))
        return revocacoes
    if metrica == 'acuracia':      
        #return(round(acuracia, 2))
        return acuracias.sort()



 
    
    

def calcula_auc(r, p):
    auc1 = auc(r, p)   
    #round(auc1, 2)
    return print(auc1)    


###############################################################

classe = 'quadrupede'
r = testa_classe(classe, 10, 'revocacao')
p = testa_classe(classe, 10, 'precisao')
calcula_auc(r, p)




###############################################################
#para todas classes

# classes = ['quadrupede', 'humano', 'passaro', 'oculos', 'aviao', 'ursinho', 'peixe', 'vaso', 'polvo', 'alicate', 'cadeira', 'tatu', 'mao', 'formiga', 'mesa', 'copo', 'rolamento', 'dorso', 'mecha']

     

# for classe in classes:    
#     r = testa_classe(classe, 10, 'revocacao')
#     p = testa_classe(classe, 10, 'precisao')
#     calcula_auc(r, p)

###############################################################



# gerar AUC por classe
# gerar valor minimo, maximo, medio, desvio padrao, variancia 
# isso eh so gerar o valor AUC pra cada objeto 
# da pra gerar AUC por objeto ou por classe? 


#plot the precision-recall curves
pyplot.plot(r, p, marker='.', label=classe)
# axis labels
pyplot.xlabel('Recall')
pyplot.ylabel('Precision')
# show the legend
pyplot.legend()
# show the plot
pyplot.show()

###############################################################


#fazer funcao q pega posicao da lista com nomes e devolve o numero do objeto
        



#def plot_PxR(classe, qtde):
#     '''plota grafico PxR de classe'''
  

#     with open('lista_ordenada_classes.txt', 'rb') as handle:
#         lista = pickle.loads(handle.read())
  
#     index = 0
#     precisoes = []
#     revocacoes = []
#     acuracias = []
#      #comparar com os elementos ao lado dele
#     for obj in lista:
#         if obj == classe:
#             p = ordem_invent_todos_objetos.total_mesma_classe_mais_proximos(index, qtde)            
#             precisoes.append(p/qtde)
#             revocacoes.append(p/19)            
#             acuracias.append((p + (360 - (qtde - p)))/380)
#         index = index + 1
            
#     revocacoes_ordenado, precisoes_ordenado = bubbleSort(revocacoes, precisoes)
    

#     pyplot.plot(revocacoes_ordenado, precisoes_ordenado, marker='.', label=classe)
#     # axis labels
#     pyplot.xlabel('Recall')
#     pyplot.ylabel('Precision')
#     # show the legend
#     pyplot.legend()
#     # show the plot
#     pyplot.show()'


#https://machinelearningmastery.com/roc-curves-and-precision-recall-curves-for-classification-in-python/
# precision-recall curve and f1

# generate 2 class dataset
# X, y = make_classification(n_samples=1000, n_classes=2, random_state=1)
# # split into train/test sets
# trainX, testX, trainy, testy = train_test_split(X, y, test_size=0.5, random_state=2)
# # fit a model
# model = LogisticRegression(solver='lbfgs')
# model.fit(trainX, trainy)
# # predict probabilities
# lr_probs = model.predict_proba(testX)
# # keep probabilities for the positive outcome only
# lr_probs = lr_probs[:, 1]
# # predict class values
# yhat = model.predict(testX)
# lr_precision, lr_recall, _ = precision_recall_curve(testy, lr_probs)


# print(lr_recall.shape)
# print(lr_precision.shape)

# lr_f1, lr_auc = f1_score(testy, yhat), auc(lr_recall, lr_precision)
# # summarize scores
# print('Logistic: f1=%.3f auc=%.3f' % (lr_f1, lr_auc))
# # plot the precision-recall curves
# no_skill = len(testy[testy==1]) / len(testy)
# pyplot.plot([0, 1], [no_skill, no_skill], linestyle='--', label='No Skill')
# pyplot.plot(lr_recall, lr_precision, marker='.', label='Logistic')
# # axis labels
# pyplot.xlabel('Recall')
# pyplot.ylabel('Precision')
# # show the legend
# pyplot.legend()
# # show the plot
# pyplot.show()
# pyplot.show()






    







