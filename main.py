from collections import Counter
from collections import OrderedDict
import re
import copy
from sklearn.feature_extraction.text import TfidfVectorizer
from pymystem3 import Mystem
import pymorphy2
from nltk.corpus import stopwords
import numpy as np
def main(array):

    filtered_tokens=[]
    docs_tokens = []
    stop_words=stopwords.words("russian")
    for doc in array:
        current_tokens=[]
        #print(doc)
        doc = lemmatize_sentence(doc)
        #print(doc)
        all_tokens=re.split(r'[-\s\n\t.,;!?()" ]+',doc)
        #print(all_tokens)
        for token in all_tokens:
            if token not in stop_words :
                filtered_tokens.append(token)
                current_tokens.append(token)
        #print()
        docs_tokens.append(current_tokens)

    #print(Counter(filtered_tokens))
    lexicon=Counter(filtered_tokens)
    #print(len(lexicon))
    #print(docs_tokens)
    zero_vector = OrderedDict((token,0) for token in lexicon)
    document_tf_idf_vectors=[]
    for number in [1,2,3]:
        vec=copy.copy(zero_vector)
        token_counts=Counter(docs[number])
        print(token_counts)
        print()
        for key, value in lexicon.items():
            docs_containig_key=0
            if key in docs[number]:
                docs_containig_key+=1
            if docs_containig_key == 0:
                continue
                tf = value

def lemmatize_sentence(text):
    lemmas=m.lemmatize(text)
    return "".join(lemmas).strip()

#def algorythm(array):

def main2():
    docs = ["понятие изоморфизма между множествами подрузамевает существование обратной биекции из образа в прообраз"]
    docs.append("изоморфизм это обратимое отображение (биекция) между двумя множествами, с сохранением структуры множеств")
    docs.append("два множества называются изоморфными, когда между ними существует изоморфизм")
    docs.append("изоморфизм - более узкое понятие биекции, а автоморфизм - сужение изоморфизма на класс отображений \"само в себя\"")
    vectorizer =TfidfVectorizer(min_df=1)
    model = vectorizer.fit_transform(docs)
    print(model.todense().round(2))

m = Mystem()
morph = pymorphy2.MorphAnalyzer()

docs = ["понятие изоморфизма между множествами подрузамевает существование обратной биекции из образа в прообраз"]
docs.append("изоморфизм это обратимое отображение (биекция) между двумя множествами, с сохранением структуры множеств")
docs.append("два множества называются изоморфными, когда между ними существует изоморфизм")
docs.append("изоморфизм - более узкое понятие биекции, а автоморфизм - сужение изоморфизма на класс отображений \"само в себя\"")
main(docs)
