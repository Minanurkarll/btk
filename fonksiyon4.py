#Kullanıcıdan verileri alarak dikdörtgen çevrisini fonksiyon
#yaparak hesaplayınız.

def cevre(a,b):
    return (a+b)*2
def alan(a,b):
    return(a*b)
a_kenar=int(input("a kenar:"))
b_kenar=int(input("b kenar:"))
print("Dikdörtgen alanı:",alan(a_kenar,b_kenar))
print("Dikdörtgen çevresi:",cevre(a_kenar,b_kenar))