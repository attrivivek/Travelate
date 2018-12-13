####
#Imports 
import pandas as pd

import metapy

####
#vars
HOTEL_WITH_SCORING = "../data/hotels_4_with_review_score.csv"

AGG_HOTELS = "../data/aggregated_hotels.csv"

#def get_analysis(hotel_data, query, country):
    # hotel_data = hotel_data[hotal_data == country]
        # Search 10,000k rows

    # return top 20 

def get_results(query):
    hotel = pd.read_csv(AGG_HOTELS)

    # hotel = pd.read_csv(AGG_HOTELS)

    # idx = metapy.index.make_inverted_index('../scripts/config.toml')
    #ret_values = get_analysis(d_hotel, query, country)

    # idx = metapy.metapy.index.make_inverted_index('config.toml')

    ret_values = hotel.sort_values(by = ['Overall.Score'], ascending = False )
    ret_values = ret_values.head(20)

    # query = metapy.index.Document()
    # query.content("austria")

    # ranker = metapy.index.OkapiBM25()

    # for result in ranker.score(idx, query, 10):
    #     print (hotel[hotel['Hotel.Name'] == idx.metadata(result[0]).get('name')])

    # ret_values = d_hotel.filter(['Hotel.Name','Average.Score','Total.Reviews', 'Hotel.Address'], axis=1)

    ret_values['Hotel.Name'] = ret_values['Hotel.Name'].astype(str)
    ret_values['Average.Score'] = ret_values['Average.Score'].astype(str)
    ret_values['Total.Reviews'] = ret_values['Total.Reviews'].astype(str)
    ret_values['Hotel.Address'] = ret_values['Hotel.Address'].astype(str)
    ret_values['Overall.Score'] = ret_values['Overall.Score'].astype(str)
    return ret_values
