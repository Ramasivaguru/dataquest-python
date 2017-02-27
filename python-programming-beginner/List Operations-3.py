## 2. Parsing the File ##

weather_data = []
f = open('la_weather.csv','r')
#f_data = f.read()
#f_rows = f_data.split('\n')
print(f_rows)
for lines in f_rows:
    weather_data.append(lines.strip().split(','))

## 3. Getting a Single Column From the Data ##

# weather_data has already been read in automatically to make things easier.
weather = []
for row in weather_data:
    weather.append(row[1])

## 4. Counting the Items in a List ##

count = 0
for i in weather:
    count += 1
print(count)
print(len(weather))
print(weather[:5])

## 5. Removing the Header ##

new_weather = weather[1:]
weather = weather.pop(0)
print(weather[0:])

## 6. The In Statement ##

animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]
cat_found = 'cat' in animals
space_monster_found = 'space_monster' in animals

## 7. Weather Types ##

weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]
weather_type_found = []
for i in weather_types:
    weather_type_found.append(i in new_weather)