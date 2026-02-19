import streamlit as st
import pickle
import string
import nltk
import re
import numpy as np
from nltk.corpus import stopwords

# --- Page Config ---
st.set_page_config(page_title="AI Fake News Detector", page_icon="🔍")
st.title("🔍 Fake News Detector")

# Download stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# --- Load Model & Vectorizer ---
@st.cache_resource
def load_assets():
    try:
        model = pickle.load(open("model.pkl", "rb"))
        vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
        return model, vectorizer
    except FileNotFoundError:
        return None, None

model, vectorizer = load_assets()

if model is None:
    st.error("⚠️ model.pkl or vectorizer.pkl not found. Please run model.py first!")
    st.stop()

# --- Preprocessing Logic (Matches model.py exactly) ---
def clean_text(text):
    # 1. Strip "Reuters" source leakage if present
    if " - " in text:
        text = text.split(" - ", 1)[1]
    
    # 2. Lowercase and clean
    text = text.lower()
    text = re.sub(r'https?://\S+|www\.\S+', '', text) # Remove URLs
    text = re.sub(r'[^\w\s]', '', text)              # Remove punctuation
    
    # 3. Stopwords
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

# --- Prediction Function ---
def predict_news(text):
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])
    
    # Prediction
    prediction = model.predict(vec)[0]
    
    # PAC doesn't have predict_proba. We use decision_function 
    # to calculate a "Confidence" score based on distance from the boundary.
    decision_val = model.decision_function(vec)[0]
    # Convert distance to a 0-100% scale using a Sigmoid-like mapping
    confidence = (1 / (1 + np.exp(-abs(decision_val)))) * 100

    return prediction, confidence

# --- UI Layout ---
input_text = st.text_area("Paste the news article text below:", height=200)

if st.button("Analyze News"):
    if not input_text.strip():
        st.warning("Please enter some text to analyze.")
    else:
        with st.spinner('Analyzing patterns...'):
            result, confidence = predict_news(input_text)
            
            # Display Results
            st.divider()
            if result == "REAL":
                st.success(f"### Result: {result}")
                st.progress(confidence / 100)
                st.write(f"The model is **{round(confidence, 2)}%** confident this news is credible.")
            else:
                st.error(f"### Result: {result}")
                st.progress(confidence / 100)
                st.write(f"The model is **{round(confidence, 2)}%** confident this shows signs of misinformation.")

            # Highlight suspicious patterns
            st.markdown("---")
            st.markdown("### 🚩 Quick Analysis")
            suspicious_words = ["shocking", "secret", "banned", "miracle", "unbelievable", "exposed", "must-see"]
            found = [w for w in suspicious_words if w in input_text.lower()]
            
            if found:
                st.write(f"Found clickbait-style keywords: {', '.join(found)}")
            else:
                st.write("No typical clickbait keywords detected in the raw text.")