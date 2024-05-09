import streamlit as st
import ollama

# Pull and run the model
ollama.pull('tinyllama')
ollama.run('tinyllama')

# Create the Streamlit app
st.title('My Ollama Chatbot')

user_input = st.text_input('Enter your message:')
send_button = st.button('Send')

if send_button and user_input:
    messages = [{'role': 'user', 'content': user_input}]
    stream = ollama.chat(model='mistral', messages=messages, stream=True)

    for chunk in stream:
        response = chunk['message']['content']
        st.write(f'Assistant: {response}')
