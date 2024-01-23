#přivítání uživatele
print("vítejte v aplikaci pro výpočet obsahu kruhu")
#přivítání uživatele

a = input("zadejte proměnou a:-")
b = input("zadejte proměnou b:-")
#možnost pro zadání proměné

if a>0 and b>0:
#nesmí být menší než 0
    vysledek = a*b
    print("vysledek je:", vysledek)
    #vzoreček pro výpočet
else:
    print("Tak jsi nadrbaný?")