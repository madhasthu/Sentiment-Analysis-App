import nltk
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the required dataset
nltk.download("vader_lexicon")

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Take user input
print("Enter your comments (type 'exit' to stop):")
comments = []
MAX_COMMENTS = 5  # Set limit

while len(comments) < MAX_COMMENTS:
    comment = input("> ")
    if comment.lower() == "exit":
        break
    comments.append(comment)


# Analyze sentiment and store results
results = []
for comment in comments:
    score = sia.polarity_scores(comment)
    sentiment = "Positive" if score["compound"] > 0 else "Negative" if score["compound"] < 0 else "Neutral"
    results.append({"Comment": comment, "Sentiment": sentiment})

# Convert to DataFrame and save to CSV
df = pd.DataFrame(results)
df.to_csv("sentiment_results.csv", index=False)

# Display results
print("\nSentiment Analysis Results:")
print(df)
print("\nResults saved to sentiment_results.csv")
