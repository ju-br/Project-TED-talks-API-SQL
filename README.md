# Project-TED-talks-API-SQL
<p align="center">
<img src="https://media2.giphy.com/media/IevSIpwnrMeIwKaF8M/giphy.gif?cid=ecf05e47cx3frmvbxflvjyyxb8g9ppg8zpca3peqh7yxmq5u&rid=giphy.gif&ct=g" width="300" height="200" />
</p>

Technology, Entertainment and Design. Do scientific talks really have to be hard to get? TED talks were firstly released in 2006 with the goal to inform and educate global audiences in an accessible way. Scientists, researchers, technologists, business leaders, artists, designers and other world experts take the TED stage to present “Ideas Worth Spreading”: valuable new knowledge and innovative research in their fields. The talks have an audience of more than 3 billion views annually.

<p>

For TED talks: [https://www.ted.com]

</p>

## Sentiment Analysis - NLP
With 4005 TED talks from 3274 speakers, the descriptions were categorized in positive, negative and neutral with NLP sentiment analysis using NLTK library from python. The talks varied from -0.99 to 0.99 in the NLP sentiment analysis with NLTK/python library. The anaysis is lexicon-based, meaning that the result is based in the count of positive and negative words in a given text and the larger count will be the sentiment attributed to the text. How will the talks be classified using NLP?

</p>


### How talks are classified with NLP - sentiment?
The vast majority of talks is classified as positive using NLP - sentiment analysis. This is expected considering that the TED talks goal is to inspire and engage. Moreover, the thresholds set in the NLTK library are quite restrictive for neutral talk so besides not being expected to have TED talks that are more neutral, we still have to take into account the threshold of -0.05 to 0.05 to be considered neutral.

![KDEsentimentstalks](https://github.com/ju-br/Project-TED-talks-API-SQL/blob/main/figures/Dispersion.png?raw=true)
</p>

### Most viewed talks sentiment - NLP
From the 20 most viewed talks, 19 were classified as positive.

![Viewsandsentiments](https://github.com/ju-br/Project-TED-talks-API-SQL/blob/main/figures/Most_viewed_talks.png?raw=true)
</p>


### Most viewed negative-NLP talks and views
From the talks with higher negative score in NLP, three had more than 5 million views. Taking a closer look to the title of such talks, we can notice that they address topics that are big challenges in our lives. Death, stress, cancer, are topics that we do need to know better how to deal with and to develop strategies. So, in that sense, the more negative ones account with a lot of views because they address topics that are useful and meaningful. Therefore, blindly adopting the label negative can be misleading and restrictive.

![negativeviews](https://github.com/ju-br/Project-TED-talks-API-SQL/blob/main/figures/negativeviews.png?raw=true)
</p>

### Most viewed positive-NLP talks and views
Though the three more negative talks with more views were way more popular than the most positively rated, in general the top 20 more positive have less dispersion.

![positiveviews](https://github.com/ju-br/Project-TED-talks-API-SQL/blob/main/figures/positiveviews.png?raw=true)
</p>

### Correlations between NLP sentiment, views and comments 
The correlations are inexpressive. This is reamarkable especially considering that social media distribution algorythims take engagement as a metric of relevance. This suggests that the NLP sentiment analysis might not be the most reliable way to assess sentiment as if we do not find expected relations (predictive validity).

![correlation](https://github.com/ju-br/Project-TED-talks-API-SQL/blob/main/figures/NLPsentiments%20correlations.png?raw=true)


</p>

## API - How to find the TED talk you want?
In order to organize the search for lectures and make it more eficcient, I developed and API linked to a SQL database. The routes for search are (in a local host):

</p>

'1. Talks: http://127.0.0.1:5000/talks'
</p>
This route will display: title, speaker, year and url of all the talks.


</p>

'2. Sentiment: http://127.0.0.1:5000/<sentiment>'
</p>
Searching for an specific sentiment (negative, neutral, positive), this route will display:
title, speaker, sentiment, comments, views and description from the Talks.

</p>

'3. Talks: http://127.0.0.1:5000//talks/<year>'
</p>
This route allows you to filter the TED talks that were published in a given year from 2006 to 2020. It will display: title, speaker and sentiment.

</p>

'4. Talks: http://127.0.0.1:5000//talks/<speaker>'
</p>
Need inspiration? With the name of the speaker you can get the transcript of the TED talk. This route gives you: title, speaker and transcript.

### Tools used in this project
- python
- SQL
- Natural Language Processing - Sentiment Analysis
- API
