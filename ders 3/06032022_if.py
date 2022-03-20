#KARŞILAŞTIRMA OPERATÖRLERİ
"""
<  :KÜÇÜKTÜR
>  :BÜYÜKTÜR
<= :KÜÇÜK EŞİT
>= :BÜYÜK EŞİT
== :EŞİTTİR
!= :EŞİT DEĞİLDİR
"""
cinsiyet=input("Bir harf seçiniz:")

if cinsiyet=="e" or cinsiyet=="E":#or:2şarttan biri doğru ise çalışır
    print("Cinsiyet olarak Erkek girdiniz")
    print("if içerisinden selamlar")
elif cinsiyet=="k":
    print("Cinsiyet olarak Kadın girdiniz")
    print("Şuanda elif bloğu içiden selam veriyorum")
else:#şartların dışında herhangi birşey girilirse çalışır
    print("Ben sana e ya da k gir demedim mi?")
print("Şuanda if dışındasın")