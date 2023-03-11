"""Programa que permite calcular ruffini sencillamente"""

#The exponent chars
exp_arr = {"1":chr(185),
        "2":chr(178),"3":chr(179),"4":chr(8308),
        "5":chr(8309),"6":chr(8310),"7":chr(8311),
        "8":chr(8312),"9":chr(8313),"0":chr(8304)}


class Polinomy():
    "A polinomy, allows you to do some basic operations"
    def __init__(self, termList:list):
        "Default constructor"
        self.coefs=termList
        self.lastTerm=termList[-1]

    def __mod__(self, value:int ):
        "Apply MOD: Polinomy%Val to check the synthetic div. result"
        last=0
        for i in self.coefs:
            last=last*value + i
        return last

    def __truediv__(self, value):
        "Applies the div. assumes the polinomy can be divided by the given (x+value) binomy"
        self.coefs.pop()
        last=0
        pos=0
        for i in self.coefs:
            last=last*value + i
            self.coefs[pos]=last
            pos+=1
        self.lastTerm=self.coefs[-1]
        return last

    def __len__(self):
        "Apply len(Polinomy)"
        return len(self.coefs)

    def zeros(self):
        "Get the right zeros"
        count=0
        for i in range(len(self)-1, -1, -1):
            if self.coefs[i]!=0:
                break
            count+=1
        return count


def generateDivisors(term):
    for i in range(1, term):
        if term%i == 0:
            yield -i
            yield i

    yield -term
    yield term


def exp(num):
    "Convert a string num into an exponent num"
    if type(num)==int:
        if num==1:
            return ""
        num=str(num)

    bld=""
    for i in num:
        if i in exp_arr:
            bld+=exp_arr[i]
        else:
            bld+=i
    return bld


def reprPolinomy(coefs, expon: int):
    "Pretty-print of a polinomy"
    if type(coefs) == int:
        if coefs==0:
            return "x"+exp(expon)
        else:
            if coefs>0:
                return f"(x-{coefs})"+exp(expon)
            else:
                return f"(x+{abs(coefs)})"+exp(expon)
    else:
        bld="("
        pos=0
        deg=len(coefs)-1
        for i in coefs:
            if i==0:
                continue
            elif pos==deg:
                if i>0:
                    bld+="+"
                bld+=f"{i}"
            elif i==1:
                bld+=f"x{exp(deg-pos)}"
            elif i==-1:
                bld+=f"-x{exp(deg-pos)}"
            else:
                if i>0:
                    bld+="+"
                bld+=f"{i}x{exp(deg-pos)}"
            pos+=1

        bld+=")"+exp(expon)
        return bld


if __name__=="__main__":
    line = input("Introduzca los coeficientes > ")
    pol = Polinomy([ int(x) for x in line.split() ])

    factors=[]
    
    for i in range(pol.zeros()):
        pol/0
        factors.append(0)

    for i in generateDivisors(pol.lastTerm):
        while(pol%i == 0):
            pol/i
            factors.append(i)

        if len(pol) < 2:
            break

    #Print the factorized result
    bld=""
    count=0
    last=-1
    for i in factors:
        if count==0:
            last=i
            count=1
            continue
        if last==i:
            count+=1
        else:
            bld+=reprPolinomy(last, count)
            count=1
            last=i
    if len(factors)>0:
        bld+=reprPolinomy(last, count)

    if len(pol)>=2:
        bld+=reprPolinomy(pol.coefs, 1)

    print(bld)

