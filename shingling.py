from nltk.tokenize import word_tokenize
from nltk import PorterStemmer
import string
import re
import random
import numpy as np
import time

# createShingles:
# input : doc - the link to the dataset
#         k - the shingle size usually between 5 - 9
# returns : a dictionary with key as the DNA string and
#           the set of shingles as the paired value


def createShingles(doc, k):
    dataset = open(doc, encoding='utf-8')
    lines = [line.rstrip('\n') for line in dataset]
    dataset.close()

    hashmap = {}
    cnt = 0
    for line in lines:
        dna = line.split(" ")[0]
        n = len(dna)
        i = int(k)
        shingles = set()
        while i < n:
            shingles.add(dna[(i - int(k)):i])
            i += 1
        hashmap[cnt] = shingles
        cnt += 1
    return hashmap





