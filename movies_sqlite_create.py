# -*- coding: utf-8 -*-
"""
Created on Wed May  6 12:33:08 2020

@author: Matthias
"""

import sqlite3
import pandas as pd

movies = pd.read_csv('csv/movies/data_007_movie.csv', sep=';', encoding='UTF-8')
movies.drop(index=25, inplace=True)

with sqlite3.connect('movies.db') as conn:
    movies.to_sql(name='movies', con=conn, if_exists='replace')
