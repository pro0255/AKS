import time
import numpy as np

def calc_probs(freq):
    res = {}    
    tic = time.time()
    print('Calculating probs')
    n = np.sum(list(freq.values()))
    for k, v in freq.items():
        res[k] = v / n

    toc = time.time()
    print(f'End of calculating {toc - tic}')
    return res