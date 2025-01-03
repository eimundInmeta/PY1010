"""
Created on Mon Nov 11 15:47:04 2024

@author: eimundb
"""

#import dict lib

###inputparametre

#lager dictionary
data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
    }


for i in range(3):
    #spør brukeren om et land
    land = input("Skriv inn et land: ")
    
    
    # sjekker om inntastet verdi finnes i dictionary og returnerer svar
    if land in data:
        #allokerer verdier til variablene
        hovedstad, befolkning = data[land]
        print(f"{hovedstad} er hovedstaden i {land} og det er {befolkning} millioner innbyggere i {hovedstad}.")
        break
    else:
        print(f"Beklager, jeg har ingen informasjon om {land}.")

# for i in data.values():
#     print(i[0])