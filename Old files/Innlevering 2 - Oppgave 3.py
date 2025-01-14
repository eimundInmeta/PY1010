# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 15:40:16 2024

@author: eimundb
"""

#import numpy lib
import numpy as np

#inputparametre
v_grad = float(input("Skriv inn gradtallet: "))

#beregnigner
v_rad = v_grad*np.pi/180

#presenterer resultat
print(f"Antall radianer som tilsvarer {v_grad} grader er {v_rad:.4f}.")
