sotrudniki = [
    {"Imya": "Maxim", "zarplata": 3500},
    {"Imya": "Alexander", "zarplata": 4000},
    {"Imya": "Natasha", "zarplata": 3000},
    {"Imya": "Oleg", "zarplata": 2500}
]
obshaya_zarplata = 0
num_sotrudnikov = len(sotrudniki)
for sotrudniki in sotrudniki:
    obshaya_zarplata += sotrudniki["zarplata"]
srednyya_zarplata = obshaya_zarplata / num_sotrudnikov
print(f"Srednyya zarplata: {srednyya_zarplata}")