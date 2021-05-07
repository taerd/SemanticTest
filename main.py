from collections import Counter
from collections import OrderedDict
import re
import copy
from pymystem3 import Mystem
import pymorphy2
from nltk.corpus import stopwords
import numpy as np
import math

def main(array):
    filtered_tokens = []
    docs_tokens = []

    # русские стоп слова, их нужно отбросить (союзы,предлоги)
    stop_words = stopwords.words("russian")
    for doc in array:
        current_tokens=[]

        # лемматизация текста
        doc = lemmatize_sentence(doc)

        # разбиение слов от всяких символов
        all_tokens=re.split(r'[-\s\n\t-:\[\]<>\'.,;!?()" ]+',doc)

        for token in all_tokens:
            if token not in stop_words :
                filtered_tokens.append(token)
                current_tokens.append(token)
        # добавление в список термов для текущего документа
        docs_tokens.append(current_tokens)

    # словарь - лексикон составленный из входных данных
    lexicon=Counter(filtered_tokens)

    zero_vector = OrderedDict((token,0) for token in lexicon)

    idf_vector=copy.copy(zero_vector)

    #tf в виде списка для каждого документа
    docs_vector=[]
    cnt = len(docs_tokens)
    for i in range(cnt):
        docs_vector.append(copy.copy(zero_vector))

    # матрица для хранения tf-idf термов и документов
    data_matrix=np.zeros((len(zero_vector),cnt))
    k=0

    for key,value in lexicon.items(): #для каждого терма в лексиконе из 4ех документов
        docs_containing_key=0
        for i in range(cnt):
            if key in docs_tokens[i]:
                #сколько раз встречается данный терм key в текущем документе
                docs_vector[i][key]=Counter(docs_tokens[i])[key]
                docs_containing_key+=1
        idf = 0
        # вычисление idf текущего терма key
        if (docs_containing_key!=0 and docs_containing_key!=cnt):
            idf=math.log2((cnt-1)/docs_containing_key)
            idf_vector[key]=idf

        for i in range(cnt):
            # вычисление tf-idf данного key для всех документов
            data_matrix[k][i]=idf_vector[key]*docs_vector[i][key]
        k+=1
    # вычисление семантическогот расстояния между векторами tf-idf документов
    simCos(data_matrix,cnt)

def lemmatize_sentence(text):
    lemmas=m.lemmatize(text)
    return "".join(lemmas).strip()

def simCos(array,m):
    for i in range(m):
        for k in range(m):
            a=array[:,i]
            b=array[:,k]
            # косинусная мера сходства
            result=a.dot(b)/(np.linalg.norm(a)*np.linalg.norm(b))
            print(f"semantic distance between {i} and {k} is: {result}")
            print()

def get_data(name):
    f=open(f"{name}.txt",encoding='utf-8')
    docs=[]
    for line in f:
        docs.append(line)
    return docs

m = Mystem()
morph = pymorphy2.MorphAnalyzer()
docs=get_data("data")
main(docs)