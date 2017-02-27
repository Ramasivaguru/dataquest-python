## 1. The Data Set ##

# Weather has been loaded in.
print(weather[0])
print(weather[-1])

## 3. Practice Populating a Dictionary ##

superhero_ranks = {}
superhero_ranks['Aquaman'] = 1
superhero_ranks['Superman'] = 2

## 4. Practice Indexing a Dictionary ##

president_ranks = {}
president_ranks["FDR"] = 1
president_ranks["Lincoln"] = 2
president_ranks["Aquaman"] = 3
fdr_rank = president_ranks.get('FDR')
lincoln_rank = president_ranks.get('Lincoln')
aquaman_rank = president_ranks.get('Aquaman')

## 5. Defining a Dictionary with Values ##

random_values = {"key1": 10, "key2": "indubitably", "key3": "dataquest", 3: 5.6}
print(random_values)
#animals = dict('7'="raven", '8'="goose", '9'="duck")
animals = {7:'raven', 8:'goose', 9:'duck'}
times = {'morning':9, 'afternoon':14, 'evening':19, 'night':23}
#times = dict('9'="morning", '14' = "afternoon", '19' = "evening", '23' = "night")

## 6. Modifying Dictionary Values ##

students = {
    "Tom": 60,
    "Jim": 70
}
students['Ann'] = 85
students['Tom'] = 80
students['Jim'] = students['Jim'] + 5

## 7. The In Statement and Dictionaries ##

planet_numbers = {"mercury": 1, "venus": 2, "earth": 3, "mars": 4}
jupiter_found = 'jupiter' in planet_numbers
earth_found = 'earth' in planet_numbers

## 9. Practicing with the Else Statement ##

planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune", "Uranus"]
short_names = []
long_names = []
for n in planet_names:
    if len(n) > 5:
        long_names.append(n)
    else:
        short_names.append(n)

## 10. Counting with Dictionaries ##

pantry = ["apple", "orange", "grape", "apple", "orange", "apple", "tomato", "potato", "grape"]
pantry_counts = {}
for i in pantry:
    pantry_counts[i] = pantry_counts.get(i,0) + 1


## 11. Counting the Weather ##

weather_counts = {}
for i in weather:
    weather_counts[i] = weather_counts.get(i,0) + 1
