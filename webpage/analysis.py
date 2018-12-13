import pandas as pd

HOTEL_WITH_SCORING = "../data/hotels_5.csv"
COUNTRIES          = ["netherlands", "austria", "france", "italy", "kingdom", "spain"]

def get_tokenizers(query):
    country_tokens = []

    for word in query.split():
        if word in COUNTRIES:
            country_tokens.append(word)

    return country_tokens

def get_results(query):
    d_hotel = pd.read_csv(HOTEL_WITH_SCORING)

    country_tokens = get_tokenizers(query)

    ret_values = d_hotel.iloc[:,1:].head(20)
    ret_values = ret_values.sort_values( by = ['Average.Score'], ascending = False )

    return ret_values