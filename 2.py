kilogram = float(input("Skolko kg produktov vy berete: "))
sena_za_kg = float(input("Vvedite senu za kg: "))
sena = kilogram * sena_za_kg
skidka_proz = 0.15
ekonom = sena * skidka_proz
sena_so_skidkoi = sena - ekonom
print(f"Sena produkta bez skidki: {sena:.2f} tenge")
print(f"Vy ekonomyte so skidkoi: {ekonom:.2f} tenge")
print(f"Sena produkta so skidkoi: {sena_so_skidkoi:.2f} tenge")