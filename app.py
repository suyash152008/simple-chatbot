import streamlit as st

st.title("🕷 Simple Chatbot")

name = st.chat_input("Type your message...")

if name:
    st.chat_message("human").write(name)

    if "hello" in name.lower():
        reply = "Hello! Sir, how can I help you?"
        
    elif "ai" in name.lower():
        reply = "AI means Artificial Intelligence."
        
    elif "what is the full form of upsc" in name.lower():
        reply = "Union Public Service Commission."
        
    elif "who is the president of india" in name.lower():
        reply = "The President of India."
        
    elif "who invented ethanol" in name.lower():
        reply = "Ethanol was not invented by one person; it has been known since ancient times."

    elif "who is abhijeet dipke"in name. lower():
        reply = "The biggest dimagi naxal👹."
        
    elif "bye" in name.lower():
        reply = "Goodbye!"
        
    else:
        reply = "Sorry, I don't understand."

    st.chat_message("assistant").write(reply)