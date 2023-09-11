n=int(input("When you write a number, I will will write the half of it and of all smaller numbers than it (except negative numbers): "))
s=0
def rec(n,z):
    z=+1
    if z==100:
        exit
    if n>-1:
        if n!=0:
            if n%2==0:
                print("Half of ",n," is ",n/2)
            elif n%2!=0:
                m=float((n-1)/2+0.5)
                print("Half of ",n," is ",m)
            rec(n-1,z)
rec(n,s)
print("The half of 0 doesn't exist. Or does it?")
