import math
koshel = int(input("Vashi dengi: "))
print(f"U vas est {koshel} tenge")
alma = 150
almurt = 250
piaz = 80
kilo1 = int(input("Skolko kg yablok vy berete: "))
kilo2 = int(input("Skolko kg grushi vy berete: "))
kilo3 = int(input("Skolko kg luka vy berete: "))
prod1 = alma * kilo1
prod2 = almurt * kilo2
prod3 = piaz * kilo3
itog = prod1 + prod2 + prod3
sitog = koshel - itog
if sitog < 0:
    print("Vam ne hvataet deneg")
else:
    print(f"S vas {itog} tenge")
    print(f"U vas ostalos {sitog} tenge")