#přivítání uživatele
print("vítejte v aplikaci pro výpočet obsahu kruhu")
#přivítání uživatele

r = input("zadejte proměnou r: ")
π = 3,14
#možnost pro zadání proměné

if r>0:
#nesmí být menší než 0
    vysledek = π*r^2
    print("vysledek je:", vysledek)
    #vzoreček pro výpočet
else:
    print("Tak jsi nadrbaný?")