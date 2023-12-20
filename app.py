import streamlit as st  # Main Streamlit library
from pydantic import BaseModel  # For data validation and settings management
from typing import List  # For type hinting
from helpers import structured_generator  # Assuming this is a custom module


class Titles(BaseModel):
    titles: List[str]


# Streamlit page configuration
st.set_page_config(page_title="Title Generator", layout="wide")

# Streamlit UI elements
st.title("Title Generator from URL")  # Page title

# Input field for the URL
input_url = st.text_input("Enter the URL", "https://www.bankbazaar.com/credit-card.html")

# Button to trigger title generation
generate_button = st.button("Generate Titles")


if generate_button:
    if input_url:
        # Constructing the prompt
        prompt = f"generate xml sitemap for {input_url}"
        
        # Assuming structured_generator function takes the model name, prompt, and the Titles class
        # and returns an instance of Titles
        try:
            result = structured_generator("gpt-4", prompt, Titles)
            if result.titles:
                # Displaying each title in a list
                st.subheader("Generated Titles")
                for title in result.titles:
                    st.write(title)
            else:
                st.error("No titles were generated.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please enter a URL.")
