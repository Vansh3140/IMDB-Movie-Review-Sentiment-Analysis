import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import SimpleRNN, Embedding, Dense
import streamlit as st

# Mapping the index to words for understanding

words_index = imdb.get_word_index()

reverse_word_index = {value:key for key, value in words_index.items()}

# loading the pre trained model

model = load_model('simple_rnn_imdb.h5')

# helper functions

def decode_review(encoded_review):

    return ' '.join([reverse_word_index.get(word-3, '?') for word in encoded_review])

def preprocess_text(text):

    words = text.lower().split()
    encoded_review = [words_index.get(word, 2) +3  for word in words]
    padded_review = sequence.pad_sequences([encoded_review], maxlen=500)
    return padded_review

# prediction function

def prediction(review):

    processed_input = preprocess_text(review)

    sentiment = model.predict(processed_input)

    if sentiment[0][0]>0.5:
        print("Positive")
        return "Positive", sentiment[0][0]
    else:
        print("Negative")
        return "Negative", sentiment[0][0]
    
# streamlit app

st.title("IMDB Movie Review Sentiment Analysis")
st.write("Enter a movie review to classify as positive and negative.")

# user input

user_input = st.text_area("Movie Review")

if st.button('Classify'):

    sentiment, score = prediction(user_input)

    st.write(f"Sentiment : {sentiment}")
    st.write(f"Prediction Score: {score}")