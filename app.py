import streamlit as st
import joblib
from nltk.corpus import stopwords
import nltk
from nltk.corpus import stopwords



nltk.download('stopwords')

# Load model and vectorizer
model = joblib.load('fake_news_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# UI
st.title('📰 Fake News Detector')
st.write('Enter a news article or headline:')

user_input = st.text_area('News text input')

if user_input:
    cleaned_input = ' '.join([word for word in user_input.split() if word.lower() not in stopwords.words('english')])
    vectorized_input = vectorizer.transform([cleaned_input])
    prediction = model.predict(vectorized_input)

    if prediction == 0:
        st.error('⚠️ This looks like *Fake News*!')
    else:
        st.success('✅ This appears to be *Real News*!')

