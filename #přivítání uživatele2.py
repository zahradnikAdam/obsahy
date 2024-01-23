#přivítání uživatele
print("vítejte v aplikaci pro výpočet objemu kvádru")
#přivítání uživatele

a = input("zadejte proměnou a:-")
b = input("zadejte proměnou b:-")
c = input("zadejte proměnou c-")
#možnost pro zadání proměné

if a>0 and b>0 and c>0:
#nesmí být menší než 0
    vysledek = a*b*c
    print("vysledek je:", vysledek)
    #vzoreček pro výpočet
else:
    print("Tak jsi nadrbaný?")