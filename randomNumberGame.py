#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import random
 
arvaukset = 0

oikeaNumero = random.randrange(1, 21)
#print(oikeaNumero)

print('Tervetuloa pelamaan numeron arvaus peliä.')
pelaajanNimi = input('Mikä on nimesi? ')
print('Heipähei ' + pelaajanNimi + '. Aloitetaan peli. Arvaa numero 1 ja 20 väliltä. Saat arvata 6 kertaa.')
 
while arvaukset < 6:
  arvaus = int(input('Arvaus: '))

  arvaukset += 1
  arvauksiaJaljella = 6 - arvaukset
  
  if arvaus == oikeaNumero:
    break
  elif arvaus < oikeaNumero:
    print('Numero on suurempi kuin ' + str(arvaus) + '. Saat arvata vielä ' + str(arvauksiaJaljella) + ' kertaa.')
  else:
    print('Numero on pienempi kuin ' + str(arvaus) + '. Saat arvata vielä ' + str(arvauksiaJaljella) + ' kertaa.')

if arvaus == oikeaNumero:
  arvaukset = str(arvaukset)
  print('Hieno homma, voitit pelin. Arvattu numero on: ' + str(oikeaNumero) + '. Arvasit numeroa ' + arvaukset + ' kertaa.')

if arvaus != oikeaNumero:
  oikeaNumero = str(oikeaNumero)
  print("Hävisit pelin, oikea numero oli " + oikeaNumero + " :)")