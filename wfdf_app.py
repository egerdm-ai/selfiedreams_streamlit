import streamlit as st
import requests


# Function to send POST request to your Flask API
def send_query(query):
    data = {
        'query': query
    }
    url = st.secrets["url"]
    response = requests.post(url, json=data)
    return response.json()['answer']

# Chat history to display the conversation
chat_history = []

# Streamlit layout
st.title("Seçkin'in test etmesi için yapılan Streamlit App :D")

user_input = st.text_input("Buradan kurallarla ilgili soru sorabilirsiniz: ","Is it considered a foul if the thrower's hand hits the marker after the throw?")

if st.button('Send'):
    # Get the API response
    response = send_query(user_input)

    # Add the user query and API response to the chat history
    chat_history.append(('You', user_input))
    chat_history.append(('', response))

    # Display the chat history
    for chat in chat_history:
        st.markdown(f"**{chat[0]}**: {chat[1]}")

