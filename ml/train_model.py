# numpy for num operation ,useful for handling array and math functions
# pandas lib for data manipulation and analysis , provides datastructures like dataframes
# train_test_split a function form scikit-learn for splitting data into training and tesing sets
# RandomForestClassifier  A machine learning model from scikit-learn used for classification 
# pickle a py module for serializing and deserializing python objects (saving and model models)
# ml/train_model.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import pickle

# Load your dataset

# Example: df = pd.read_csv('movie_reviews.csv')

# df should have columns 'review' and 'sentiment'

# Sample data (replace with actual data loading)
def load_data():
    data = {
        'review': ["I loved this movie", "I hated this movie", "It was okay", "Amazing film", "Worst movie ever"],
        'sentiment': [1, 0, 1, 1, 0]  # 1 for positive, 0 for negative
    }
    return pd.DataFrame(data)

df = load_data()
X = df['review']
y = df['sentiment']

# Convert text data to feature vectors
vectorizer = TfidfVectorizer()
X_features = vectorizer.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X_features, y, test_size=0.2, random_state=0)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Save the model and vectorizer
with open('model.pkl', 'wb') as f:
    pickle.dump((vectorizer, model), f)

print("Model trained and saved as 'model.pkl'")
