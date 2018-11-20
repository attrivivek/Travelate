
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer, BOOSTER_DICT
from nltk import tokenize
import sys, os
import pandas as pd

# Global variables
# sentiment classification
sentiment = {"-2": "very negative", "-1": "negative", "0": "neutral",
             "1": "positive", "2": "very positive"}
# dataset path
DATSET_PATH = "../data/"
HOTEL_DATASET = DATSET_PATH + "hotels_3.csv"
HOTEL_DATASET_WITH__SCORE = DATSET_PATH + "hotels_3_with_review_score.csv"

def check_sentiment(score):
    senti = .99  # default value
    if score >= 0.8:
        senti = 2
    elif (score >= 0.3 and score < 0.8):
        senti = 1
    elif (score >= -0.3 and score < 0.3):
        senti = 0
    elif (score < -0.3 and score >= -0.75):
        senti = -1
    else:
        senti = -2
    return sentiment[str(senti)]


# --- static examples fetched from moneycontrol -------
sentences = [
            "The plot was good, but the characters are uncompelling and the dialog is not great.",
            "RBI to soon re-introduce one rupee currency notes in circulation",
            "Babri Masjid case: Advani, Joshi, Bharti charged with criminal conspiracy - as it happened",
            "Swiggy raises $80 million in Series E funding led by Naspers",
            "Mahindra to infuse Rs 12,000 crore over 3 years, improve UV marketshare",
            "Ashok Leyland developing own technology to meet BS-VI standards",
            "JLR cuts prices of select models by up to Rs 10.9 lakh",
            "Swizz is an awesome, great and fantastic place to visit!!!"
            ]


def analyse_sentiment(input_sentence, choice):
    analyzer = SentimentIntensityAnalyzer()
    if choice == 2:
        calculate_sentiments = [input_sentence]
    elif choice == 1:
        calculate_sentiments = sentences
    elif choice == 3:
        vs = analyzer.polarity_scores(input_sentence)
        return vs["compound"]   
    for sentence in calculate_sentiments:
        vs = analyzer.polarity_scores(sentence)
        print("{:-<70} :: (sentiment score ->) {}".format(sentence, check_sentiment(vs["compound"])))

    return vs["compound"]   

def read_dataset():

    global HOTEL_DATASET
    d_hotel = pd.read_csv(HOTEL_DATASET)
    #print d_hotel.head(10) 
    print "columns:", d_hotel.columns.values
    d_hotel = d_hotel.reindex( columns = d_hotel.columns.tolist() + ['Neg_Review_Score','Pos_Review_Score'])
    print "columns:", d_hotel.columns.values
    for index, row in d_hotel.iterrows(): 
        print "N:", row['Negative Review'], "    ", "P", row['Positive Review']
        n_review = analyse_sentiment(row['Negative Review'], choice=3)     
        p_review = analyse_sentiment(row['Positive Review'], choice=3)
        d_hotel.set_value(index, 'Neg_Review_Score', n_review)
        d_hotel.set_value(index, 'Pos_Review_Score', p_review)    
        print "n_Score: ", n_review, "    ", "p_Score: ", p_review
        #if index ==5:
        #    break

    # Save Hotels Dataset
    d_hotel.to_csv(HOTEL_DATASET_WITH__SCORE)

    

if __name__ == '__main__':
    while(True):
        print("Choose options by entering 0/1/2/3:\n")
        print("1)Sentiment Analysis of static text.")
        print("2)Input a sentence to perform sentiment analysis.")
        print("3)Read hotel dataset.")
        print("0) To Quit")
        choice = int(raw_input("Enter Choice (0/1/2/3):"))
        #calculate sentiment for the sentences already in the program
        if choice == 0:
            sys.exit(0)
        if choice==1:
            print "Scoring: ", analyse_sentiment("", choice)
        #input the sentence
        elif choice == 2:
            capture_sentence = str(raw_input("Enter the sentence :"))
            #calculate sentence for the input sentence
            print "Scoring: ", analyse_sentiment(capture_sentence, choice)
        elif choice == 3:
            read_dataset()   
        else:
            print("Error: Input correct option")


