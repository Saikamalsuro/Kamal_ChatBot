import os
import streamlit as st
import google.generativeai as genai

# Configure API key (better from environment variable)
genai.configure(api_key="AIzaSyBaKeUYwr0dN0yWkyvQaJe8exZHfHnOaIc")


# Create the model
model = genai.GenerativeModel("gemini-1.5-flash")

st.title("Kamal's Chatbot 🥷")
st.write("Welcome to the Kamal Chatbot application!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "ai", "content": "Hi there! I am a Kamal's Assistant. How can I help you today?"}
    ]

# Display previous chat messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Chat input
human_prompt = st.chat_input("Say Something...")

if human_prompt:
    # Add user message
    st.session_state.messages.append({"role": "human", "content": human_prompt})
    st.chat_message("human").write(human_prompt)

    # Get AI response
    response = model.generate_content(human_prompt)
    ai_reply = response.text

    # Add AI message
    st.session_state.messages.append({"role": "ai", "content": ai_reply})
    st.chat_message("ai").write(ai_reply)
