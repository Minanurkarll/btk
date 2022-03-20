import random
seviye=input("Bir seviye seçiniz(kolay/orta/zor):")

if seviye=="kolay":
    uret=random.randint(1,10)#1 ile 10 arasında rastgele tamsayı üretir.
elif seviye=="orta":
    uret=random.randint(1,50)
elif seviye=="zor":
    uret=random.randint(1,100)
else:
    print("lütfen doğru giriş yapınız")
while True:
    seviye=input("Bir seviye seçiniz (kolay/orta /zor):")
   tahmin=int(input("Tahmininiz:"))
   if tahmin==uret:
    print("Tebrikler,sayıyı buldunuz")
    break
   elif tahmin<uret:
    print("Üzgünüm, sayıyı büyültün!")
   else:
    print("Üzgünüm, sayınızı küçültün!")
