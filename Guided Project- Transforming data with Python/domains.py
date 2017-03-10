from read import load_data
import pandas as pd

hn_stories = load_data()
most_domains = hn_stories.url.value_counts()
most_domains.sort_values(ascending = False, inplace = True)

limit = 1

for i,v in most_domains.items():
    if limit > 100:
        break
    limit += 1
    print('{0} : {1}'.format(i,v))
    