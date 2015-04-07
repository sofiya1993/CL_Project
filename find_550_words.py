# -*- coding: utf-8 -*-
"""
Spyder Editor


"""
# Please, be careful! Python3 and NLTK 3.0.

import nltk
from nltk.corpus import PlaintextCorpusReader
stopwords=nltk.corpus.stopwords.words('ukrainian1')
def corpus_checking(corpus_root):
    """Function for personal corpus (all txt files in "corpus_root" ) creation 
    and checking the number of words 
    """
    reader = PlaintextCorpusReader(corpus_root, '.*\.txt')
    words=set(w.lower() for w in reader.words() if w.isalpha() and w.lower() not in stopwords )
    if len(words) < 100:
        print ("Додай, будь-ласка, мила, ще трохи відгуків.")
        print (len(words))
    else:
        print (words)
        f=open(corpus_root+'\Kulba_wordslist.txt','w')
        for word in words:
            f.write(word+'\n')
        f.close()
    
corpus_root = 'C:\Users\Oksana\Documents\GitHub\CL_Project'
corpus_checking(corpus_root)
