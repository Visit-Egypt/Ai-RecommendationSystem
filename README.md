# Ai-RecommendationSystem


## Recommendation System 
It is a filtration program whose prime goal is to predict the “rating” or “preference” of a user towards a domain-specific item or item. In our case, this domain-specific item is a Place, therefore the main focus of our recommendation system is to filter and predict only those places which a user would prefer given some data about the user him or herself.

## Content-based Filtering Recommendation system
This filtration strategy is based on the data provided about the items. The algorithm recommends products that are similar to the ones that a user has liked in the past. This similarity (generally cosine similarity) is computed from the data we have about the items as well as the user’s past preferences.
For example, if a user likes movies such as ‘The Prestige’ then we can recommend him the movies of ‘Christian Bale’ or movies with the genre ‘Thriller’ or maybe even movies directed by ‘Christopher Nolan’.So what happens here the recommendation system checks the past preferences of the user and find the film “The Prestige”, then tries to find similar movies to that using the information available in the database such as the lead actors, the director, genre of the film, production house, etc and based on this information find movies similar to “The Prestige”.

## Collaborative Filtering Recommendation System

This filtration strategy is based on the combination of the user’s behavior and comparing and contrasting that with other users’ behavior in the database. The history of all users plays an important role in this algorithm. The main difference between content-based filtering and collaborative filtering that in the latter, the interaction of all users with the items influences the recommendation algorithm while for content-based filtering only the concerned user’s data is taken into account.
There are multiple ways to implement collaborative filtering but the main concept to be grasped is that in collaborative filtering multiple user’s data influences the outcome of the recommendation. and doesn’t depend on only one user’s data for modeling.

There are 2 types of collaborative filtering algorithms:

1 - User-based Collaborative filtering

2-  Item-based Collaborative Filtering

![Image](https://editor.analyticsvidhya.com/uploads/88506recommendation%20system.png)


In this implementation, when the user searches for a Tag we will recommend the top 1 similar place using our places recommendation system. We will be using an item-based collaborative filtering algorithm for our purpose. The dataset extracted from  rate of users on the  15  historical places . 


We have two Tables to work  on  : 

1 -  Places 

2-  Rating

Places dataset has:

PlaceId – once the recommendation is done, we get a list of all similar Places
 
Tag – which is not required for this filtering approach.

Ratings dataset has :

userId – unique for each user.

PlaceId – using this feature, we take the Tag of the place from the places dataset.

rating – Ratings given by each user to all the places using this we are going to predict the top 1 similar place.

to make things easier to understand and work with, we are going to make a new dataframe where each column would represent each unique userId and each row represents each unique PlaceId.

## Recommendation system model

We will be using KNN algorithm to compute similarity with Cosine similarity metric which is very fast and more preferable 


## Cosine similarity

measures the similarity between two vectors of an inner product space. It is measured by the cosine of the angle between two vectors and determines whether two vectors are pointing in roughly the same direction. It is often used to measure document similarity in text analysis . 

![image2](https://erikbern.com/assets/2015/09/vector-model1.png)



## recommendation function (get_recommendation , get_similar_users)
The working principle is very simple.  Both functions  work on to get the best places to recommend to the user 

get_similar_users

This function working on find the similar user who has the same interset as  like our target user (  User-based Collaborative filtering ) 

![image](https://github.com/Visit-Egypt/Ai-RecommendationSystem/blob/main/r4.png?raw=true)

get_recommendation

This function working on Recommended places to user depends on user actions ( Item-based Collaborative Filtering)

![image](https://raw.githubusercontent.com/Visit-Egypt/Ai-RecommendationSystem/main/r3.png?token=GHSAT0AAAAAABRI6JN2T4KTHMXRDOIC4QLCYRTWZFA)






