import time

def calc_freq(data):
    tic = time.time()
    print('Calculating freqs')
    res = {}
    for c in data:
        res[c] = res.get(c, 0) + 1
    toc = time.time()
    print(f'End of calculating {toc - tic}')
    return res