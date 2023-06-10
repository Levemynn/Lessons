jyl = int(input("Jyl engiz: "))
januarlar = {
    0: "Mezhin",
    1: "Tauyq",
    2: "It",
    3: "Donyz",
    4: "Tyzhqan",
    5: "Siyr",
    6: "Barys",
    7: "Qoian",
    8: "Ulu",
    9: "Zhylan",
    10: "Zhylqy",
    11: "Qoi"
}
januar_jyl = jyl % 12
januar = januarlar[januar_jyl]
print(f"{jyl} zhyl {januar} saikes keledi")