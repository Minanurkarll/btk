"""
kullanıcı yılsonu ortalaması girsin.ortalama 85 üsüt ise takdir,70 üstü teşekkür,
bunların dışında ise hiçbirşey almadınız desin.
"""
ortalama=int(input("Yılsonu otalamanız:"))
if ortalama>=85:
    print("Takdir belgesi aldınız")
elif ortalama>=70:
    print("Teşekkür belgesi aldınız")
else oratlama>=