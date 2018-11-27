####
#Imports 
import pandas as pd

####
#vars
HOTEL_WITH_SCORING = "data/hotels_4_with_review_score.csv"

def test_func(query):
    
    d_hotel = pd.read_csv(HOTEL_WITH_SCORING)
    ret_values = d_hotel.iloc[:,2:].head(20)  
    return ret_values

