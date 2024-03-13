## ------ NLP CAPSTONE PROJECT ------ ##

# Importing all necessary packages.
import pandas as pd
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')
import warnings 
warnings.filterwarnings("ignore",
                        message=r".*\[W007\].*",
                        category=UserWarning)

import os

# Creating file path variable
absolute_path = os.path.dirname("amazon_product_reviews.csv")
relative_path = "T21 - Capstone Project - NLP Applications/amazon_product_reviews.csv"
file_path = os.path.join(absolute_path, relative_path)

# Importing data into df, selecting only the reviews.text column 
# and dropping any NAs.
df = pd.read_csv(file_path,
                 dtype={1: str, 10: str})
df = df['reviews.text']
df = df.dropna()


# Creating function to pre-process data that will be called later in 
# the sentiment analysis function.
def cleanText(string):
    """ Return cleaned text:
        - Converted to lowercase
        - Any digits removed
        - Any punctuations removed
        - Any stop words removed 
        - Extra whitespaces removed
    ------
    input: string (str)
    output: cleaned string (str)
    """
     # Converting to lowercase.
    string = string.lower()

    # Removing numbers
    string = "".join([i for i in string if not i.isdigit()])

    # Removing punctuations, stop words and whitespaces using SpaCy.
    text = string
    doc = nlp(text)
    string = "".join(token.text for token in doc if not token.is_punct)
    string = "".join(token.text for token in doc if not token.is_stop)
    string = " ".join(token.text for token in doc if not token.is_space)
    
    return(string)


# Creating function to determine sentiment of text.
def sentiment_analysis(data):
    """ Return sentiment polarity value (between -1 to 1) for
        the inputted text where -1 indicates a very negative sentiment,
        0 indicates a neutral sentiment and 1 indicates a very positive
        sentiment:
    ------
    input: string (str)
    output: polarity (float)
    """
    # First cleaning the data using the defiend cleanText function.
    clean_data = cleanText(data)

    # Performing sentiment analysis using the polarity attribute.
    doc = nlp(clean_data)
    polarity = doc._.blob.polarity

    return(round(polarity,2))


# Generating a random sample of 100 review texts from the data to test 
# the model and also printing the average polarity.
sample_data = df.sample(n=100)
sample_index = list(sample_data.index.values)
sentiment_list = []

print("------- AMAZON REVIEWS SENTIMENT ANALYSIS -------")

for i in sample_index:
    sentiment = sentiment_analysis(sample_data[i])
    sentiment_list.append(sentiment)
    
    # Printing the original (uncleaned) review alongside 
    # its sentiment polarity value.
    print(f"{sample_data[i]}",
           f"Sentiment polarity: {str(sentiment)}",
           sep="\n")
    print("------------------------")

average_polarity = round(sum(sentiment_list) / len(sentiment_list),2)
print(f"AVERAGE SENTIMENT POLARITY: {average_polarity}")


# Finding the semantic similarity value from two random reviews.
my_review_of_choice1 = nlp(df[2085])
my_review_of_choice2 = nlp(df[1087])
similarity = round(my_review_of_choice1.similarity(my_review_of_choice2),2)

print("------------------------")
print(f"1. {df[2085]}",
      f"2. {df[1087]}",
      f"Similarity: {str(similarity)}",
      sep="\n")

