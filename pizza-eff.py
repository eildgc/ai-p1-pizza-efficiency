import math

# Crear un programa en python para calcular la eficiencia de costo de una pizza, a partir de su costo y diámetro (en cm)
# Mayor área y menor costo es mejor
# La eficiencia se puede expresar como área / costo
# El programa se debe trabajar como archivo de python (con extensión .py). No es necesario usar argumentos desde la terminal.

price = float(input('How much does the pizza cost? '))
diam = float(input("What's the pizza diameter? "))
r = diam/2
area = math.pi *(r**2)

eff = area/price

print(f"Efficiency {eff}")
