# scripts/sentiment_analyzer.py

# Import dependencies
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download necessary NLTK resources
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('vader_lexicon')

class SentimentAnalyzer:
    def __init__(self, data_path):
        """Initialize SentimentAnalyzer with dataset path."""
        self.data_path = data_path
        self.df = pd.read_csv(data_path)
        self.sia = SentimentIntensityAnalyzer()
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words("english"))

    def preprocess_text(self, text):
        """Tokenize, remove stopwords, and lemmatize text."""
        tokens = word_tokenize(text.lower())
        tokens = [self.lemmatizer.lemmatize(word) for word in tokens if word.isalnum() and word not in self.stop_words]
        return ' '.join(tokens)

    def get_vader_sentiment(self, text):
        """Compute sentiment score & label using VADER."""
        scores = self.sia.polarity_scores(text)
        sentiment_label = "positive" if scores['compound'] > 0.05 else "negative" if scores['compound'] < -0.05 else "neutral"
        return scores['compound'], sentiment_label

    def apply_sentiment_analysis(self):
        """Apply sentiment analysis to processed reviews."""
        self.df["processed_review"] = self.df["review"].apply(self.preprocess_text)
        self.df[["sentiment_score", "sentiment_label"]] = self.df["processed_review"].apply(lambda x: pd.Series(self.get_vader_sentiment(x)))

    def save_results(self, output_path):
        """Save processed dataset with sentiment scores & labels."""
        self.df.to_csv(output_path, index=False)
        print(f"✅ Sentiment analysis completed and saved to {output_path}!")

    def run_analysis(self, output_path="data/sentiment_reviews.csv"):
        """Execute full sentiment analysis pipeline."""
        print("🚀 Running Sentiment Analysis Pipeline...")
        self.apply_sentiment_analysis()
        self.save_results(output_path)

# Allow module import without auto-execution
if __name__ == "__main__":
    analyzer = SentimentAnalyzer("data/cleaned_reviews.csv")
    analyzer.run_analysis()