import math

class Fraction :
    def __init__(self,n,d): #initialisation du constructeur / méthode particulière définit pour n'importe quelle classe.Le self ne compte pas
        self.num = n #num et den sont des variables propres
        self.den = d

    def __str__ (self):
        return(f"{self.num} / {self.den}")

    def add(self,other):
        new_num = self.num*other.num + other.num*self.den
        new_den = self.den*other.den
        return (Fraction(new_num,new_den))

    def mult(self,other):
        new_num = self.num*other.num
        new_den = self.den*other.den
        return (Fraction(new_num,new_den))

    def simplify(self):
        r = math.gcd(self.num,self.den)
        self.num = self.num // r
        self.den = self.den // r
        # return(Fraction(new_num,new_den))

def H(n):
    frac = Fraction(1,1)
    for i in range(n):
        frac.add(frac,Fraction(1,i))
    frac.simplify()
    return(frac)



## exercice 1
obj = Fraction(3,4)
# obj.__str__()
print(obj)
str(obj)
##exercice 2
obj2 = Fraction(3,4)
obj3 = Fraction(5,6)
# print(obj2 + obj3)

## multiplier
obj5 = obj2.mult(obj3)
print(obj5)

##simplifier
obj4 = Fraction(210,118)
obj4.simplify()
print(obj4)

## exercice 3
# print('H(100) :', H(10 000))

## exercice 4
def Leib(n):
    Pol = Fraction(1,1)
    for i in range(1,n):
        Pol=Pol.add(Fraction((-1)**i,2*i+1))
    Pol.simplify()
    return (Pol)

print('Leibniz pour n=100 :',Leib(100))


class Polynomial:
    def __init__(self, liste_coeff):
        n= len(liste_coeff)
        for i in range(n):
            self.i=liste_coeff[i]
    def __str__(self, liste_coeff):
        n= len(liste_coeff)
        ans=''
        for i in range(n):
            ans+= f'(+ {self.i}*X**{i})'
        ans= f'({self.n}*X**{n})' + 'ans'
        return ans
    def add(self, P2, n):
        P3=[]
        for i in range(n):
            P3.append= self.i + P2.i
        return Polynomial(P3)
    def deriv(self,n):
        obj2= np.zeros(n)
        for i in range(1,n+1):
            obj2[i-1]=i*self.i
        return Polynomial(obj2)
    def integrate(self, n, C):
        obj2= np.zeros(n+1)
        obj2[0]=C
        for i in range(n+1):
            obj2[i+1]=(self.i)/i
        return Polynomial(obj2)


obj6=Polynomial([1,2,3])

print(obj6)



