import os
import json

"""
Po utworzeniu pliku, załaduj dane do bazy poleceniem:
python manage.py loaddata florist/fixtures/initial_data.json
"""



file_path = os.path.join("initial_data.json")

products = []

categories = [
    {"model": "florist.category", "pk": 1, "fields": {"name": "Cut Flowers", "description": "Single flowers"}},
    {"model": "florist.category", "pk": 2,
     "fields": {"name": "Compositions", "description": "Ready-made bouquets and arrangements"}}
]
products.extend(categories)

cut_flowers = [
    ("Red Rose", "Beautiful red rose, perfect for romantic occasions"),
    ("White Lily", "Elegant white lily symbolizing purity"),
    ("Yellow Tulip", "Cheerful yellow tulip for spring arrangements"),
    ("Pink Carnation", "Classic pink carnation for any occasion"),
    ("Purple Iris", "Majestic purple iris with unique petals"),
    ("Orange Gerbera", "Vibrant orange gerbera daisy"),
    ("Blue Delphinium", "Tall blue delphinium stem"),
    ("White Chrysanthemum", "Traditional white chrysanthemum"),
    ("Pink Peony", "Luxurious pink peony bloom"),
    ("Red Anthurium", "Exotic red anthurium flower"),
    ("Yellow Sunflower", "Bright yellow sunflower"),
    ("Purple Orchid", "Elegant purple orchid stem"),
    ("White Rose", "Classic white rose"),
    ("Pink Lily", "Fragrant pink lily"),
    ("Orange Rose", "Unique orange rose variety"),
    ("Blue Hydrangea", "Fresh blue hydrangea stem"),
    ("Red Tulip", "Traditional red tulip"),
    ("White Gerbera", "Pure white gerbera daisy"),
    ("Yellow Iris", "Sunny yellow iris flower"),
    ("Purple Rose", "Rare purple rose variety")
]

compositions = [
    ("Wedding Bouquet Classic", "Traditional white and pink rose wedding bouquet"),
    ("Spring Joy", "Colorful spring flower arrangement"),
    ("Romantic Evening", "Red roses with white lilies arrangement"),
    ("Birthday Surprise", "Mixed gerbera and carnation bouquet"),
    ("Sympathy Arrangement", "White lily and chrysanthemum composition"),
    ("Valentine's Special", "Dozen red roses with greenery"),
    ("Mother's Day Bouquet", "Pink and purple mixed flower arrangement"),
    ("Graduation Success", "Yellow and white celebration bouquet"),
    ("Business Welcome", "Professional office flower arrangement"),
    ("Garden Fresh", "Mixed seasonal flower bouquet"),
    ("Summer Breeze", "Bright summer flowers composition"),
    ("Autumn Colors", "Fall-themed flower arrangement"),
    ("Winter Wonder", "White and blue winter composition"),
    ("Tropical Paradise", "Exotic flowers arrangement"),
    ("Sweet Memory", "Pastel colors mixed bouquet"),
    ("Royal Purple", "Luxury purple flowers arrangement"),
    ("Golden Sunset", "Orange and yellow flowers mix"),
    ("Pink Cloud", "Soft pink flowers arrangement"),
    ("Ocean Breeze", "Blue and white flowers mix"),
    ("Forest Fresh", "Green and white arrangement")
]

for i, (name, desc) in enumerate(cut_flowers, 1):
    products.append({
        "model": "florist.product",
        "pk": i,
        "fields": {
            "name": name,
            "description": desc,
            "price": f"{9.99 + i}",
            "category": 1,
            "is_composition": False,
            "available": True
        }
    })

for i, (name, desc) in enumerate(compositions, len(cut_flowers) + 1):
    products.append({
        "model": "florist.product",
        "pk": i,
        "fields": {
            "name": name,
            "description": desc,
            "price": f"{49.99 + (i * 2)}",
            "category": 2,
            "is_composition": True,
            "available": True
        }
    })

with open(file_path, "w") as file:
    json.dump(products, file, indent=4)
