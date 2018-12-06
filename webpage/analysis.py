####
#Imports 
import pandas as pd

####
#vars
HOTEL_WITH_SCORING = "../data/hotels_4_with_review_score.csv"

def get_analysis(hotel_data, query, country):
    # hotel_data = hotel_data[hotal_data == country]
        # Search 10,000k rows

    # return top 20 

def get_results(query, country):
    d_hotel = pd.read_csv(HOTEL_WITH_SCORING)
    ret_values = get_analysis(d_hotel, query, country)

    # ret_values = d_hotel.iloc[:,2:].head(20)  
    ret_values = ret_values.sort_values( by = ['Average.Score'], ascending = False )

    return ret_values