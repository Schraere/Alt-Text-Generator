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
if file is not None:
    image = PIL.Image.open(file)
    img, result = st.columns(2)
    with img:
        st.image(image, width=350)
    with result:
        model = genai.GenerativeModel('gemini-pro-vision')
        response = model.generate_content(["Create alt-text for each image that meets WCAG 2.2 specifications. Suggest a short description for a caption.", image], stream=True)
        response.resolve()
        for candidate in response.candidates:
            st.write(" ".join(part.text for part in candidate.content.parts))
    user_text = st.text_input("Provide additional context")
    if user_text:
        response = model.generate_content(["Create alt-text for each image that meets WCAG 2.2 specifications. Suggest a short description for a caption.", image, user_text], stream=True)
        response.resolve()
        for candidate in response.candidates:
            st.write(" ".join(part.text for part in candidate.content.parts))
