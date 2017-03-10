from read import load_data
import dateutil.parser as dp

hn_stories = load_data()

def parse_time(col):
    return dp.parse(col).hour

hn_stories['submission_hours'] = hn_stories['submission_time'].apply(parse_time)

print(hn_stories.submission_hours.value_counts().head(5))
