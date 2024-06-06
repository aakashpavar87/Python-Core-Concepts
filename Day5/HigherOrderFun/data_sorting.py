from data import data

name_finder = lambda item: item["name"]
capital_finder = lambda item: item["capital"]
population_finder = lambda item: item["population"]


sorted_countries_by_name = sorted(data, key=name_finder)
sorted_countries_by_capital = sorted(data, key=capital_finder)
sorted_countries_by_population = sorted(data, key=population_finder)

print(sorted_countries_by_name[1:5])
