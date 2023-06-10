product_records = [
    {"product_id": 1, "name": "Keyboard", "price": 25.99},
    {"product_id": 2, "name": "Mouse", "price": 19.99},
    {"product_id": 3, "name": "Monitor", "price": 199.99},
    {"product_id": 4, "name": "Headphones", "price": 49.99},
    {"product_id": 5, "name": "Printer", "price": 149.99},
    {"product_id": 6, "name": "Speakers", "price": 79.99},
    {"product_id": 7, "name": "Laptop", "price": 899.99}
]
Numb = int(input("Vvedite chilso dlya topa: "))
sortirovannye = sorted(product_records, key=lambda x: x["price"], reverse=True)
top_numb_producty = sortirovannye[:Numb]
print(f"Top {Numb} Samyh dorogih produktov:")
for i, product in enumerate(top_numb_producty, start=1):
    print(f"{i}. {product['name']} - ${product['price']}")