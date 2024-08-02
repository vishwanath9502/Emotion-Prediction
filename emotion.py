import streamlit as st
from joblib import load

image_path = 'Inno_logo_.png'  # Replace with your actual PNG image file path

# Specify the desired width and height
st.image(image_path, width=400)

# Load the model
loaded_model = load('best_model.joblib')

# Emotion-to-emoji mapping with image path and emotion name
emotion_emoji = {
    0: ("Sad.png", "Sad"),
    1: ("Joy.png", "Joy"),
    2: ("Love.png", "Love"),
    3: ("Anger.png", "Anger"),
    4: ("Fear.png", "Fear"),
    5: ("Suprise.png", "Surprise")
}

# Function to predict emotion from text
def predict_emotion(text):
    prediction = loaded_model.predict([text])
    return prediction[0]

# Streamlit app layout
st.title("Emotion Prediction")
st.write("This app uses a machine learning model to predict the emotion from a given text.")

# Text input
input_text = st.text_area("Enter your text here:", "")

if st.button("Predict"):
    if input_text:
        # Predict emotion
        emotion = predict_emotion(input_text)
        # Get the path to the emoji image and the emotion name based on prediction
        emoji_data = emotion_emoji.get(emotion, None)
        
        if emoji_data:
            emoji_path, emotion_name = emoji_data
            st.image(emoji_path, width=100)  # Adjust the width as needed
            st.write(f"**Predicted Emotion:** {emotion_name}")
        else:
            st.write("Unknown Emotion")
    else:
        st.write("Please enter some text to get a prediction.")
