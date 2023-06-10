chislo1 = float(input())
chislo2 = float(input())
operasya = input()
if chislo2 == 0:
    print("Деление на 0!")
elif operasya == "+":
    print(chislo1 + chislo2)
elif operasya == "-":
    print(chislo1 - chislo2)
elif operasya == "/":
    print(chislo1 / chislo2)
elif operasya == "*":
    print(chislo1 * chislo2)
elif operasya == "mod":
    print(chislo1 % chislo2)
elif operasya == "pow":
    print(chislo1 ** chislo2)
elif operasya == "div":
    print(chislo1 // chislo2)