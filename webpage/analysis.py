####
#Imports 
import pandas as pd

import metapy

####
#vars
HOTEL_WITH_SCORING = "../data/hotels_4_with_review_score.csv"

# AGG_HOTELS = "../data/aggregated_hotels.csv"

#def get_analysis(hotel_data, query, country):
    # hotel_data = hotel_data[hotal_data == country]
        # Search 10,000k rows

    # return top 20 

def get_results(query):
    #d_hotel = pd.read_csv(HOTEL_WITH_SCORING)

    hotel = pd.read_csv(HOTEL_WITH_SCORING)

    #idx = metapy.index.make_inverted_index('../scripts/config.toml')
    #ret_values = get_analysis(d_hotel, query, country)

    idx = metapy.metapy.index.make_inverted_index('config.toml')

    # ret_values = d_hotel.iloc[:,2:].head(20)  
    # ret_values = ret_values.sort_values( by = ['Average.Score'], ascending = False )

    # query = metapy.index.Document()
    # query.content("1 room")

    ranker = metapy.index.OkapiBM25()

    for result in ranker.score(idx, query, 10):
        ret_values = hotel[hotel['Hotel.Name'] == idx.metadata(result[0]).get('name')]
        print( idx.metadata(result[0]).get('name') )

    return ret_values
