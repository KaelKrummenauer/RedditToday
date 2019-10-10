# load packages
import praw
import json
import matplotlib.pyplot as plt

# for text
import nltk
from nltk.corpus import stopwords
import spacy
nlp = spacy.load("en")
import gensim
from sklearn.feature_extraction.text import CountVectorizer

# credentials
with open('credentials.json', 'r') as f:
    credentials = json.load(f)

# create reddit wrapper api
reddit = praw.Reddit(client_id=credentials['client_id'],
                     client_secret=credentials['client_secret'],
                     user_agent='TodayOnReddit')

# collect reddit posts
data = [submission.title for submission in reddit.subreddit('all').hot(limit=10000)]

# create stopwords list
stop_words = set(stopwords.words('english'))
stop_words.update(["gonna", "gotta", "just", "like"])

def preprocess(text, irrelevant_pos = ['ADV','PRON','CCONJ','PUNCT','PART','DET','ADP','SPACE']):
    """
    Simple preprocessor that cleans texts and returns a string of selected words
    """
    # text = re.compile(r'<.*?>').sub("", text)
    text = " ".join([token for token in text.split() if token not in stop_words])

    # Create doc
    doc = nlp(text)

    # create tokens
    tokens = [str(token).lower() for token in doc if not token.is_stop and not token.pos_ in irrelevant_pos]
    token_join = " ".join(tokens)

    # use gensim's preprocessing function
    simple = gensim.utils.simple_preprocess(str(token_join), deacc=True)

    return " ".join(simple)

# clean texts
clean_data = [preprocess(text) for text in data]

# function to get top k words
def get_topk_words(text, k=10, ngram_range=(1,1)):
    """
    Returns the top k most freuently occurring words or word sequences
    """
    cv = CountVectorizer(max_df=0.8, stop_words=stop_words, max_features=10000, ngram_range=ngram_range)
    bow = cv.fit_transform(text)
    sum_words = bow.sum(axis=0)
    frequencies = [(word, sum_words[0, idx]) for word, idx in cv.vocabulary_.items()]
    sorted_freq = sorted(frequencies, key=lambda x: (x[1], x[0]), reverse=True)
    return sorted_freq[:k]

# top 20 words/word sequences
top_20_words = get_topk_words(data, k=20, ngram_range=(1, 2))

# plot figure and save
plot_data = {key.title():val for key, val in top_20_words}
plt.figure(figsize=(16, 6))
plt.title('Number of occurrences in post titles of last 10000 All posts', fontsize=16, fontweight='bold')
plt.bar(plot_data.keys(), plot_data.values(), width = 0.8)
plt.xticks(rotation=20, fontsize=12)
plt.tight_layout()
plt.savefig('imgs/example_img_v2.jpg')
plt.show()
