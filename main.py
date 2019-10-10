# load packages
import praw
import json
import matplotlib.pyplot as plt

# credentials
with open('credentials.json', 'r') as f:
    credentials = json.load(f)

# create reddit wrapper api
reddit = praw.Reddit(client_id=credentials['client_id'],
                     client_secret=credentials['client_secret'],
                     user_agent='TodayOnReddit')

# collect reddit posts
data = [submission.title for submission in reddit.subreddit('all').hot(limit=10000)]

# specify keywords
keywords = ["Blizzard", "China", "Hong Kong", "Trump", "Riot Games", "Tencent", "Google", "Climate"]

# count occurrences
keyword_count = {}
for keyword in keywords:
    keyword_count[keyword] = len([s for s in data if keyword.lower() in s.lower()])

# plot figure and save
plt.figure(figsize=(8, 6))
plt.title('Number of occurrences in post titles of last 10000 All posts')
plt.bar(keyword_count.keys(), keyword_count.values(), width = 0.8, color = ['blue'])
plt.tight_layout()
plt.savefig('example_img.jpg')
plt.show()
