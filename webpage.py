import streamlit as st
import ollama

st.set_page_config(page_title='Neelash Chat',page_icon='robot_face', layout='wide')


col1, col2 = st.columns(2)
st.image("C:/Users/Robonium/Downloads/cobolt.png", width=200)
st.markdown("<h1 style='text-align: center;'>Neelash's Chat</h1>", unsafe_allow_html=True)


# Create a placeholder for the output at the top of the page
output_placeholder = st.empty()

# Initialize an empty list to store the chat history
chat_history = []

user_input = st.text_input('Enter your message:')
send_button = st.button('Send', use_container_width=200)

if send_button and user_input:
    messages = [{'role': 'user', 'content': user_input}]
    stream = ollama.chat(model='cobolt', messages=messages, stream=True)

    output = f'You: {user_input}\n \n Assistant: '
    for chunk in stream:
        response = chunk['message']['content']
        if '\n' in response:
            lines = response.split('\n')
            output += ' '.join(lines) + '\n'
        else:
            output += response

    # Add the output to the chat history
    chat_history.append(output)

    # Use the placeholder to display the chat history
    for message in chat_history:
        output_placeholder.write(message)
