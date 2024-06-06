from collections import Counter

from data import data

name_finder = lambda item: item["name"]
capital_finder = lambda item: item["capital"]
population_finder = lambda item: item["population"]


sorted_countries_by_name = sorted(data, key=name_finder)
sorted_countries_by_capital = sorted(data, key=capital_finder)
sorted_countries_by_population = sorted(data, key=population_finder)

# for country in sorted_countries_by_capital[1:6]:
#     print(country)

# for country in sorted_countries_by_population[1:7]:
#     print(country["population"])

languages_counter = Counter()
location_map = {}

for country in data:
    for language in country["languages"]:
        languages_counter[language] += 1
        if language in location_map:
            location_map[language].append(country["name"])
        else:
            location_map[language] = [country["name"]]

# Step 2: Sort the languages by their frequency
most_common_languages = languages_counter.most_common(10)

# Step 3: Retrieve the top ten most spoken languages along with their locations
top_ten_languages_by_location = {
    lang: location_map[lang] for lang, count in most_common_languages
}

# ! Sorting ten most populated Countries

# ? extracting countries and population

countries_with_population = [
    (country["name"], country["population"]) for country in data
]

sorted_countries = sorted(
    countries_with_population, key=lambda item: item[1], reverse=True
)

print(sorted_countries[:10])

# Output the result
# print(top_ten_languages_by_location)
# print(sorted_countries_by_capital[1:6])
# print(sorted_countries_by_population[1:7])
# for country in sorted_countries_by_name[1:5]:
#     print(country["name"])
