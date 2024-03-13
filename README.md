# Sentiment Analysis Final Capstone Project

## Description
This is a final capstone project where I have written a script to analyse the sentiment polarity of Amazon product reviews. The script contains functions to clean/preprocess the data,  measure the sentiment polarity and usage of the functions to analyse a sample of the dataset. It also calculates the semantic similarity of two reviews from the dataset. This repo also contains a short report of my findings called "sentiment_analysis_report.pdf". 

## Installation and usage
1. Download "sentiment_analysis.py" and "amazon_product_reviews.rar" into your local directory and unzip the .rar file to obtain the "amazon_product_reviews.csv" dataset.
2. Open the .py file and change the file path on **line 17** to your local directory with the "amazon_product_reviews.csv" file.
3. Run the file to generate the sentiment polarity of a random sample of 100 reviews and the semantic similarity value of review #2085 and review #1087.
   - **OPTIONAL** You can modify the n value on **line 74** to generate a random sample number of your choosing (up to n = 34660)
   - **OPTIONAL** You can modify the df[] values on **line 96** and **line 97** to any values (between 0-34659) to compare the similarity of two reviews of your choosing.

## Credits
The dataset used in this project was obtained from [this](https://www.kaggle.com/datasets/datafiniti/consumer-reviews-of-amazon-products) kaggle.com dataset. 
