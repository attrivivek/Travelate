
#imports
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from gensim.models import KeyedVectors
import pandas as pd

#global
TOP_N_ASPECTS = 3
THRESHOLD = 0.25

# Dependency
# User needs to download the google's word2vec 'GoogleNews-vectors-negative300.bin' file in the local folder

# Paths
DATSET_PATH = "../data/"
HOTEL_DATASET = DATSET_PATH + "hotels_5.csv"
HOTEL_DATASET_WITH_ASPECTS = DATSET_PATH + "hotels_6_aspects.csv"
GOOGLE_WORD2VEC = "GoogleNews-vectors-negative300.bin"
stopword_txt = "stopwords.txt"

print "Reading word2Vec...."
# google's word2vector
model = KeyedVectors.load_word2vec_format(GOOGLE_WORD2VEC, binary=True)

# aspects and seeds
aspects_seeds = {
    "value" : ['value', 'price', 'quality', 'worth', "expense", "decor", "interior"],
    "room" : ['room', 'suite', 'view', 'bed', "bathroom", "studio"],
    "location" : ['location', 'traffic', 'minute', 'restaurant', "landmark", "city", "noisy", ],
    "cleanliness" : ['clean', 'dirty', 'maintain', 'smell', "surrounding"],
    "service" : ["service", "delay"],
    "food": ["food", "breakfast", "buffet"],
    "facilities" : ["facilities", "sauna", "internet", "computer", "garden", "wifi", "shuttle", "bar", "cafe"],
    "staff" : ["staff", "friendly", "rude", "professional", "receptionist"],
    "trip" : ["trip", "business", "leisure", "family", "weekend", "weekday"],
    "transport" : ["transport", "station", "bus", "train", "metro"],
}

# store mean similarity between each word and aspects
df_top_aspects = pd.DataFrame(columns=['word','aspect','similarity'])

# read hotel dataset
d_hotel = pd.read_csv(HOTEL_DATASET)

# sample sentences
example_sent2 = "Hotel was downtown and staff was friendly"

# filter stop words
stop_word = []
with open(stopword_txt) as fd:
    for line in fd:
        word = line.replace('\n','').replace('\r','')
        stop_word.append(word)
    else:
        print "File reading done."

word_aspect = dict()
top_aspects = list()
dt_top_aspects = list()

# iter over hotel dataset
for index, row in d_hotel.iterrows():

    # init values
    neg_review = pos_review = ""
    word_aspect = dict()
    top_aspects = list()
    dt_top_aspects = list()

    # read negative and positive reviews
    neg_review = row['Negative.Review']
    pos_review = row['Positive.Review']
    count = 0

    reviews = [neg_review, pos_review]
    for sentence in reviews:
        print "review comment: ",sentence
        # empty review
        if pd.isnull(sentence):
            count += 1
            continue
        # create tokens
        word_tokens2 = word_tokenize(sentence)
        # filter stop words
        filtered_sentence2 = [w for w in word_tokens2 if not w in stop_word]
        if not filtered_sentence2:
            count += 1
            continue
        for word in filtered_sentence2:
            for aspect, seeds in aspects_seeds.iteritems():
                print "in the loop for aspects"
                word_aspect[aspect] = 0
                for seed in seeds:
                    # calculate similarity between word and the seed words
                    try:
                        simi = 0.001  # pseudo similarity values
                        simi = model.similarity(word, seed)
                        word_aspect[aspect] += simi
                    except:
                        word_aspect[aspect] += simi
                # calculate the mean of the similarity with each seed word
                word_aspect[aspect] = word_aspect[aspect] / len(seeds)
                temp = {'word': word, 'aspect': aspect, 'similarity': word_aspect[aspect]}
                dt_top_aspects.append(temp)

        df_top_aspects = pd.DataFrame(dt_top_aspects)
        # sort the similarity
        sorted_aspects = df_top_aspects.sort_values(['similarity'], ascending=[0])
        print sorted_aspects.head(5)

        # pick top n aspects
        top_asp = set()
        for index, row in sorted_aspects.iterrows():
            asp = row['aspect']
            top_asp.add(asp)
            if len(top_asp) == TOP_N_ASPECTS:
                break
            if row['similarity'] < THRESHOLD:
                if len(top_asp) > 1:
                    top_asp.remove(asp)
                    break

        filtered_aspects = ""
        for asp in top_asp:
            filtered_aspects += asp + ","
        print "top aspects: ", filtered_aspects

        # add the aspects to the dataframe
        if count == 0:
            "negative"
            d_hotel.set_value(index, 'Neg.Aspect', filtered_aspects)
        elif count == 1:
            "positive"
            d_hotel.set_value(index, 'Pos.Aspect', filtered_aspects)
        # increment count
        count +=1

# store the new dataset
d_hotel.to_csv(HOTEL_DATASET_WITH_ASPECTS)