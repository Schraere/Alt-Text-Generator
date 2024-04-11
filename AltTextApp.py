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
file = st.file_uploader("Upload the photo or image you want the AI model to use to generate alt-text and description.", type=["jpg", "jpeg", "png"])
img, result = st.columns(2)

with img:
     if file is not None:
          image = PIL.Image.open(file)
          st.image(file,width=350)

with result:
    if file is not None:
        model = genai.GenerativeModel('gemini-pro-vision')
        response = model.generate_content(["Create alt-text for each image that meets WCAG 2.2 specifications.", image], stream=True)
        response.resolve()
        for candidate in response.candidates:
            st.write(part.text for part in candidate.content.parts)
        response.prompt_feedback
