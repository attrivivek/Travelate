import pandas as pd

import re

HOTEL_WITH_SCORING = "../data/aggregated_hotels_2.csv"
COUNTRIES          = ["Netherlands", "Austria", "France", "Italy", "Kingdom", "Spain"]

d_hotel = pd.read_csv(HOTEL_WITH_SCORING)

def get_tokenizers(query):
    country_tokens = []

    for word in query.replace(',',' ').split():
        if word.capitalize() in COUNTRIES:
            country_tokens.append( word.capitalize() )

    return country_tokens

# def check_tags(query, country_dataframe):

#     f = lambda x: re.split(',|[|]| ', x)

#     # for index, tags in enumerate(country_dataframe['Tags'].apply(f)):
#     #     if any(tag in query for tag in tags):
#     #         tags_dataframe = country_dataframe.loc[:index + 1]

#     # return tags_dataframe

#     query_indexes = []

#     for index, row in country_dataframe.iterrows():
#         if any( tag in query for tag in row.Tags ):
#             query_indexes.append( index )

#     if len( query_indexes ) > 0:
#         return query_indexes
#     else:
#         return country_dataframe

def get_results(query):
    country_dataframe = d_hotel[(d_hotel['Country']).isin(get_tokenizers(query))]
    # tags_dataframe    = check_tags(query, country_dataframe)

    ret_values = country_dataframe.sort_values( by = ['Overall.Score'], ascending = False )
    ret_values = ret_values.head(20)
    ret_values = ret_values.sort_values( by = ['Average.Score'], ascending = False )

    return ret_values