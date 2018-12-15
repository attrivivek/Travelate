# Travelate

## Features
- Original Database used: https://www.kaggle.com/jiashenliu/515k-hotel-reviews-data-in-europe/home
- Search hotels in 6 countries. Countries include: Netherlands, Austria, France, Italy, Kingdom (United Kingdom), or Spain.
- A set of results are returned in response to the query. The information listed for each result is Hotel Name, Hotel Address, Average Score, Sentiment Score, and Number of Reviews.
- Each reasult is also linked to a search result for that hotel in Google. By clicking a result item the user will be taken to a search result page for that hotel item.
- The result page will also have a button that allows the user to go back to the input page to search using a new query.
- The results returned are the top 20 hotels in a given country based on sentiment score from positive and negative reviews and order by average review score derived from aggregating all review scores for a given hotel.
- Incorporated latent aspect analysis which aims to analyze opinions expressed about an entity in a review. The review discussed multiple aspects of the hotel, such as location, value, price etc. Aim was to first define different aspects based on number of related seed words like 'room' aspect has seed words "room", "suite", "view", "bed", "bathroom", "studio". Program found related aspects with the help of word vector representation and comparing similarity between words.    

## Pre-Processing
The following steps had taken place to get the original dataset from https://www.kaggle.com/jiashenliu/515k-hotel-reviews-data-in-europe/home to the one used in the application:  

- Select Variables of interest, which were the following: Hotel Address, Tags, Reviewer Score, Total Reviews, Hotel Name, Average Score, Negative Review, Positive Review, Days Since Review, Negative Review Score, Positive Review Score
- Normalize the Average Score and the Reviewer Score
- Transform data, like days since review from a string to an integer or tags from a string into an array
- Choose 10,000 observations for each of the 6 countries at random (slim down dataset size to 60,000 from the original 515,000)
- Remove reviews in the positive and negative reviews columns that were adding no value. Examples include the following: none, no, nil, nothing, none at all, etc.
- Run the reviews columns through a sentiment analysis scoring algorithm
- Normalize the Negative reviews columns to be between -1 and 0 and Positive reviews columns to be between 0 and 1 
- Aggregate the reviews by hotel and deriving an overall score based on the normalized positive, negative review scores and factors like reviewer rating and number of reviews
- Different weights were used for different factors to keep the scores realistic; e.g higher weight to negative review score than positive review score etc., see aggregate_data.py for more details
- Normalizing the Overall Score the same way the positive and negative review scores were normalized; they range between 0 and 1
- Create an inverted index of tags aggregated by hotel using metapy library after removing stopwords and using analyzer with bigram, icu-tokenizer and ptb-normalizer, see search_indexing.py for more details.
- Creation of aspects and its related seed words post stuying multiple reviews. There were 10 aspects created which could broadly distinguish reviews like value, room, location, cleanliness, service, food, facilities, staff, trip and transport.

## Application 
- The user begins with index.html, which is served by app.py using the Flask library
- When a hotel name is submitted the input value is sent to a Flask function in app.py
- app.py will check to see if the user is searching for one of the 6 countries. If not they are given an error message.
- If the user does search one of the 6 countries then the query is sent to a function in analysis.py
- analysis.py selects the hotels from a given country, chooses the top 20 hotels based on sentiment analysis scores, and sorts these top hotels for that country by average review score. This information is sent as a pandas dataframe back to app.py
- app.py will take this pandas dataframe received from analysis.py and generate HTML content using values of interest from the pandas dataframe
- Once the HTML content is set, the results.html page is rendered by the app.py Flask function using the generated HTML (these are the results the viewer receives from their query)
- The results are generated by creating HTML on a loop from the pandas dataframe.
- Find related aspects: An independent program find_Aspects.py which would iter over all the reviews and then iter on each words in the review (expect stop words), calculate google's word vector similarity between words and each seed words of an aspect. Build a list of similarity values and sort them. Then choose top N unique aspects. N for our program was hard coded as 3 so find top 3 aspects for a review. If similarity was too low (less than threshold value which empirically set to 0.25) then choose less then N aspects. In the end, this program has found a number of aspects for each positive and negative reviews.

## Set Up Environment
- Install Anaconda: https://www.anaconda.com/download/
- After Anaconda installation, open Anaconda Prompt
- In Anaconda prompt install Flask: $ pip install Flask
- Download the Travelate application in desired directory: https://github.com/attrivivek/Travelate
- In Anaconda prompt change directory to the application (assuming in root of Travelate app): /webpage/
- In Anaconda prompt: $ set FLASK_APP=app.py (Windows) or export FLASK_APP=app.py (Mac)
- In Anaconda prompt: $ python -m flask run
- Visit: http://127.0.0.1:5000/
- Enter one of the 6 countries to find top hotels in
- View Results

*** If using Windows you may need to set up your PATH variables for installed items. You can do this in:  
- 'System Properties' -> 
- 'Advanced' -> 'Environment Variables' -> 
- 'Path' (Under 'System Variables') -> 
- 'New' -> 
- Paste path to the desired .exe file downloaded if not using pip install.   

If installing with Anaconda the installations will be a part of the Anaconda path, which should already be set when installing Anaconda. Hence why Anaconda is preferred to run this application.

## Shortcomings / Future Development
- Due to the time frame we only focused on 6 countries. If time had been extended we would have included all countries a user could submit. We would also make it so the user did not have to specify a country name. 
- We would have liked to include filter options in the results page that allowed the user to target specific attributes like review score. Or hotel amenities
- We would have liked to have included amenities in the results info as well.
- We would like to get pricing info for the hotels; this would have been a good addition to the filter attributes.
- Although we began this implementation, we would like to have tags in the index.html page that the user could select, and then those options would be appended to the query to sharpen the search results further.
- We were not able to figure out how to get a Flask function to render results in real time on the same page as the input. With given time we would have liked to add this functionality as well. Maybe even have the results update as the user types.
- We also looked into adding nearby hotels as an option on the results page for thre given hotels returned from the user's query.
- The dataset we worked with included tags which were too ambiguous for querying. The app utilizes country as a query to search by, but given amenities for these hotels we would be able to develop a more robust querying system that not only targets hotels by country, but by amenities that are pertinent to the query.
- Could'nt use metapy because of environment related issue, But would've used sophisticated and state-of-the-art algorithms like OkapiBM25 for user search query ranking and sorting.
- Reviews did not have punctuations which created issues in sentiment analysis. This was handled by normalizing sentiment of reviews.
- Idea is to extend the aspects for each reviews to be searched based on user selection. We could display all the unique aspects in the GUI and allow user to select aspects and provide filtered reviews based on the chosen aspect related to the reviews.

## Tools / Research Papers

1. Latent Aspect Rating Analysis on Review Text Data: A Rating Regression Approach, by Hongning Wang, Yue Lu, Chengxiang Zhai
2. Google's word2vec biinary: https://code.google.com/archive/p/word2vec/
3. Gensim library was used to load a pre-trained google's word2vec binary
4. VADER Sentiment Analysis tool : A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text
