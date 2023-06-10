zaem = input("Skolko hotite vzyat deneg: ")
zaem = int(zaem)
proz = input("Pod kakoi prosent vam ih daiut: ")
proz = int(proz)
years = input("Naskolko let berete: ")
years = float(years)
proz = proz / 100
month_pay = (zaem * proz * (1+ proz)**years) / (12 * ((1 + proz)**years - 1))
print("Vash mesyachnyi platezh sostavit: %.2f" % month_pay)
summa = month_pay * years * 12
print("Za ves period vy zaplatite: %.2f" % summa)
print("Eto sostavit %.2f%% ot pervonachalnoi summy" % ((summa/zaem) * 100))