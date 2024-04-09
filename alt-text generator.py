import streamlit as st
import google.generativeai as genai
import PIL.Image

genai.configure(api_key=st.secrets['GOOGLE_API_KEY'])

st.set_page_config(
    page_title="Alt-text and Image Description Generator",
    layout="centered"
)

st.header("Upload one image at a time, 200MB max.", divider='rainbow')

file = st.file_uploader("Upload the photo or image you want the AI model to use to generate alt-text and description.", type=["jpg", "jpeg", "png"])
img, result = st.columns(2)

with img:
     if file is not None:
          image = PIL.Image.open(file)
          st.image(file,width=350)

with result:
    if file is not None:
        model = genai.GenerativeModel('gemini-pro-vision')
        response = model.generate_content(["Describe all content in the image, and generate a description suitable to be used for alt-text.", image], stream=True)
        response.resolve()
        for candidate in response.candidates:
            st.write(part.text for part in candidate.content.parts)
        response.prompt_feedback
