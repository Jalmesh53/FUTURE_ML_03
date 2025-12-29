import os
import json
import datetime
import csv
import nltk
import ssl
import streamlit as st
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("nltk_data"))
nltk.download('punkt')
nltk.download('punkt_tab')

# --- Part 1: Load & Preprocess Data ---
def load_data():
    with open('intents.json', 'r') as file:
        data = json.load(file)
    return data

data = load_data()

patterns = []
tags = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        patterns.append(pattern)
        tags.append(intent['tag'])

# --- Part 2: Train the Model ---
# Convert text to numbers using TF-IDF
vectorizer = TfidfVectorizer(tokenizer=nltk.word_tokenize, stop_words='english', max_features=5000)
X = vectorizer.fit_transform(patterns)
y = tags

# Train a simple classifier
clf = LogisticRegression(random_state=0, max_iter=10000)
clf.fit(X, y)

def chatbot_response(input_text):
    input_vector = vectorizer.transform([input_text])
    predicted_tag = clf.predict(input_vector)[0]
    
    for intent in data['intents']:
        if intent['tag'] == predicted_tag:
            return random.choice(intent['responses'])

# --- Part 3: Streamlit Interface ---
st.title("🤖 Customer Support Chatbot")
st.write("Welcome! Ask me anything about your order, returns, or contact info.")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("How can I help you?"):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get Bot Response
    response = chatbot_response(prompt)
    
    # Add bot message to history
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)

# --- Sidebar ---
st.sidebar.title("Chatbot Options")
if st.sidebar.button("Clear Chat History"):
    st.session_state.messages = []
st.sidebar.write("Built with NLTK & Streamlit")