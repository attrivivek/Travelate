# Travelate

## Features
- Original Database used: https://www.kaggle.com/jiashenliu/515k-hotel-reviews-data-in-europe/home
- Search hotels in 6 countries using a query from the initial input box. Countries include: Netherlands, Austria, France, Italy, Kingdom (United Kingdom), or Spain.
- A set of results are returned in response to the query. The information listed for each result is Hotel Name, Hotel Address, Average Score, and Number of Reviews.
- Each reasult is also linked to a search result for that hotel in Google. By clicking a result item the user will be taken to a search result page for that hotel item.
- The result page will also have a button that allows the user to go back to the input page to search using a new query.

## Pre-Processing
The following steps had taken place to get the original dataset from https://www.kaggle.com/jiashenliu/515k-hotel-reviews-data-in-europe/home to the one used in the application:  

- Select Variables of interest, which were the following: Hotel Address, Tags, Reviewer Score, Total Reviews, Hotel Name, Average Score, Negative Review, Positive Review, Days Since Review, Negative Review Score, Positive Review Score
- Normalize the Average Score and the Reviewer Score
- Transform data, like days since review from a string to an integer or tags from a string into an array
- Choose 10,000 observations for each of the 6 countries at random (slim down dataset size to 60,000 from the original 515,000)
- Remove reviews in the positive and negative reviews columns that were adding no value. Examples include the following: none, no, nil, nothing, none at all, etc.
- Run the reviews columns through a sentiment analysis scoring algorithm
- Normalize the Negative reviews columns to be between -1 and 0 and Positive reviews columns to be between 0 and 1 

## Application 
- The user begins with index.html, which is served by app.py using the Flask library
- When a query is submitted the input value is sent to a Flask function in app.py
- app.py will check to see if the user is searching for one of the 6 countries. If not they are given an error message.
- If the user does mention one of the 6 countries then the query is sent to a function in analysis.py
- analysis.py utilizes the pandas and metapy library to query the database and return results related to the query in the form of a pandas dataframe back to app.py
- app.py will take this pandas dataframe received from analysis.py and generate HTML content using values of interest from the pandas dataframe
- Once the HTML content is set, the results.html page is rendered by the app.py Flask function using the generated HTML (these are the results the viewer receives from their query)
- The results are generated by creating HTML on a loop from the pandas dataframe.

## Set Up Environment
- Install Anaconda: https://www.anaconda.com/download/
- After Anaconda installation, open Anaconda Prompt
- In Anaconda prompt install metapy: $ pip install metapy
- In Anaconda prompt install Flask: $ pip install Flask
- Download the Travelate application in desired directory: https://github.com/attrivivek/Travelate
- In Anaconda prompt change directory to the application (assuming in root of Travelate app): /webpage/
- In Anaconda prompt: $ set FLASK_APP=app.py (Windows) or export FLASK_APP=app.py (Mac)
- In Anaconda prompt: $ python -m flask run
- Visit: http://127.0.0.1:5000/
- Enter Query and Search
- View Results

*** If using Windows you may need to set up your PATH variables for installed items. You can do this in 'System Properties' -> 'Advanced' -> 'Environment Variables' -> 'Path' (Under 'System Variables') -> 'New' -> Paste path to the desired .exe file downloaded if not using pip install. If installing with Anaconda the installations will be a part of the Anaconda path, which should already be set when installing Anaconda. Hence why Anaconda is preferred to run this application.

## Shortcomings / Future Development
- Due to the time frame we only focused on 6 countries. If time had been extended we would have included all countries a user could submit. We would also make it so the user did not have to specify a country name. 
- We would have liked to include filter options in the results page that allowed the user to target specific attributes like review score.
- We would hae liked to have included amenities in the results info as well.
- We would like to get pricing info for the hotels; this would have been a good addition to the filter attributes.
- Although we began this implementation, we would like to have tags in the index.html page that the user could select, and then those options would be appended to the query to sharpen the search results further.
- We were not able to figure out how to get a Flask function to render results in real time on the same page as the input. With given time we would have liked to add this functionality as well. Maybe even have the results update as the user types.
- We also looked into adding nearby hotels as an option on the results page for thre given hotels returned from the user's query.
- We owuld have liked to explore metapy further to implement potentially more powerful algorithms for retrieval. Even consult other research papers for state-of-the-art retrieval methods.
- We attempted to use metapy, but ran into issues getting metapy to return a pandas dataframe and also to work on the Flask server.