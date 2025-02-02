import streamlit as st
import ollama

# Streamlit UI
st.title("🦙 Llama 3.2 Chatbot (Powered by Ollama)")
st.write("Ask me anything!")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate response from Ollama (Llama 3.2)
    response = ollama.chat(model="llama3.2", messages=st.session_state.messages)

    bot_reply = response["message"]["content"]

    # Display chatbot response
    with st.chat_message("assistant"):
        st.markdown(bot_reply)

    # Save chatbot response to chat history
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
