class Komplex:
    def __init__(self,real=0,img=0):
        self.real = real
        self.img = img

    def __str__(self):
        if self.img >=0:
            return str(self.real)+"+"+str(self.img)+"i"
        else:
            return str(self.real) + str(self.img) + "i"

        def abs(self):
            return (self.real**2+self.img**2)**0.5

        def __add__(self, other):
            return Komplex(self.real+other.real,self.img+other.img)

k1=Komplex( 6,  5)
k2=Komplex( 3, -2)
k3=k1+k2

print(k1)
print(k2)
print(k3)