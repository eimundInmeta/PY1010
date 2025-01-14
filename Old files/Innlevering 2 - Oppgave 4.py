#lager dictionary (deloppgave a)
data = {
    "Norge": ["Oslo", 0.634],
    "England": ["London", 8.982],
    "Frankrike": ["Paris", 2.161],
    "Italia": ["Roma", 2.873]
    }


#spør brukeren om et land (deloppgave b)
land = input("Skriv inn et land: ")
    
    
# sjekker om inntastet verdi finnes i dictionary og returnerer svar
if land in data:
    #allokerer verdier til variablene
    hovedstad, befolkning = data[land]
    print(f"{hovedstad} er hovedstaden i {land} og det er {befolkning} millioner innbyggere i {hovedstad}.")

else:
    print(f"Beklager, jeg har ingen informasjon om {land}.")
        
    #sjekker om land skal legges til i listen (deloppgave c)
    nyttland = input("Ønsker du å legge det til i listen? (y/n): ")
    if nyttland.lower() == "y":
        hovedstad = input(f"Hva er hovedstaden i {land}? ")
        folketall = input(f"Hvor mange millioner innbyggere bor det i {hovedstad}? ")
        data.update({land: [hovedstad, folketall]})
        print(f"Takk, da er {land} lagt til. Ha en god dag!")
        print(data)
    else:
        print("OK, ha en fin dag videre!")