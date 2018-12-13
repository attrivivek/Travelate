import pandas as pd
import math


# Variables
HOTEL_WITH_SCORING = "../data/hotels_5.csv"

AGG_HOTELS = "../data/hotels_4_with_review_score.csv"

WEIGHTS = [20, 10, 5, 2, 0.00001]

# Read Detailed hotels CSV

data = pd.read_csv(HOTEL_WITH_SCORING)

# Aggregate data

aggregations = {'Neg_Review_Score': 'mean',
                'Pos_Review_Score': 'mean',
                'Reviewer.Score': 'mean',
                'Average.Score': 'mean',
                'Total.Reviews': 'mean',
                }

hotel_agg = data.groupby(['Hotel.Name']).agg(aggregations)

# Aggregate all tags

hotel_agg['Tags'] = data.groupby(['Hotel.Name'])['Tags'].apply(list)

# Create an overall score

hotel_agg['Overall.Score'] = WEIGHTS[0] * hotel_agg['Neg_Review_Score'] + \
                             WEIGHTS[1] * hotel_agg['Pos_Review_Score'] + \
                             WEIGHTS[2] * hotel_agg['Reviewer.Score'] +  \
                             WEIGHTS[3] * hotel_agg['Average.Score'] + \
                             WEIGHTS[4] * hotel_agg['Total.Reviews']

hotel_agg['Hotel.Address'] = data['Hotel.Address']

# Write to aggregated csv

hotel_agg.to_csv(AGG_HOTELS)





