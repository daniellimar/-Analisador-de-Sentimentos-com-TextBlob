from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment
    return sentiment.polarity, sentiment.subjectivity

if __name__ == "__main__":
    text = "I love programming. It's amazing and fun!"
    polarity, subjectivity = analyze_sentiment(text)
    print(f"Polarity: {polarity}, Subjectivity: {subjectivity}")
