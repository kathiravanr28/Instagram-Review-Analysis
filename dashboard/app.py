import streamlit as st
import pandas as pd
from PIL import Image

# Load dataset
data = pd.read_csv("../src/processed_reviews.csv")

# Title
st.title("📱 Instagram Review Analysis Dashboard")

st.write("Natural Language Processing (NLP) analysis of Instagram user reviews.")

# Show dataset
st.subheader("Dataset Preview")
st.dataframe(data.head())

# Sentiment Distribution
st.subheader("Sentiment Distribution")

sentiment_counts = data["sentiment"].value_counts()

st.bar_chart(sentiment_counts)

# Word Cloud
st.subheader("Word Cloud")

wordcloud = Image.open("../images/wordcloud.png")

st.image(wordcloud)

# Bigram Graph
st.subheader("Top Review Bigrams")

bigram = Image.open("../images/top_bigrams.png")

st.image(bigram)

# Sentiment Graph
st.subheader("Sentiment Count Graph")

sentiment_graph = Image.open("../images/sentiment_distribution.png")

st.image(sentiment_graph)

# Show Positive Reviews
st.subheader("Sample Positive Reviews")

positive_reviews = data[data["sentiment"] == "Positive"]

st.write(positive_reviews["content"].head())

# Show Negative Reviews
st.subheader("Sample Negative Reviews")

negative_reviews = data[data["sentiment"] == "Negative"]

st.write(negative_reviews["content"].head())