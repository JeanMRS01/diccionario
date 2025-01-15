
import random

caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

contraseña = ""

long = int(input("Introduzca la longitud de la contraseña: "))

for i in range(long):
    contraseña += random.choice(caracteres)
    
print ("Tu contraseña es:", contraseña)