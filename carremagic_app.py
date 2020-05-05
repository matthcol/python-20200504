# -*- coding: utf-8 -*-
"""
Created on Tue May  5 09:40:12 2020

@author: Matthias
"""

from carremagic_fun import isMagique, makeMagic
from carremagic_ex import d_ca

for n, ca in d_ca.items():
    m = isMagique(ca)
    print(n,':',m)
    
ca15 = makeMagic(15)
print(ca15)
print(isMagique(ca15))