#kendisine gönderilen kullanıcı adı veya şifreyi kontrol ederek
#sonucunda True ya da False gönderen fonksiyon python kodu
#kullanıcıadı :admin,şifre123456 olmalı

def kontrol(kullanici,sifre):
kullanici=input("Kullanıcı adınız:")
sifre=input("Parolanız:")
if kullanici=="admin" and sifre=="123456":
    return True
else:
    return False
kullanici=input("Kullanıcı adınız:")
sifre=input("Şifreniz:")
sonuc=kontrol("Kullaıcı adınız")