import h5py
import numpy as np


hf = h5py.File('model_weights.h5', 'r')
print("Keys: %s" % hf.keys())
n_array1 = hf.get('dense_1')
n1 = np.array(n_array1)

n_array2 = hf.get('dense_2')
n2 = np.array(n_array2)

n_array3 = hf.get('dense_3')
n3 = np.array(n_array3)

print(n1)
print("__________________________")
print(n2)
print("__________________________")
print(n3)
print("__________________________")
hf.close()
