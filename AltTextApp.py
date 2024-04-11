import streamlit as st
import google.generativeai as genai
import PIL.Image

genai.configure(api_key=st.secrets['GOOGLE_API_KEY'])

st.set_page_config(
    page_title="Alt-text and Image Description Generator",
    layout="centered"
)

st.header("Alternative Text Generator", divider='blue')
st.markdown("This prototype utilizes the free version of Google Gemini and should not be used with sensitive data.")
file = st.file_uploader("Upload the photo or image to generate alt-text and caption. If needed, use the toggle to provide additional context and regenerate the alt-text and caption", type=["jpg", "jpeg", "png"])
img, result = st.columns(2)
with img:
     if file is not None:
          image = PIL.Image.open(file)
          st.image(file,width=350)
on = st.toggle('Add context for the image.')
if on:
   user_text = st.text_input("Write context description")

with result:
    if file is not None:
        model = genai.GenerativeModel('gemini-pro-vision')
        response = model.generate_content(["Create alt-text for each image that meets WCAG 2.2 specifications. Suggest a short description for a caption.", image, user_text], stream=True)
        response.resolve()
        for candidate in response.candidates:
            st.write(part.text for part in candidate.content.parts)
        response.prompt_feedback
