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

mm = m['idx2w']

for _ in range(20):
	k = random.randint(1, iq.shape[0])
	q = iq[k, :]
	a = ia[k, :]
	qq = ' '.join([mm[w] for w in q])
	aa = ' '.join([mm[w] for w in a])
	print ('HUMAN ++', qq)
	print ('BOT ++++', aa)
	print ()


# # with open('train.enc', 'w') as f:
# # 	for i in range(iq.shape[0]):
# # 		a = []
# # 		for k in iq[i, :]:
# # 			if k:
# # 				if k > 2: 
# # 					k += 2
# # 				k -= 1
# # 				a.append(str(k))
# # 			else:
# # 				break
# # 		f.write(' '.join(a))
# # 		f.write('\n')

# with open('train.dec', 'w') as f:
# 	for i in range(ia.shape[0]):
# 		a = ['3']
# 		for k in ia[i, :]:
# 			if k:
# 				if k > 2: 
# 					k += 2
# 				k -= 1
# 				a.append(str(k))
# 			else:
# 				break
# 		a.append('4')
# 		f.write(' '.join(a))
# 		f.write('\n')
