# Election-Sentiment-Analysis
The project is streaming tweets and using Spark MLlib to do sentiment analysis on 2020 election.

Skills applied: <br>
    1. Tweeter Streaming<br>
    2. Spark MLlib <br>
    3. Python library Basemap

Please refer to [Twitter Scrape](https://github.com/dataquestio/twitter-scrape) for streaming. Data are processed: <br>
    1. polarity: 0-positive, 1-netrual, 2-negative <br>
    2. user_localtion: exclude null and locations are not in the states <br>

Result visualizaion:<br>
<img src="images/biden.png" width="500" height="300"> <br>
<img src="images/trump.png" width="500" height="300">
