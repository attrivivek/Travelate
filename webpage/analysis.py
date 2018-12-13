import pandas as pd

HOTEL_WITH_SCORING = "../data/aggregated_hotels.csv"
COUNTRIES          = ["Netherlands", "Austria", "France", "Italy", "Kingdom", "Spain"]

d_hotel = pd.read_csv(HOTEL_WITH_SCORING)

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

    # tags_dataframe = country_dataframe[any(tag in query for tag in country_dataframe['Tags'])]

    #tags_dataframe = country_dataframe[any(tag in query for tag in country_dataframe['Tags'].str.replace(',]\'',' ').split().tolist())]

    # return temp pandas dataframe that has rows in which tags are in query


    return tags_dataframe

def get_results(query):


    # If update get_tokenizers update this variable
    country_dataframe = d_hotel[(d_hotel['Country']).isin(get_tokenizers(query))]



    #tags_dataframe    = check_tags(query, country_dataframe)

    # At this point you will have pandas dataframe with rows that match by country and tag
    # Use this pandas dataframe to select rows with best score and return
    # Make sure the pandas dataframe at this point is similar to the dataframe from HOTEL_WITH_SCORING

    ret_values = country_dataframe.sort_values( by = ['Overall.Score'], ascending = False )
    ret_values = ret_values.head(20)

    ret_values['Average.Score'] = ret_values['Average.Score'].astype(str)

    return ret_values