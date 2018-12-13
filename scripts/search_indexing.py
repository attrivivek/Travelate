import metapy

import pandas as pd

AGG_HOTELS = "../data/aggregated_hotels.csv"


hotel = pd.read_csv(AGG_HOTELS)

doc = metapy.index.Document()
# ana = metapy.analyzers.load('config.toml')

idx = metapy.index.make_inverted_index('config.toml')


query = metapy.index.Document()
query.content("1 room France")

ranker = metapy.index.OkapiBM25()



for result in ranker.score(idx, query, 10):
    print hotel[hotel['Hotel.Name'] == idx.metadata(result[0]).get('name')]
    #print idx.metadata(result[0]).get('name')


#for tag in hotel['Tags']:
# doc.content(hotel['Tags'][1])
# print hotel['Tags'][1]
# print(ana.analyze(doc))
