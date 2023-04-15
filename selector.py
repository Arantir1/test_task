import pandas as pd
from reader import read_movies


'''
Business logic where performed selection and filtering
'''
def get_top_genre(year, row_count=5):
    storage = pd.DataFrame(columns=['genres', 'values'])                                                         # storage of final data
    storage.set_index('genres')

    for chunk in read_movies():
        chunk.query("startYear == @year", inplace=True)                                                         # filter by year 
        chunk['genres'] = chunk['genres'].str.split(',')                                                        # split genres to list by comma 
        series_genres = chunk.explode('genres').groupby(['genres'])['genres'].count()                           # count unique genres
        chunk_genres = pd.DataFrame({'genres':series_genres.index, 'values':series_genres.values})              # convert series -> dataframe
        storage = storage.set_index('genres').add(chunk_genres.set_index('genres'), fill_value=0).reset_index() # merge current chunk data with storage
    
    result = storage.sort_values(by=['values'], ascending=False).head(row_count)                                # get top n popular genres
    
    return result.to_dict('records')