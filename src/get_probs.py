from src.calc_freq import calc_freq
from src.calc_probs import calc_probs
import pandas as pd


def get_probs(data):
    freq = calc_freq(data)
    return calc_probs(freq)


def get_sorted_probs(data):
    p = get_probs(data)
    return dict(sorted(p.items(), key=lambda item: item[1], reverse=True))


def get_sorted_probs_as_df(data):
    return pd.DataFrame.from_dict(get_sorted_probs(data), orient='index')
