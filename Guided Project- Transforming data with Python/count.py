from read import load_data
import collections

hn_stories = load_data()


list_of_words = []
str_of_words = str()
for d in hn_stories['headline']:
    str_of_words += str(d).lower()
    #list_of_words.append(d.lower().split(' '))

list_of_words = str_of_words.split(' ')

c = collections.Counter(list_of_words)

with open('most_common_words.txt', 'w') as f:
    print(c.most_common(100), file = f)