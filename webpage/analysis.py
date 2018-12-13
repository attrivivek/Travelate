import pandas as pd

HOTEL_WITH_SCORING = "../data/hotels_5.csv"
COUNTRIES          = ["netherlands", "austria", "france", "italy", "kingdom", "spain"]

def get_tokenizers(query):
    # Create temp pandas dataframe

    country_tokens = []

    for word in query.replace(',',' ').split():
        if word in COUNTRIES:
            country_tokens.append(word)

    return country_tokens

    # Instead of returning tokens return rows that have country name found. Use tokens to select rows

def check_tags(query, country_dataframe):
    # Create temp pandas dataframe

    # for every hotel row
        # check if query contains tags for that hotel
            # If so add hotel row to pandas dataframe
    
    # return temp pandas dataframe that has rows in which tags are in query
    return 0

def get_results(query):
    d_hotel = pd.read_csv(HOTEL_WITH_SCORING)

    # If update get_tokenizers update this variable
    country_dataframe = get_tokenizers(query)
    tags_dataframe    = check_tags(query, country_dataframe)

    # At this point you will have pandas dataframe with rows that match by country and tag
    # Use this pandas dataframe to select rows with best score and return
    # Make sure the pandas dataframe at this point is similar to the dataframe from HOTEL_WITH_SCORING

    ret_values = d_hotel.iloc[:,1:].head(20)
    ret_values = ret_values.sort_values( by = ['Average.Score'], ascending = False )

    return ret_values