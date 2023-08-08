import streamlit as st
import requests

# Function to send POST request to your Flask API
def send_query(query):
    data = {
        'query': query
    }
    response = requests.post('https://4a95-34-86-206-243.ngrok-free.app/ask', json=data)
    return response.json()['answer']

# Chat history to display the conversation
chat_history = []

# Streamlit layout
st.title('Chatbot')

user_input = st.text_input("You: ")

if st.button('Send'):
    # Get the API response
    response = send_query(user_input)

    # Add the user query and API response to the chat history
    chat_history.append(('You', user_input))
    chat_history.append(('AI', response))

    # Display the chat history
    for chat in chat_history:
        st.markdown(f"**{chat[0]}**: {chat[1]}")

