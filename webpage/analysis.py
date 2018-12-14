import pandas as pd

import re

HOTEL_WITH_SCORING = "../data/aggregated_hotels.csv"
COUNTRIES          = ["Netherlands", "Austria", "France", "Italy", "Kingdom", "Spain"]

d_hotel = pd.read_csv(HOTEL_WITH_SCORING)

def get_tokenizers(query):
    # Create temp pandas dataframe

    country_tokens = []

    for word in query.replace(',',' ').split():
        if word.capitalize() in COUNTRIES:
            country_tokens.append( word.capitalize() )

    return country_tokens

    # Instead of returning tokens return rows that have country name found. Use tokens to select rows

def check_tags(query, country_dataframe):
    # Create temp pandas dataframe

    # for every hotel row
        # check if query contains tags for that hotel
            # If so add hotel row to pandas dataframe

    # tags_dataframe = country_dataframe[any(tag in query for tag in country_dataframe['Tags'])]
    # tags_dataframe = country_dataframe

    f = lambda x: re.split(',|[|]| ', x)

    for index, tags in enumerate(country_dataframe['Tags'].apply(f)):
        if any(tag in query for tag in tags):
            tags_dataframe = country_dataframe.loc[:index + 1]

    return tags_dataframe

def get_results(query):


    # If update get_tokenizers update this variable
    country_dataframe = d_hotel[(d_hotel['Country']).isin(get_tokenizers(query))]
    tags_dataframe    = check_tags(query, country_dataframe)

    # At this point you will have pandas dataframe with rows that match by country and tag
    # Use this pandas dataframe to select rows with best score and return
    # Make sure the pandas dataframe at this point is similar to the dataframe from HOTEL_WITH_SCORING

    ret_values = tags_dataframe.sort_values( by = ['Overall.Score'], ascending = False )
    ret_values = ret_values.head(20)
    ret_values = tags_dataframe.sort_values( by = ['Average.Score'], ascending = False )

    return ret_values