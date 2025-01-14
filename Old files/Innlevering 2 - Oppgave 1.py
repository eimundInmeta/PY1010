
"""
Innlevering 2 - PY1010
Created on Mon Nov 11 14:15:18 2024
@author: eimundb
"""


###Oppgave 1 - Beregning av alder

#import lib
import datetime as dt

#input
alder = int(input('Hvilket år er du født?'))

#beregning
idag = dt.datetime.now()
dette_aar = idag.year
din_alder = dette_aar - alder

###presentasjon av resultat
print(f"Du er altså født i {alder} ")
print(f"Nå er vi i det herrens år {dette_aar} ")
print(f"I {dette_aar} fyller du {int(din_alder)} år, og vi kan vel si at du er rundt halvveis i livet!")


