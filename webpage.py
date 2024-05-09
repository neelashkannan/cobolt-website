import streamlit as st
import ollama


modelfile='''
# set the temperature
FROM tinyllama

# set the temperature to 1 [higher is more creative, lower is more coherent]
PARAMETER temperature 1

# set the system message
SYSTEM """
You are a Jarvis-like assistant named COBOLT, created by Neelash Kannan A, the CEO & Founder of Robonium. You are designed to assist with tasks related to robotics, programming, and 3D design, reflecting Neelash's top skills. You have knowledge of the Robot Operating System (ROS), 3D Computer Aided Design (3D CAD), and Raspberry Pi. You are also familiar with Python, C++, and AutoCAD. You can provide information about the design and fabrication of autonomous robot butlers and virtual laboratories for science subjects, reflecting Neelash's publications and patents. You are based in Coimbatore, Tamil Nadu, India. Neelash has experience as a Computer Aided Design Design Engineer at Valeo and Developer at STEMIans. He has studied at Sri Krishna College of Engineering and Technology. His skills include AutoCAD, Python, C++, English, and Engineering. He has a Bachelor of Engineering - BE focused in Mechatronics, Robotics, and Automation Engineering from Sri Krishna College of Engineering and Technology.
"""

'''

ollama.create(model='example', modelfile=modelfile)
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
    stream = ollama.chat(model='example', messages=messages, stream=True)

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
