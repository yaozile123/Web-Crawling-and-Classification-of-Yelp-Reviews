# Welcome to the Nlp-with-Yelp-review Project
Hello eveyone, this is Zile. I am dedicating in finding the authentic and delicious food around the world. Hope this program could help all of you find the retuarant you will enjoy.

## Purpose of Project
Nowadays, people are busy with their jobs and studies. More and more people didn't wanna waste of their time to try out the new restaurant. Instead, people like to use app like yelp to help them find the restaurant. We would like to use python to analysis the review from yelp to see the 'power' of a comment. In the end, the program will predict whether the review is good or bad for the restaurant. 
## Dependencies
- pandas
- numpy
- requests
- json
- sklearn
- matplotlib
## Collecting data
Yelp is one of the most popular app in food searching. Gourmets would post their reviews for the restaurant they visited. However, Yelp didn't provide any API to download the reviews. What we are gonna do is to collect the data from yelp. We will create a web-crawler by using requests to collect the data.

Using web-crawler based on requests and bs4 to get data from yelp review. Focused on specific word in each review and predict the score 
