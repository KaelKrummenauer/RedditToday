# load packages
import praw
import json
import matplotlib.pyplot as plt
import operator


# credentials
with open('credentials.json', 'r') as f:
    credentials = json.load(f)

# create reddit wrapper api
reddit = praw.Reddit(client_id=credentials['client_id'],
                     client_secret=credentials['client_secret'],
                     user_agent='TodayOnReddit')

# collect reddit posts
data = [submission.title for submission in reddit.subreddit('formula1').hot(limit=100)]

# specify keywords
keywords = ["renault", "racing point", "mercedes", "williams", "ferrari", "red bull","toro rosso", "alfa romeo", "haas", "mclaren"]

# count occurrences
keyword_count = {}
for keyword in keywords:
    keyword_count[keyword] = len([s for s in data if keyword.lower() in s.lower()])

# sort keywords
sortedkeywords = sorted(keyword_count.items(), key = operator.itemgetter(1), reverse = True)

x_val = [x[0] for x in sortedkeywords]
y_val = [x[1] for x in sortedkeywords]

# plot figure and save
plt.figure(figsize=(8, 6))
plt.title('Number of occurrences in post titles of last 100 hot posts in Formula 1')
plt.bar(x_val, y_val, width = 0.8, color = ['blue'])
plt.tight_layout()
plt.show()
