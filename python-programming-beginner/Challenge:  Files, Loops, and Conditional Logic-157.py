## 3. Read the File Into a String ##

f = open('dq_unisex_names.csv','r')
names = f.read()

## 4. Convert the String to a List ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split("\n")
first_five = names_list[:5]
print(first_five)
    

## 5. Convert the List of Strings to a List of Lists ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')
nested_list = []
for n in names_list:
    comma_list = n.split(',')
    nested_list.append(comma_list)
print(nested_list[:5])

## 6. Convert Numerical Values ##

print(nested_list[0:5])
numerical_list = []
for n in nested_list:
 
    l = [n[0],float(n[1])]
    numerical_list.append(l)

print (numerical_list[0:5])

## 7. Filter the List ##

# The last value is ~100 people
numerical_list[len(numerical_list)-1]
thousand_or_greater = []
for n in numerical_list:
    if n[1] >= 1000:
        thousand_or_greater.append(n[0])
print(thousand_or_greater[:10])
    