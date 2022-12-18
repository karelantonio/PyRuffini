"""
Software bajo la licencia Apache License 2.0,
puedes obtener una copia en: http://www.apache.org/licenses/LICENSE-2.0.txt
o en el fichero LICENSE

Programa que permite descomponer en factores a un polinomio usando la regla de
ruffini
"""

#Imports
from util import *
from sys import exit

#Metodos
def checkCoefs(coefs: list) -> None:
    poly = toPolinomy(coefs)
    if input(f"El polinomio deberia parecer de la siguiente forma: {poly}, es correcto? [y/n]").lower() in ["n", "no"]:
        print("Saliendo...")
        exit(1)


print("Calculadora de ruffini v1.0")

#Los coeficientes
coefs_str = input("Introduzca los coeficientes > ")
lst = coefs_str.split()
coefs=[]

#Convertimos los coeficientes a numeros
for i in lst:
    coefs.append(int(i))

checkCoefs(coefs)

#Aplicatmos la regla de ruffini
#Obtenemos los divisores del ultimo termino
divs = divisors(coefs[-1])

#Verificamos cada una de las soluciones
sols = []

for i in divs:
    lastV = coefs[0]
    for j in range(1, len(coefs)):
        lastV = lastV*i + coefs[j]

    if lastV==0:
        #Se cumple ruffini, entonces es una solucion
        sols.append(i)

print()

if len(sols)==0:
    print("Parece no tener descomposicion :/ saliendo...")
    exit(0)

print("Las soluciones del ruffini son:", sols)
print("Y el polinomio descompuesto deberia quedar:")

result=""
newcoefs = coefs.copy()

for i in sols:
    poly=toPolinomy([1,-i])
    result=result+f"({poly})"

    tmp=[]
    lastV = 0

    for j in newcoefs[:-1]:
        tmp.append(lastV*i + j)
        lastV=tmp[-1]

    del(lastV)
    del(newcoefs)
    newcoefs=tmp.copy()
    del(tmp)

if not len(newcoefs) in [0,1]:
    last = toPolinomy(newcoefs)
    result=result+f"({last})"

print(result)
