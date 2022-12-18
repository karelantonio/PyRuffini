"""
Software bajo la licencia Apache License 2.0,
puedes obtener una copia en: http://www.apache.org/licenses/LICENSE-2.0.txt
o en el fichero LICENSE

Algunos metodos utiles
"""

def divisors(num: int) -> list:
    """Descompone en factores primos un numero"""
    #Factores primos
    terms = []

    for i in range(1, num+1):
        #Si es divisible por {i}
        if not num%i:
            terms.append(i);terms.append(-i)

    return terms

def intToSuperIndex(num: int) -> str:
    indxs = {"0":"⁰", "1":r"¹", "2":r"²", "3":"³", "4":"⁴", "5":"⁵",
            "6":"⁶", "7":"⁷", "8":"⁸", "9":"⁹"}
    numstr = str(num)
    newstr = ""
    for i in numstr:
        newstr=newstr+indxs[i]
    return newstr


def numToNiceStr(num: int) -> str:
    if num>0:
        return "+"+str(num)
    else:
        return str(num)


def toPolinomy(coefs: list) -> str:
    val = " "
    deg = len(coefs)
    isFst=True
    for i in coefs:
        deg=deg-1
        sign=True #Cuando es el primer termino se puede omitir

        #Si es 0, omitimos ese termino
        if i == 0:
            continue

        #Si es el primer termino, podemos omitor el signo positivo
        if isFst:
            num=str(i)
            isFst=False
            sign=False
        else:
            num=numToNiceStr(i)
            
        #Si es 1 o -1, podemos omitir el coeficiente, solo especificar el signo
        #claro esta que no puede ser el ultmo termino
        if i==-1 and not deg==0:
            val+val+"-"
        elif i==1 and not deg==0:
            if not sign:
                sign=True
            else:
                val=val+"+"
        else:
            val=val+num


        if deg==1:
            val=val+"x"
        elif deg!=0:
            val=val+"x"+intToSuperIndex(deg)
        val = val + " "
    return val

if __name__=="__main__":
    print("Making some tests...")
    print("Divisors or 27:", divisors(27))
    print("Divisors of 30:", divisors(30))
    print("Divisors of 3 :", divisors(27))
    print("Exponent: 1234567890:", intToSuperIndex(1234567890))
    print("Coeficients to polinomy (1 2 0 4 5):", toPolinomy([1,2,3,4,5]))

