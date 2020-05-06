# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:12:54 2020

@author: Matthias
"""

import sys
import logging


def print_usage():
    print('Usage: python script_dummy [options]', file=sys.stderr )
    print('Options:', file=sys.stderr )
    print('\t-a : blabla option a', file=sys.stderr )
    print('\t-n nb : blabla option n', file=sys.stderr )


log = logging.getLogger('dummy')
log.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logfile = logging.FileHandler('dummy.log', encoding='UTF-8')
logfile.setFormatter(formatter)
log.addHandler(logfile)

print(sys.argv)
if len(sys.argv) > 1:
    # paramètres supplémentaires
    try:
        if "-a" in sys.argv:
            print('Option a activée')
        if "-n" in sys.argv:
            pos = sys.argv.index("-n")
            nb = int(sys.argv[pos+1])
            print("Option -n activée avec :", nb)
        log.info("paramètres analysés avec succès")
    except:
        log.error("erreur sur l'analyse de paramètres")
        print_usage()
        
        
        
        
        
        
        
        
        