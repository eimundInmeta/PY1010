# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 15:15:02 2024

@author: eimundb
"""

###Oppgave 2 - Innkjøp av pizza
# load lib math
import math

#input
antall_elever = int(input("Skriv inn antall elever: "))
antall_alever_pr_pizza = 4

#beregninger
antall_pizza = math.ceil(antall_elever / antall_alever_pr_pizza)

#presentasjon av resultat
print(f"Det må kjøpes inn {antall_pizza} pizzaer til festen! Hver elev får da {(antall_pizza / antall_elever):.2f} pizzaer hver.")