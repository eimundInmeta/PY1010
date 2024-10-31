
"""
Innlevering 1 - Kostnad elbil vs bensinbil
Created on Tue Oct 22 11:15:19 2024
@author: eimundb

"""

### inputparametre

# kostnad forsikring
forsikring_el       = 5000  #kr/år 
forsikring_bensin   = 7500  #kr/år 

# kostnad trafikkforsikringavgift (TFA)
tfa_el              = 8.38  #kr/dag 
tfa_bensin          = 8.38  #kr/dag 

# kjørelengde
kjørelengde         = int(input("Hvor langt kjører du i året? "))  #km/år 

# forbruksdata
forbruk_el          = 0.2  #kWh/km 
forbruk_bensin      = 1.0  #kr/km 

# strømpris
strømpris           = 2.0  #kr/kWh 

# bomavgifter
bom_el              = 0.1  #kr/km 
bom_bensin          = 0.3  #kr/km 


### beregning av årlig kostnad
kostnad_el          = forsikring_el + tfa_el*365 + forbruk_el*kjørelengde*strømpris + bom_el*kjørelengde
kostnad_bensin      = forsikring_bensin + tfa_bensin*365 + kjørelengde*(forbruk_bensin + bom_bensin)
differanse          = kostnad_bensin - kostnad_el
billigst            = 'elbil' if differanse > 0 else 'bensinbil' if differanse < 0 else 'ingen av dem'

### presentasjon av resultat
print(f"Årlig kostnad elbil = {kostnad_el} kroner")
print(f"Årlig kostnad bensinbil = {kostnad_bensin} kroner")
print(f"Årlig kostnadsdifferanse = {differanse} kroner, og {billigst} er billigst!")

