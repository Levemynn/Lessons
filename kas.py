import math
aksha= int(input("tenge:"))
alma= 200
almurt=150
banan=250
kilo1=float(input("kansha kg alma:"))
kilo2=float(input("kansha kg almurt:"))
kilo3=float(input("kansha kg banan:"))
zat1 = alma * kilo1 
zat2 = almurt* kilo2
zat3 = banan * kilo3
itog = aksha - (zat1+zat2+zat3)
if itog < 0:
   print(f"sizge {-itog} tenge jetpeidi")
else:
   print (f"sizde {itog} tenge kaldi")