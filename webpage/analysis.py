####
#Imports 
import pandas as pd

####
#vars
HOTEL_WITH_SCORING = "../data/hotels_4_with_review_score.csv"

def get_results(query):
    
    d_hotel    = pd.read_csv(HOTEL_WITH_SCORING)
    ret_values = d_hotel.iloc[:,2:].head(20)  
    ret_values = ret_values.sort_values( by = ['Average.Score'], ascending = False )

    return ret_values