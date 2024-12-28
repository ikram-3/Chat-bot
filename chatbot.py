import google.generativeai as genai
import os
import re
import markdown
import streamlit as st
from IPython.display import HTML

# Configure API Key for Generative AI
API_KEY = "Your API Key Enter here"
genai.configure(api_key=API_KEY)

# Streamlit App Interface
st.title("Generative AI Chatbot")
st.markdown("Chatbot powered by Google's Gemini 1.5 model.")

# User input section
input_text = st.text_input("Enter your prompt:", "")

if st.button("Generate Response"):
    if input_text.strip():
        try:
            # Create the model instance
            model = genai.GenerativeModel("gemini-1.5-flash")

            # Generate response
            response = model.generate_content(input_text)
            generated_text = response.text  # Adjust based on API's actual response format
            
         
            colored_text = re.sub(r'\*\*(.*?)\*\*', r'<span style="color: green; font-weight: bold;">\1</span>', generated_text)
            colored_text = colored_text.replace("*", "<br> <li>")
            colored_text = colored_text.replace("##", "<br>")

    
            st.write("Raw Response:")
            import time
            for i in generated_text.split("\n"):
                st.write(i)
                time.sleep(0.7)  
            
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a prompt to generate a response.")
