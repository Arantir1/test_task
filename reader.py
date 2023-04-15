import pandas as pd

'''
Implementation of iterative file reading
'''
def read_movies():
    data = pd.read_csv('movies.tsv', sep='\t', chunksize=1000)
    return data