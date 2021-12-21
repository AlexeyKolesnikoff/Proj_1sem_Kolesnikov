# Вариант 20
# Известны марки машин, выпускаемые в данной стране и экспортируемых в N заданных
# стран. Определить какие марки машин были доставлены во все указанные страны, какие в
# некоторые из стран и какие не доставлены ни в одну страну.

cars =  {'BMW', 'Mercedes-Benz', 'Audi', 'Opel', 'Volkswagen'}
print("Машины, выпускаемые в данной стране: ", cars)

country1 = {'BMW', 'Mercedes-Benz', 'Audi'}
print("Машины поставляемые в 1-ую страну: ", country1)

country2 = {'BMW', 'Audi', 'Volkswagen'}
print("Машины поставляемые в 2-ую страну: ", country2)

country3 = {'Mercedes-Benz', 'BMW', 'Volkswagen'}
print("Машины поставляемые в 3-ю страну: ", country3)

print("Машины, которые были доставлены во все страны: ", ','.join(country1 & country2 & country3))
print("Машины, доставленные в некоторые страны:", ','.join((country1 | country2 | country3) & cars))
print("Машины, которые не доставляются ни в одну из стран: ", ','.join(cars - (country1 | country2 | country3)))


