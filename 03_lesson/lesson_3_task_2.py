from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 13", "+79161234567"),
    Smartphone("Samsung", "Galaxy S22", "+79261234568"),
    Smartphone("Xiaomi", "Mi 11", "+79371234569"),
    Smartphone("Google", "Pixel 6", "+79481234560"),
    Smartphone("OnePlus", "9 Pro", "+79591234561"),
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
