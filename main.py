import praw
import matplotlib.pyplot as plt

reddit = praw.Reddit(client_id="your client id",
                     client_secret="your client secret",
                     user_agent="my user agent")

data=[]

for submission in reddit.subreddit('all').hot(limit=10000):
    data.append(submission.title)


blizzard = [s for s in data if "blizzard" in s]
Blizzard = [s for s in data if "Blizzard" in s]
china = [s for s in data if 'china' in s]
China = [s for s in data if "China" in s]
hongKong = [s for s in data if "Hong Kong" in s]
hongkong = [s for s in data if "hong kong" in s]
Trump = [s for s in data if "Trump" in s]
trump = [s for s in data if "trump" in s]
riotGames = [s for s in data if 'riot games' in s]
RiotGames = [s for s in data if 'Riot Games' in s]
tencent = [s for s in data if 'tencent' in s]
Tencent = [s for s in data if 'Tencent' in s]
google = [s for s in data if 'google' in s]
Google = [s for s in data if 'Google' in s]
climate = [s for s in data if 'climate' in s]
Climate = [s for s in data if 'Climate' in s]


climate = len(climate) + len(Climate)
google = len(google) + len(Google)
blizzard = len(blizzard) + len(Blizzard)
china = len(china) + len(China)
hongKong = len(hongKong) + len(hongkong)
trump = len(trump) + len(Trump)
riot = len(riotGames) + len(RiotGames)
tencent = len(tencent) + len(Tencent)

print(china, blizzard, hongKong, trump, riot, tencent, google, climate)

left = [1, 2, 3, 4, 5, 6, 7, 8]

height = [blizzard, china, hongKong, trump, riot, tencent, google, climate]

tick_label = ['Blizzard', 'China', 'Hong Kong', "Trump", 'Riot Games', 'Tencent', 'Google', 'Climate']

plt.bar(left, height, tick_label = tick_label,
        width = 0.8, color = ['blue'])

plt.title('Number of occurrences in post titles of last 10000 All posts')

plt.show()
