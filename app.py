import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download dataset
nltk.download("vader_lexicon")

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Streamlit UI
st.title("📝 Sentiment Analysis App")
st.write("Enter a comment below and analyze its sentiment.")

# User input
comment = st.text_area("Enter your comment here:")

if st.button("Analyze Sentiment"):
    if comment.strip():
        score = sia.polarity_scores(comment)
        sentiment = "Positive" if score["compound"] > 0 else "Negative" if score["compound"] < 0 else "Neutral"
        st.write(f"**Sentiment:** {sentiment}")
    else:
        st.warning("Please enter a comment.")
