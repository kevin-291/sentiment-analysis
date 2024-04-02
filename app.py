from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax
import streamlit as st


MODEL = f"cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

def analyse_sentiment(text):
    encoded_text = tokenizer(text, return_tensors = 'pt')
    output = model(**encoded_text)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    return scores[0], scores[1], scores[2]

def main():
    st.title("Sentiment Analysis App")

    msg = st.text_area("Enter text for sentiment analysis")

    if st.button("Analyse"):
        if msg:
            negative, neutral, positive = analyse_sentiment(msg)
            max_val = max(negative, neutral, positive)
            if max_val == negative:
                st.text(body=f'The statement is negative ({negative*100:.2f}%)')
            elif max_val == neutral:
                st.text(body=f'The statement is neutral ({neutral*100:.2f}%)')
            elif max_val == positive:
                st.text(body=f'The statement is positive ({positive*100:.2f}%)')
        else:
            st.write("Please enter some text for analysis.")

if __name__ == '__main__':
    main()
            
