countries = input().split(", ")
cities = input().split(", ")
new_dict = dict(zip(countries, cities))
for country, city in new_dict.items():
    print(f"{country} -> {city}")