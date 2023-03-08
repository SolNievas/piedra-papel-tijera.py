from os import system 
from datetime import date
from random import choice
import platform
autor="sol"

so=platform.system()
if so=="Linux":
  s="clear"
else:
  s="cls"
    
hoy =date.today()
dia =hoy.day
mes =hoy.month
anio=hoy.year

system(s)

print (" Autor: "+f" {autor}".rjust(60,"-"))
print (" Fecha: "+f" {dia}/{mes}/{anio}".rjust(60,"-"))

a = (input("jugador 1: piedra, papel, tijera: "))
b = (input("jugador 2: piedra, papel, tijera: "))
  
if a == ("piedra") and b == ("tijera"):
    print("jugador 1 gana")
  
elif a == ("papel") and b == ("piedra"):
    print ("jugador 1 gana")
   
elif a == ("tijera") and b == ("papel"):
    print ("jugador 1 gana")
  
  
elif b == ("piedra") and a == ("tijera"):
    print("jugador 2 gana")
  
elif b == ("papel") and a == ("piedra"):
    print ("jugador 2 gana")

elif b == ("tijera") and a == ("papel"):
    print ("jugador 2 gana")
  
else:
    print ("ninguno gana")
