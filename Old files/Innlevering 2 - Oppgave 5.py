

import numpy as np


def areal_omkrets(a, b):
    
    #Beregner hypotenus i trekant med Pythagoras (k1^2 + k2^2 = h^2)
    hyp = np.sqrt(a**2 + b**2)
    
    #Radius
    rad = a / 2
    
    #Areal halvsirkel (pi*r^2/2)
    areal_sirkel = np.pi * rad**2 / 2
    
    #Areal trekant (l*b/2)
    areal_trekant = a * b / 2
    
    #Omkrets halvsirkel (pi*d)
    omkrets_sirkel = np.pi * rad
    
    #Areal totalt
    areal_tot = areal_sirkel + areal_trekant
    
    #Ytre omkrets totalt
    omkrets_tot = omkrets_sirkel + b + hyp
    
    #Definerer funksjonens utdata
    return areal_tot, omkrets_tot
    
#Lar brukeren skrive inn verdier for a og b
a = float(input("Skriv inn en verdi for a: "))
b = float(input("Skriv inn en verdi for b: "))

#Gjør beregninger
areal, omkrets = areal_omkrets(a, b)

#Presenterer resultat
print(areal)
print(omkrets)

print(f"Ytre omkrets for hele figuren er {omkrets:.2f}.")
print(f"Areal for hele figuren er {areal:.2f}.")
      