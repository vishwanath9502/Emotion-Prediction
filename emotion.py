import streamlit as st
from joblib import load

image_path = 'Inno_logo_.png'  # Replace with your actual PNG image file path

# Specify the desired width and height
st.image(image_path, width=400)


# Load the model
loaded_model = load('best_model.joblib')

# Emotion-to-emoji mapping
emotion_emoji = {
    0: "😞 (Disheartened)",
    1: "😊 (Happy)",
    2: "❤️ (Compassionate)",
    3: "😡 (Angry))",
    4: "😟 (Scared/Anxious)",
    5: "🤩 (Enthralled)"
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
        # Get emoji and name based on prediction
        emoji = emotion_emoji.get(emotion, "Unknown Emotion")
        st.write(f"**Predicted Emotion:** {emoji}")
    else:
        st.write("Please enter some text to get a prediction.")