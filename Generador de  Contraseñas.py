import random
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("¿Cuántos caractéres tendrá tu contraseña? Te recomendamos que tenga mínimo 12 caractéres."))
contraseña = ""
for i in range (longitud):
    contraseña += random.choice(caracteres)
print(contraseña)
