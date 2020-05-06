# -*- coding: utf-8 -*-
"""
Created on Wed May  6 14:47:23 2020

@author: Matthias
"""
from datetime import date
from functools import total_ordering

@total_ordering
class Movie:
    """
    class representing a movie with its title, year and director
    """
    
    def __init__(self, title, year, director=None):
        self.title = title
        self.year = year
        self.director = director
      
    # override __repr__ and __str__
    def __repr__(self):
        return f"{self.title} ({self.year}) by {self.director}"
    
    def __len__(self):
        return len(self.title)
    
    # override __eq__ and __neq__
    def __eq__(self, other):
        if type(other) != Movie:
            return NotImplemented
        return (self.title, self.year) == (other.title, other.year)
    
    def __lt__(self, other):
        if type(other) != Movie:
            return NotImplemented
        return (self.year, self.title) < (other.year, other.title)
    
    def age(self):
        today = date.today()
        return today.year - self.year
    
    
print('module Movie loaded')
if __name__ == '__main__':
    print('Application movie started')
    m = Movie('No Time To Die',2020, 'Cary Joji Fukunaga')
    print(m)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    