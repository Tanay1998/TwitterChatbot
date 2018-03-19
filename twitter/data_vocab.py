import random
import sys

import nltk
import itertools
from collections import defaultdict

import numpy as np

import pickle

def load_data(PATH=''):
    # read data control dictionaries
    with open(PATH + 'metadata.pkl', 'rb') as f:
        metadata = pickle.load(f)
    # read numpy arrays
    idx_q = np.load(PATH + 'idx_q.npy')
    idx_a = np.load(PATH + 'idx_a.npy')
    return metadata, idx_q, idx_a

m, iq, ia = load_data('./')
m = m['w2idx']

vocab = []
for k, v in m.items():
	vocab.append((v, k))

vocab.sort(key=lambda x: x[0])

with open('vocab.dec', 'w') as f:
	for k, v in vocab:
		f.write(v + '\n')
