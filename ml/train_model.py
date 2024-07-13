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
def load_data(file_path='movie_reviews.csv'):
    try:
        df = pd.read_csv(file_path)
        return df
    except pd.errors.EmptyDataError:
        print(f"Error: The file {file_path} is empty or does not contain valid data.")
        return pd.DataFrame()  # Return an empty DataFrame

df = load_data()
if df.empty:
    print("No data loaded. Exiting.")
    exit()

# Ensure columns are present
if 'review' not in df.columns or 'sentiment' not in df.columns:
    print("Dataset must contain 'review' and 'sentiment' columns.")
    exit()

X = df['review']
y = df['sentiment']

# Convert text data to feature vectors
vectorizer = TfidfVectorizer(stop_words='english')  # Added stop words removal
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
