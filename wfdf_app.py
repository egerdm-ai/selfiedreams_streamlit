import streamlit as st
import requests


# Function to send POST request to your Flask API
def send_query(query):
    data = {
        'query': query
    }
    response = requests.post('https://111b-34-86-206-243.ngrok-free.app/ask', json=data)
    print(response)  # print the raw response
    print(type(response))  # print the type of the response
    return response.json()

# Chat history to display the conversation
chat_history = []

# Streamlit layout
st.title("App made for Seçkin to test")

user_input = st.text_input("You can ask questions about the rules from here: ","Is it considered a foul if the thrower's hand hits the marker after the throw?")

if st.button('Send'):
    # Get the API response
    response = send_query(user_input)

    # Add the user query and AI response to the chat history
    chat_history.append(('You', user_input))
    chat_history.append(('AI', response['answer']))
    # Only add 'Source' to chat history if 'source_document' is in the response
    if 'source_document' in response:
        chat_history.append(('Source', response['source_document']))

    # Display the chat history
    for chat in chat_history:
        st.markdown(f"**{chat[0]}**: {chat[1]}")

